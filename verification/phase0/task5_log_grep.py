#!/usr/bin/env python3
"""Phase 0, Task 5 -- log grep for Grundy retrodictions.

PROVENANCE. Written and executed locally in this repository; the output
pasted below is this file's own output and a re-run reproduces it.

READ-ONLY. hunt_log.jsonl and every report_*.json are opened for reading
and never written. This script creates no files.

SCOPE. Finite computation. Hits and misses are reported; nothing is
concluded from either.

WHAT IS SEARCHED. Every finalist record in every report_*.json, plus every
line of hunt_log.jsonl, for games in squares mode -- rules of the form
["ifmod", m, r, ["squares"], F]. Each such game is recomputed locally and
its class-r positions are tested against

    g(n) = 2 + Gamma(floor(t/d) - a),   n = r + t*m, d = squarefree part of m,

with a fitted per copy, exactly as in Task 1. A game is an exact diagonal
game D(m,r) only when F = {m}; anything else is recorded as a near miss and
tested anyway, since the point is to find out what the recorded data does.

Local run:

    $ python3 verification/phase0/task5_log_grep.py

    Phase 0 / Task 5 -- log grep for Grundy retrodictions (logs READ-ONLY)

    hunt_log.jsonl: 5 lines. It records only stamp/seed/best/best_score --
    no Grundy values and no rule JSON, so it carries nothing testable:
        seed 1  best=({3..3} ∪ proper divisors of n)  score=8.14
        seed 2  best=(proper divisors of n ∪ {7})  score=11.14
        seed 3  best=(proper divisors of n + 2)  score=11.26
        seed 4  best=(proper divisors of n + 2)  score=11.26
        seed 5  best=[if n≡1 (mod 2): nonzero base-12 digits of n else: {1,6,9}]  score=11.14

    report_*.json: 5 files, 40 finalist records
    records in squares mode (rule = [ifmod m r [squares] F]): 6
    of those, EXACT diagonal games D(m,r) (F = {m})            : 0

      So the census logs contain no D(m,r) at all. There is no diagonal-game
      Grundy anomaly in these logs to retrodict. That is the finding; the
      near misses below are tested only because they are what is on record.

    NEAR MISSES -- squares mode, fallback not {m}. Tested anyway.
    rule                                       d    checked   mismatches verdict
    --------------------------------------------------------------------------------------------
    ["ifmod", 4, 1, ["squares"], ["const", [3, 1    5000      4646       MISS
          first 10 bad: [1, 5, 9, 13, 17, 21, 25, 29, 33, 37]   fitted a_rho = [5]
    ["ifmod", 5, 1, ["squares"], ["range", 2,  5    4000      2          hit beyond n=7
          bad set (complete): [1, 6]   fitted a_rho = [1, 1, 0, 0, 0]
    ["ifmod", 5, 2, ["squares"], ["range", 2,  5    4000      2          hit beyond n=8
          bad set (complete): [2, 7]   fitted a_rho = [1, 1, 0, 0, 0]
    ["ifmod", 5, 2, ["squares"], ["range", 1,  5    4000      3457       MISS
          first 10 bad: [2, 7, 12, 17, 22, 27, 32, 37, 42, 47]   fitted a_rho = [10, 35, 17, 10, 6]
    ["ifmod", 3, 1, ["squares"], ["range", 3,  3    6667      5133       MISS
          first 10 bad: [1, 7, 19, 22, 25, 46, 49, 52, 64, 67]   fitted a_rho = [0, 0, 0]
    ["ifmod", 5, 1, ["squares"], ["range", 1,  5    4000      3403       MISS
          first 10 bad: [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]   fitted a_rho = [17, -1, 10, 5, 8]

    SUMMARY
      exact diagonal games found in logs      : 0
      near-miss squares-mode games tested     : 6
      near misses matching after a finite bad set (<20 positions): 2
      near misses not matching (>=20 mismatching positions)      : 4

      Reported as found. No conclusion is drawn from either column.
    elapsed: 0.7s
"""
import glob
import json
import sys
import time

DEPTH = 20000
FIT_RANGE = range(-5, 51)


def squarefree_step(m):
    n, m0, p = m, 1, 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            m0 *= p ** ((e + 1) // 2)
        p += 1
    if n > 1:
        m0 *= n
    return m0 * m0 // m


def gamma_sequence(T):
    A = bytearray(T + 1)
    mark = [-1] * 300
    for t in range(1, T + 1):
        k = 1
        while k * k <= t:
            mark[A[t - k * k]] = t
            k += 1
        g = 0
        while mark[g] == t:
            g += 1
        A[t] = g
    return A


def grundy_modeswitch(m, r, fallback, N):
    """Grundy for [ifmod m r squares F]: squares at n = r (mod m), else F."""
    G = bytearray(N + 1)
    mark = [-1] * 300
    sq, k = [], 1
    while k * k <= N:
        sq.append(k * k)
        k += 1
    nsq = 0
    for n in range(1, N + 1):
        while nsq < len(sq) and sq[nsq] <= n:
            nsq += 1
        if n % m == r:
            for i in range(nsq):
                mark[G[n - sq[i]]] = n
        else:
            for s in fallback:
                if s <= n:
                    mark[G[n - s]] = n
        g = 0
        while mark[g] == n:
            g += 1
        G[n] = g
    return G


def expand(node):
    """Expand a fallback DSL node to a finite move list, or None."""
    op = node[0]
    if op == "const":
        return sorted(node[1])
    if op == "range":
        return list(range(node[1], node[2] + 1))
    return None


def test_game(m, r, fb, Gam):
    G = grundy_modeswitch(m, r, fb, DEPTH)
    d = squarefree_step(m)
    rows = {}
    for t in range((DEPTH - r) // m + 1):
        n = r + t * m
        rows.setdefault(t % d, []).append((t // d, n, G[n]))
    bad, offs = [], {}
    for rho in range(d):
        best, bmis = None, None
        for a in FIT_RANGE:
            mis = sum(1 for u, n, g in rows.get(rho, [])
                      if u - a < 0 or u - a >= len(Gam) or g != 2 + Gam[u - a])
            if bmis is None or mis < bmis:
                best, bmis = a, mis
        offs[rho] = best
        for u, n, g in rows.get(rho, []):
            if u - best < 0 or u - best >= len(Gam) or g != 2 + Gam[u - best]:
                bad.append(n)
    return d, offs, sorted(bad), len(rows and [x for v in rows.values() for x in v])


def main():
    t0 = time.time()
    print("Phase 0 / Task 5 -- log grep for Grundy retrodictions (logs READ-ONLY)")
    print()
    hunt = [json.loads(l) for l in open("hunt_log.jsonl") if l.strip()]
    print("hunt_log.jsonl: %d lines. It records only stamp/seed/best/best_score --" % len(hunt))
    print("no Grundy values and no rule JSON, so it carries nothing testable:")
    for h in hunt:
        print("    seed %s  best=%s  score=%s" % (h["seed"], h["best"], h["best_score"]))
    print()
    files = sorted(glob.glob("report_*.json"))
    finalists = []
    for f in files:
        for rec in json.load(open(f))["finalists"]:
            finalists.append((f, rec))
    print("report_*.json: %d files, %d finalist records" % (len(files), len(finalists)))
    sq = [(f, rec) for f, rec in finalists
          if isinstance(rec.get("rule"), list) and rec["rule"][0] == "ifmod"
          and rec["rule"][3] == ["squares"]]
    print("records in squares mode (rule = [ifmod m r [squares] F]): %d" % len(sq))
    exact = [(f, rec) for f, rec in sq if expand(rec["rule"][4]) == [rec["rule"][1]]]
    print("of those, EXACT diagonal games D(m,r) (F = {m})            : %d" % len(exact))
    print()
    if not exact:
        print("  So the census logs contain no D(m,r) at all. There is no diagonal-game")
        print("  Grundy anomaly in these logs to retrodict. That is the finding; the")
        print("  near misses below are tested only because they are what is on record.")
    print()
    umax = DEPTH + 10
    Gam = gamma_sequence(umax)
    print("NEAR MISSES -- squares mode, fallback not {m}. Tested anyway.")
    print("%-42s %-4s %-9s %-10s %s" % ("rule", "d", "checked", "mismatches", "verdict"))
    print("-" * 92)
    hits, misses = 0, 0
    for f, rec in sq:
        rule = rec["rule"]
        m, r = rule[1], rule[2]
        fb = expand(rule[4])
        if fb is None:
            print("%-42s  (fallback not a finite literal set; skipped)" % json.dumps(rule)[:42])
            continue
        d, offs, bad, checked = test_game(m, r, fb, Gam)
        n_class = (DEPTH - r) // m + 1
        verdict = "HIT" if not bad else ("hit beyond n=%d" % (bad[-1] + 1) if len(bad) < 20 else "MISS")
        if not bad or len(bad) < 20:
            hits += 1
        else:
            misses += 1
        print("%-42s %-4d %-9d %-10d %s" % (json.dumps(rule)[:42], d, n_class, len(bad), verdict))
        if bad and len(bad) < 20:
            print("      bad set (complete): %s   fitted a_rho = %s" % (bad, [offs[i] for i in range(d)]))
        elif bad:
            print("      first 10 bad: %s   fitted a_rho = %s" % (bad[:10], [offs[i] for i in range(d)]))
    print()
    print("SUMMARY")
    print("  exact diagonal games found in logs      : %d" % len(exact))
    print("  near-miss squares-mode games tested     : %d" % len(sq))
    print("  near misses matching after a finite bad set (<20 positions): %d" % hits)
    print("  near misses not matching (>=20 mismatching positions)      : %d" % misses)
    print()
    print("  Reported as found. No conclusion is drawn from either column.")
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
