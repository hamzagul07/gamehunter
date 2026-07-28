#!/usr/bin/env python3
"""
GameHunter v1 -- an automated conjecture-hunting engine for impartial combinatorial games.

Architecture (FunSearch-style, student scale):
    PROPOSER  -> random/evolutionary mutation of game rules written in a tiny DSL
                 (an LLM can be wired in as an extra proposer; see README §5)
    VERIFIER  -> deterministic Grundy-value engine (Sprague-Grundy theory)
    DETECTORS -> deterministic pattern finders (periodicity, arithmetic periodicity,
                 modular / digit-sum characterizations of P-positions)
    FILTER    -> OEIS lookup to kill already-known sequences (online only)
    SELECTOR  -> interestingness score drives the evolutionary loop
    HUMAN     -> you. The machine outputs CONJECTURES. Only your proof makes a discovery.

Zero dependencies: Python 3.9+ standard library only.

Usage:
    python3 game_hunter.py demo                     # detectors rediscover known theorems
    python3 game_hunter.py hunt --gens 15 --pop 24  # search for new games
    python3 game_hunter.py analyze --game digits10  # analyze a built-in game
    python3 game_hunter.py analyze --rule '["union", ["digits", 10], ["const", [3]]]'
"""

from __future__ import annotations
import argparse
import json
import math
import os
import random
import sys
import time
import hashlib
from urllib import request as urlreq
from urllib import parse as urlparse

# ----------------------------------------------------------------------------
# 0. Globals
# ----------------------------------------------------------------------------

MAX_RULE_NODES = 9          # complexity cap for evolved rules
OEIS_TERMS = 24             # how many terms to send to OEIS
OEIS_SLEEP = 1.0            # be polite to OEIS servers
FIBS: list[int] = []        # filled lazily


def _fibs_upto(n: int) -> list[int]:
    global FIBS
    if not FIBS:
        FIBS = [1, 2]
    while FIBS[-1] <= n:
        FIBS.append(FIBS[-1] + FIBS[-2])
    return [f for f in FIBS if f <= n]


# ----------------------------------------------------------------------------
# 1. The DSL -- rules are nested lists (JSON-serializable s-expressions)
# ----------------------------------------------------------------------------
# Leaves (move-set generators; every move s must satisfy 1 <= s <= n):
#   ["const", [a, b, ...]]      fixed subtraction set
#   ["range", a, b]             {a, a+1, ..., b}
#   ["digits", base]            nonzero digits of n written in `base`
#   ["divisors"]                proper divisors of n (1 <= d < n)
#   ["squares"]                 positive perfect squares <= n
#   ["fib"]                     Fibonacci numbers <= n   (1,2,3,5,8,...)
#   ["powers", k]               powers of k <= n         (1,k,k^2,...)
#   ["halve"]                   the single move ceil(n/2)
# Combinators:
#   ["union", A, B]  ["inter", A, B]  ["diff", A, B]
#   ["modfilter", m, r, A]      keep s in A with s % m == r
#   ["ifmod", m, r, A, B]       use A when n % m == r, else B
#   ["shift", c, A]             {s + c : s in A}
#   ["capmax", c, A]            keep s in A with s <= c

LEAF_OPS = {"const", "range", "digits", "divisors", "squares", "fib", "powers", "halve"}
COMB_OPS = {"union", "inter", "diff", "modfilter", "ifmod", "shift", "capmax"}


def compile_rule(rule):
    """Return f(n) -> set of legal subtraction amounts. Deterministic, side-effect free."""
    op = rule[0]

    if op == "const":
        S = set(rule[1])
        return lambda n: {s for s in S if 1 <= s <= n}

    if op == "range":
        a, b = rule[1], rule[2]
        return lambda n: set(range(a, min(b, n) + 1)) if n >= a else set()

    if op == "digits":
        base = rule[1]

        def f(n, base=base):
            s, m = set(), n
            while m:
                s.add(m % base)
                m //= base
            s.discard(0)
            return {x for x in s if x <= n}
        return f

    if op == "divisors":
        def f(n):
            if n <= 1:
                return set()
            s = {1}
            i = 2
            while i * i <= n:
                if n % i == 0:
                    s.add(i)
                    s.add(n // i)
                i += 1
            s.discard(n)
            return s
        return f

    if op == "squares":
        return lambda n: {k * k for k in range(1, math.isqrt(n) + 1)}

    if op == "fib":
        return lambda n: set(_fibs_upto(n))

    if op == "powers":
        k = rule[1]

        def f(n, k=k):
            s, v = set(), 1
            while v <= n:
                s.add(v)
                v *= k
            return s
        return f

    if op == "halve":
        return lambda n: {(n + 1) // 2} if n >= 1 else set()

    # ---- combinators ----
    if op == "union":
        fa, fb = compile_rule(rule[1]), compile_rule(rule[2])
        return lambda n: fa(n) | fb(n)

    if op == "inter":
        fa, fb = compile_rule(rule[1]), compile_rule(rule[2])
        return lambda n: fa(n) & fb(n)

    if op == "diff":
        fa, fb = compile_rule(rule[1]), compile_rule(rule[2])
        return lambda n: fa(n) - fb(n)

    if op == "modfilter":
        m, r = rule[1], rule[2]
        fa = compile_rule(rule[3])
        return lambda n: {s for s in fa(n) if s % m == r}

    if op == "ifmod":
        m, r = rule[1], rule[2]
        fa, fb = compile_rule(rule[3]), compile_rule(rule[4])
        return lambda n: fa(n) if n % m == r else fb(n)

    if op == "shift":
        c = rule[1]
        fa = compile_rule(rule[2])
        return lambda n: {s + c for s in fa(n) if s + c <= n}

    if op == "capmax":
        c = rule[1]
        fa = compile_rule(rule[2])
        return lambda n: {s for s in fa(n) if s <= c}

    raise ValueError(f"unknown op: {op}")


def pretty(rule) -> str:
    op = rule[0]
    if op == "const":
        return "{" + ",".join(map(str, rule[1])) + "}"
    if op == "range":
        return f"{{{rule[1]}..{rule[2]}}}"
    if op == "digits":
        return f"nonzero base-{rule[1]} digits of n"
    if op == "divisors":
        return "proper divisors of n"
    if op == "squares":
        return "squares \u2264 n"
    if op == "fib":
        return "Fibonacci numbers \u2264 n"
    if op == "powers":
        return f"powers of {rule[1]} \u2264 n"
    if op == "halve":
        return "\u2308n/2\u2309 only"
    if op == "union":
        return f"({pretty(rule[1])} \u222a {pretty(rule[2])})"
    if op == "inter":
        return f"({pretty(rule[1])} \u2229 {pretty(rule[2])})"
    if op == "diff":
        return f"({pretty(rule[1])} \\ {pretty(rule[2])})"
    if op == "modfilter":
        return f"[s\u2261{rule[2]} (mod {rule[1]}) in {pretty(rule[3])}]"
    if op == "ifmod":
        return f"[if n\u2261{rule[2]} (mod {rule[1]}): {pretty(rule[3])} else: {pretty(rule[4])}]"
    if op == "shift":
        return f"({pretty(rule[2])} + {rule[1]})"
    if op == "capmax":
        return f"[s\u2264{rule[1]} in {pretty(rule[2])}]"
    return str(rule)


def rule_size(rule) -> int:
    op = rule[0]
    if op in LEAF_OPS:
        return 1
    if op in ("union", "inter", "diff"):
        return 1 + rule_size(rule[1]) + rule_size(rule[2])
    if op == "modfilter":
        return 1 + rule_size(rule[3])
    if op == "ifmod":
        return 1 + rule_size(rule[3]) + rule_size(rule[4])
    if op in ("shift", "capmax"):
        return 1 + rule_size(rule[2])
    return 1


# ----------------------------------------------------------------------------
# 2. Proposer -- random generation and mutation of rules
# ----------------------------------------------------------------------------

def random_leaf(rng: random.Random):
    choice = rng.choice(
        ["const", "const", "range", "digits", "digits", "divisors",
         "squares", "fib", "powers", "halve"]
    )
    if choice == "const":
        k = rng.randint(1, 3)
        return ["const", sorted(rng.sample(range(1, 10), k))]
    if choice == "range":
        a = rng.randint(1, 4)
        return ["range", a, a + rng.randint(0, 5)]
    if choice == "digits":
        return ["digits", rng.choice([2, 3, 4, 5, 8, 10, 12])]
    if choice == "powers":
        return ["powers", rng.choice([2, 3])]
    return [choice]


def random_rule(rng: random.Random, depth: int = 2):
    if depth <= 0 or rng.random() < 0.45:
        return random_leaf(rng)
    op = rng.choice(["union", "union", "diff", "inter",
                     "modfilter", "ifmod", "shift", "capmax"])
    if op in ("union", "inter", "diff"):
        return [op, random_rule(rng, depth - 1), random_rule(rng, depth - 1)]
    if op == "modfilter":
        m = rng.randint(2, 5)
        return [op, m, rng.randint(0, m - 1), random_rule(rng, depth - 1)]
    if op == "ifmod":
        m = rng.randint(2, 6)
        return [op, m, rng.randint(0, m - 1),
                random_rule(rng, depth - 1), random_rule(rng, depth - 1)]
    if op == "shift":
        return [op, rng.randint(1, 3), random_rule(rng, depth - 1)]
    return ["capmax", rng.randint(2, 9), random_rule(rng, depth - 1)]


def _all_subnodes(rule, path=()):
    """Yield (path, subrule) for every rule-valued node."""
    yield path, rule
    op = rule[0]
    idxs = []
    if op in ("union", "inter", "diff"):
        idxs = [1, 2]
    elif op == "modfilter":
        idxs = [3]
    elif op == "ifmod":
        idxs = [3, 4]
    elif op in ("shift", "capmax"):
        idxs = [2]
    for i in idxs:
        yield from _all_subnodes(rule[i], path + (i,))


def _replace_at(rule, path, new):
    if not path:
        return new
    out = list(rule)
    out[path[0]] = _replace_at(rule[path[0]], path[1:], new)
    return out


def mutate(rule, rng: random.Random):
    r = json.loads(json.dumps(rule))  # deep copy
    nodes = list(_all_subnodes(r))
    path, node = rng.choice(nodes)
    roll = rng.random()

    if roll < 0.35:                                   # replace subtree
        return _replace_at(r, path, random_rule(rng, 1))
    if roll < 0.55:                                   # wrap subtree
        wrap = rng.choice(["union", "modfilter", "shift", "capmax", "ifmod"])
        if wrap == "union":
            new = ["union", node, random_leaf(rng)]
        elif wrap == "modfilter":
            m = rng.randint(2, 5)
            new = ["modfilter", m, rng.randint(0, m - 1), node]
        elif wrap == "shift":
            new = ["shift", rng.randint(1, 3), node]
        elif wrap == "capmax":
            new = ["capmax", rng.randint(2, 9), node]
        else:
            m = rng.randint(2, 6)
            new = ["ifmod", m, rng.randint(0, m - 1), node, random_leaf(rng)]
        return _replace_at(r, path, new)
    if roll < 0.75:                                   # tweak parameters in place
        op = node[0]
        if op == "const":
            node[1] = sorted(set(node[1] + [rng.randint(1, 9)]))[:4]
        elif op == "range":
            node[1] = max(1, node[1] + rng.choice([-1, 1]))
            node[2] = max(node[1], node[2] + rng.choice([-1, 1]))
        elif op == "digits":
            node[1] = rng.choice([2, 3, 4, 5, 8, 10, 12])
        elif op == "powers":
            node[1] = rng.choice([2, 3])
        elif op in ("modfilter", "ifmod"):
            node[1] = rng.randint(2, 6)
            node[2] = rng.randint(0, node[1] - 1)
        elif op in ("shift", "capmax"):
            node[1] = max(1, node[1] + rng.choice([-1, 1]))
        return r
    # unwrap: replace a combinator by one of its children
    comb = [(p, nd) for p, nd in nodes if nd[0] in COMB_OPS]
    if comb:
        p, nd = rng.choice(comb)
        child = nd[3] if nd[0] == "modfilter" else (
            nd[2] if nd[0] in ("shift", "capmax") else nd[rng.choice([1, 2])]
            if nd[0] in ("union", "inter", "diff") else nd[rng.choice([3, 4])]
        )
        return _replace_at(r, p, child)
    return _replace_at(r, path, random_leaf(rng))


def valid(rule) -> bool:
    if rule_size(rule) > MAX_RULE_NODES:
        return False
    try:
        f = compile_rule(rule)
        nonempty = 0
        for n in range(1, 61):
            s = f(n)
            for x in s:
                if not (1 <= x <= n):
                    return False
            if n >= 5 and s:
                nonempty += 1
        return nonempty >= 8  # the game must not be dead
    except Exception:
        return False


# ----------------------------------------------------------------------------
# 3. Verifier -- the Grundy engine (Sprague-Grundy theory, normal play)
# ----------------------------------------------------------------------------

def grundy_sequence(rule, N: int) -> list[int]:
    f = compile_rule(rule)
    G = [0] * (N + 1)
    for n in range(1, N + 1):
        seen = {G[n - s] for s in f(n)}
        g = 0
        while g in seen:
            g += 1
        G[n] = g
    return G


# ----------------------------------------------------------------------------
# 4. Detectors -- deterministic pattern finders (no AI anywhere in here)
# ----------------------------------------------------------------------------

def eventual_period(seq, start=1, max_p=None):
    a = seq[start:]
    L = len(a)
    if L < 60:
        return None
    if max_p is None:
        max_p = max(4, L // 5)
    for p in range(1, max_p + 1):
        i = L - p - 1
        while i >= 0 and a[i] == a[i + p]:
            i -= 1
        q = i + 1
        tail = L - q
        if tail >= max(3 * p, 40) and q <= L // 2:
            return {"preperiod": q + start, "period": p}
    return None


def arithmetic_periodic(seq, start=1, max_p=80):
    a = seq[start:]
    L = len(a)
    if L < 80:
        return None
    for p in range(1, min(max_p, L // 4) + 1):
        d = a[L - 1] - a[L - 1 - p]
        if d <= 0:
            continue
        i = L - p - 1
        while i >= 0 and a[i + p] - a[i] == d:
            i -= 1
        q = i + 1
        tail = L - q
        if tail >= max(3 * p, 40) and q <= L // 2:
            return {"preperiod": q + start, "period": p, "saltus": d}
    return None


def residue_characterization(G, max_m=40):
    """P-positions (G=0) exactly = a set of residues mod m, for n past a preperiod."""
    N = len(G) - 1
    q0 = min(40, max(10, N // 10))
    for m in range(2, max_m + 1):
        P, W = set(), set()
        for n in range(q0, N + 1):
            (P if G[n] == 0 else W).add(n % m)
        if P and W and not (P & W):
            # walk back: find the minimal n0 from which the law actually holds
            n0 = q0
            while n0 > 1 and ((G[n0 - 1] == 0) == ((n0 - 1) % m in P)):
                n0 -= 1
            return {"modulus": m, "residues": sorted(P), "from": n0}
    return None


def _digitsum(n, b):
    s = 0
    while n:
        s += n % b
        n //= b
    return s


def digitsum_characterization(G):
    N = len(G) - 1
    q0 = min(40, max(10, N // 10))
    for b in (2, 3, 4, 5, 10):
        for k in range(2, 6):
            P, W = set(), set()
            for n in range(q0, N + 1):
                r = _digitsum(n, b) % k
                (P if G[n] == 0 else W).add(r)
            if P and W and not (P & W):
                return {"base": b, "mod": k, "residues": sorted(P), "from": q0}
    return None


def game_stats(rule, G):
    N = len(G) - 1
    f = compile_rule(rule)
    tail = G[max(1, N // 2):]
    distinct = len(set(tail))
    p_positions = [n for n in range(1, N + 1) if G[n] == 0]
    q0 = min(40, max(10, N // 10))
    p_tail = [n for n in p_positions if n >= q0]
    sample_ns = [max(2, N // 3), max(3, 2 * N // 3), N]
    branching = sum(len(f(n)) for n in sample_ns) / len(sample_ns)
    static = f(sample_ns[0]) == f(sample_ns[1]) == f(sample_ns[2]) and branching <= 12
    dull = (len(p_tail) == 0) or (len(p_tail) >= (N - q0) * 0.98) or (distinct <= 1)
    return {
        "distinct_tail_values": distinct,
        "p_positions": p_positions,
        "branching": round(branching, 1),
        "static_set": static,
        "dull": dull,
    }


def detect_all(rule, G):
    stats = game_stats(rule, G)
    det = {
        "arith": arithmetic_periodic(G),
        "period": eventual_period(G),
        "residue": None,
        "digitsum": None,
    }
    if det["arith"] and det["period"]:
        det["arith"] = None  # plain periodicity subsumes; keep the simpler statement
    if not det["period"]:
        det["residue"] = residue_characterization(G)
        if not det["residue"]:
            det["digitsum"] = digitsum_characterization(G)
    return det, stats


# ----------------------------------------------------------------------------
# 5. Conjecture drafting -- turn detections into precise statements
# ----------------------------------------------------------------------------

PROOF_HINT = ("Proof strategy: induction on n. Show (i) every move from a claimed "
              "P-position lands on a claimed N-position, and (ii) from every claimed "
              "N-position some move lands on a claimed P-position.")


def draft_conjectures(det, stats):
    out = []
    if det["period"]:
        d = det["period"]
        out.append(f"CONJECTURE: G(n + {d['period']}) = G(n) for all n \u2265 {d['preperiod']} "
                   f"(period {d['period']}, preperiod {d['preperiod']}).")
    if det["arith"]:
        d = det["arith"]
        out.append(f"CONJECTURE: G(n + {d['period']}) = G(n) + {d['saltus']} for all "
                   f"n \u2265 {d['preperiod']} (arithmetic-periodic, saltus {d['saltus']}).")
    if det["residue"]:
        d = det["residue"]
        rs = ", ".join(map(str, d["residues"]))
        out.append(f"CONJECTURE: for n \u2265 {d['from']}, the P-positions are exactly "
                   f"n \u2261 {rs} (mod {d['modulus']}).")
    if det["digitsum"]:
        d = det["digitsum"]
        rs = ", ".join(map(str, d["residues"]))
        out.append(f"CONJECTURE: for n \u2265 {d['from']}, n is a P-position iff the "
                   f"base-{d['base']} digit sum of n \u2261 {rs} (mod {d['mod']}).")
    if out:
        out.append(PROOF_HINT)
    else:
        out.append("No clean global structure detected at this range. Options: raise --N, "
                   "study the P-position sequence directly, or discard.")
    return out


# ----------------------------------------------------------------------------
# 6. Interestingness score -- drives evolution
# ----------------------------------------------------------------------------

def score_game(det, stats, size):
    notes = []
    if stats["dull"]:
        return 0.1, "DULL", ["degenerate game (P-positions vanish or dominate)"]
    if det["arith"]:
        score, tier = 8.0, "ARITHMETIC_PERIODIC"
        notes.append("rare elegant structure")
    elif det["period"]:
        p = det["period"]["period"]
        score, tier = 5.0 + 3.0 / math.sqrt(p), "PERIODIC"
        if stats["static_set"]:
            score -= 2.5
            notes.append("static finite subtraction set: eventual periodicity is a "
                         "classical theorem, so novelty is limited")
        if p >= 10:
            score += 0.8
            notes.append(f"unusually long period {p} for so simple a rule")
    elif det["residue"]:
        score, tier = 7.5, "HIDDEN_MOD_STRUCTURE"
        notes.append("Grundy values look chaotic but win/loss is cleanly modular -- "
                     "ideal theorem material")
    elif det["digitsum"]:
        score, tier = 8.5, "DIGIT_STRUCTURED"
        notes.append("digit-sum law: provable by base-b induction, very classroom-friendly")
    else:
        score, tier = 2.0, "CHAOTIC"
        if stats["distinct_tail_values"] <= 6:
            score += 1.0
            notes.append("Grundy values bounded -- structure may exist deeper")
    score -= 0.12 * size
    return round(score, 2), tier, notes


# ----------------------------------------------------------------------------
# 7. OEIS filter -- novelty check (finalists only; polite; cached; offline-safe)
# ----------------------------------------------------------------------------

def load_cache(path):
    if os.path.exists(path):
        with open(path) as fh:
            return json.load(fh)
    return {}


def save_cache(path, cache):
    with open(path, "w") as fh:
        json.dump(cache, fh)


def oeis_lookup(terms, cache, offline):
    terms = [t for t in terms][:OEIS_TERMS]
    if len(terms) < 8:
        return {"status": "too_short"}
    key = ",".join(map(str, terms))
    if key in cache:
        return cache[key]
    if offline:
        return {"status": "offline"}
    url = "https://oeis.org/search?fmt=json&q=" + urlparse.quote(key)
    try:
        req = urlreq.Request(url, headers={"User-Agent": "GameHunter-student-project"})
        with urlreq.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode())
        time.sleep(OEIS_SLEEP)
        # OEIS now returns a bare JSON array of results (null when no match);
        # older versions returned {"count": n, "results": [...]}. Accept both.
        if data is None:
            results = []
        elif isinstance(data, list):
            results = data
        else:
            results = data.get("results") or []
        count = len(results)
        if count == 0:
            res = {"status": "not_found"}
        elif results:
            res = {"status": "found",
                   "A": f"A{results[0]['number']:06d}",
                   "name": results[0].get("name", "")[:90],
                   "count": count}
        else:
            res = {"status": "found_many", "count": count}
        cache[key] = res
        return res
    except Exception as e:
        return {"status": "error", "detail": str(e)[:80]}


# ----------------------------------------------------------------------------
# 8. LLM proposer hook (optional; see README §5)
# ----------------------------------------------------------------------------

def llm_propose(hall_of_fame_reports):
    """Return a list of candidate rules (DSL nested lists) proposed by your LLM.

    v1 returns []. If you wire an LLM in, remember the firewall: every proposal
    goes through the same validate() + Grundy engine + detectors as any random
    mutation. The LLM proposes; the verifier decides. Never skip verification.
    """
    return []


# ----------------------------------------------------------------------------
# 9. Analysis + reporting
# ----------------------------------------------------------------------------

def analyze_rule(rule, N, oeis_cache=None, offline=True, deep=False):
    G = grundy_sequence(rule, N)
    det, stats = detect_all(rule, G)
    score, tier, notes = score_game(det, stats, rule_size(rule))
    rec = {
        "rule": rule,
        "pretty": pretty(rule),
        "size": rule_size(rule),
        "N": N,
        "tier": tier,
        "score": score,
        "notes": notes,
        "detections": det,
        "stats": {k: v for k, v in stats.items() if k != "p_positions"},
        "G_head": G[1:31],
        "p_positions_head": stats["p_positions"][:25],
        "conjectures": draft_conjectures(det, stats),
        "game_hash": hashlib.sha1(str(G[1:min(N, 300)]).encode()).hexdigest()[:12],
    }
    if deep and oeis_cache is not None:
        rec["oeis_p_positions"] = oeis_lookup(stats["p_positions"], oeis_cache, offline)
        rec["oeis_grundy"] = oeis_lookup(G[1:], oeis_cache, offline)
        for key in ("oeis_p_positions", "oeis_grundy"):
            r = rec[key]
            if r["status"] == "not_found":
                rec["score"] = round(rec["score"] + 2.0, 2)
                rec["notes"].append(f"{key}: ABSENT from OEIS -- novelty candidate")
            elif r["status"] == "found":
                rec["score"] = round(rec["score"] - 1.0, 2)
                rec["notes"].append(f"{key}: matches {r['A']} ({r['name']})")
    return rec


def print_report(rec, verbose=True):
    print("=" * 78)
    print(f"GAME: subtract s \u2208 {rec['pretty']}")
    print(f"  DSL: {json.dumps(rec['rule'])}")
    print(f"  tier={rec['tier']}  score={rec['score']}  size={rec['size']}  "
          f"N={rec['N']}  hash={rec['game_hash']}")
    print(f"  G(1..30)      : {rec['G_head']}")
    print(f"  P-positions   : {rec['p_positions_head']} ...")
    for n in rec["notes"]:
        print(f"  note: {n}")
    for k in ("oeis_p_positions", "oeis_grundy"):
        if k in rec:
            print(f"  {k}: {rec[k]}")
    if verbose:
        for c in rec["conjectures"]:
            print(f"  {c}")


# ----------------------------------------------------------------------------
# 10. The hunt -- evolutionary loop
# ----------------------------------------------------------------------------

def known_classic_hashes():
    """Fingerprints of known games/families (stable for any N >= 300)."""
    fams = [(f"digits{b}", ["digits", b]) for b in range(2, 13)]
    fams += [(f"powers{k}", ["powers", k]) for k in (2, 3)]
    fams += [(f"range1-{b}", ["range", 1, b]) for b in range(1, 10)]
    fams += list(BUILTIN.items())
    out = {}
    for name, rule in fams:
        G = grundy_sequence(rule, 320)
        out[hashlib.sha1(str(G[1:300]).encode()).hexdigest()[:12]] = name
    return out


def hunt(args):
    rng = random.Random(args.seed)
    oeis_cache = load_cache(args.cache)
    known = known_classic_hashes()
    t0 = time.time()

    population = []
    while len(population) < args.pop:
        r = random_rule(rng, 2)
        if valid(r):
            population.append(r)

    hof = {}  # game_hash -> record
    for gen in range(1, args.gens + 1):
        scored = []
        seen_this_gen = set()
        for rule in population:
            rec = analyze_rule(rule, args.N)
            if rec["game_hash"] in seen_this_gen:
                continue  # same game in disguise; keep one representative
            seen_this_gen.add(rec["game_hash"])
            if rec["game_hash"] in known:
                rec["score"] = round(rec["score"] - 4.0, 2)
                rec["notes"].append(f"identical to known classic '{known[rec['game_hash']]}' "
                                    "-- great sanity check, zero novelty")
            scored.append(rec)
            old = hof.get(rec["game_hash"])
            if old is None or rec["score"] > old["score"]:
                hof[rec["game_hash"]] = rec
        scored.sort(key=lambda r: r["score"], reverse=True)
        best = scored[0]
        print(f"[gen {gen:>3}] pop={len(scored):>3} best={best['score']:>5}  "
              f"{best['tier']:<22} {best['pretty'][:52]}")

        elite = [r["rule"] for r in scored[: max(3, args.pop // 4)]]
        nxt = list(elite)
        nxt += [m for m in llm_propose(list(hof.values())) if valid(m)]
        while len(nxt) < args.pop:
            if rng.random() < 0.8 and elite:
                cand = mutate(rng.choice(elite), rng)
            else:
                cand = random_rule(rng, 2)
            if valid(cand):
                nxt.append(cand)
        population = nxt

    finalists = sorted(hof.values(), key=lambda r: r["score"], reverse=True)[: args.top]
    print(f"\nDeep verification of {len(finalists)} finalists at N={args.deepN} "
          f"+ OEIS novelty check ({'OFFLINE' if args.offline else 'online'})...\n")
    deep = []
    for r in finalists:
        deep.append(analyze_rule(r["rule"], args.deepN, oeis_cache, args.offline, deep=True))
    deep.sort(key=lambda r: r["score"], reverse=True)
    for r in deep:
        print_report(r)

    save_cache(args.cache, oeis_cache)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    out_json = os.path.join(args.outdir, f"report_{stamp}.json")
    with open(out_json, "w") as fh:
        json.dump({"seed": args.seed, "args": vars(args), "finalists": deep}, fh, indent=1)
    with open(os.path.join(args.outdir, "hunt_log.jsonl"), "a") as fh:
        fh.write(json.dumps({"stamp": stamp, "seed": args.seed,
                             "best": deep[0]["pretty"] if deep else None,
                             "best_score": deep[0]["score"] if deep else None}) + "\n")
    print(f"\nSaved full report -> {out_json}")
    print(f"Elapsed: {time.time() - t0:.1f}s.  Reproduce with --seed {args.seed}.")
    print("\nREMEMBER: everything above is a CONJECTURE until you prove it. "
          "Verify by hand at small n, re-run at higher --deepN, then start the induction.")


# ----------------------------------------------------------------------------
# 11. Demo -- detectors rediscover known theorems (trust-building + tutorial)
# ----------------------------------------------------------------------------

DEMO_GAMES = [
    (["const", [1, 2, 3]], "classic subtraction {1,2,3}: expect period 4, G(n) = n mod 4"),
    (["powers", 2], "subtract a power of 2: expect P-positions = multiples of 3"),
    (["divisors"], "subtract a proper divisor: expect P-positions = odd n"),
    (["digits", 10], "subtract a nonzero decimal digit of n: expect P = multiples of 10"),
    (["squares"], "subtract a square: famously chaotic; P-positions are OEIS A030193 "
                  "(the online OEIS check should recognize it)"),
]

BUILTIN = {"sub123": ["const", [1, 2, 3]], "pow2": ["powers", 2],
           "divisors": ["divisors"], "digits10": ["digits", 10],
           "squares": ["squares"], "fib": ["fib"]}


def demo(args):
    oeis_cache = load_cache(args.cache)
    print("GameHunter demo: the detectors should REDISCOVER known theorems.\n")
    for rule, expect in DEMO_GAMES:
        print(f">>> {expect}")
        rec = analyze_rule(rule, args.N, oeis_cache, args.offline, deep=True)
        print_report(rec)
        print()
    save_cache(args.cache, oeis_cache)
    print("If the detections above match the expectations, the engine is telling the "
          "truth.\nNow run a hunt:  python3 game_hunter.py hunt")


# ----------------------------------------------------------------------------
# 12. CLI
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="GameHunter v1")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--N", type=int, default=1200)
        p.add_argument("--offline", action="store_true",
                       help="skip OEIS lookups (auto-fallback on network errors)")
        p.add_argument("--cache", default="oeis_cache.json")
        p.add_argument("--outdir", default=".")

    p = sub.add_parser("demo"); common(p)
    p = sub.add_parser("analyze"); common(p)
    p.add_argument("--rule", help='DSL as JSON, e.g. \'["union",["digits",10],["const",[3]]]\'')
    p.add_argument("--game", choices=sorted(BUILTIN), help="built-in game name")
    p = sub.add_parser("hunt"); common(p)
    p.add_argument("--gens", type=int, default=15)
    p.add_argument("--pop", type=int, default=24)
    p.add_argument("--top", type=int, default=8)
    p.add_argument("--deepN", type=int, default=5000)
    p.add_argument("--seed", type=int, default=random.randrange(10**6))

    args = ap.parse_args()
    if args.cmd == "demo":
        demo(args)
    elif args.cmd == "analyze":
        rule = BUILTIN[args.game] if args.game else json.loads(args.rule)
        if not valid(rule):
            sys.exit("rule failed validation (illegal moves, dead game, or too large)")
        cache = load_cache(args.cache)
        print_report(analyze_rule(rule, args.N, cache, args.offline, deep=True))
        save_cache(args.cache, cache)
    else:
        hunt(args)


if __name__ == "__main__":
    main()
