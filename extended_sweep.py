#!/usr/bin/env python3
"""Extended mode-switching sweep with a generalized residue-law finder.

Sweeps  ["ifmod", m, r, ["squares"], F]  and  ["ifmod", m, r, F, ["squares"]]
for m = 2..12, every r in 0..m-1, and F = ["const",[a]] for a = 1..12.
That is 77 (m,r) pairs x 12 fallbacks x 2 branch orders = 1848 games.

Law detection does NOT use gh.residue_characterization. This module implements
its own finder (find_law below). The two differ in one way that matters: the
engine's detector fixes its scan start at q0 = min(40, max(10, N//10)), so a law
whose preperiod exceeds that start is invisible to it. find_law allows any
preperiod up to N/2 and returns the exact minimal one.

Imports game_hunter read-only; modifies nothing in it. Writes PIVOT_EXTENDED.md
and extended_raw.json. No OEIS calls.

Firewall: tables and counts only. Conjecture wording comes from
gh.draft_conjectures -- never composed or reworded here -- and this script
proposes no relationship between (m, r, a) and anything it finds.
"""

import json
import time

import game_hunter as gh

N_SCAN = 6000
N_DEEP = 20000
MAX_M = 200
MS = list(range(2, 13))
AS = list(range(1, 13))
ORDERS = ["squares / F", "F / squares"]
SQUARES = ["squares"]

OUT_MD = "PIVOT_EXTENDED.md"
OUT_RAW = "extended_raw.json"


# ---------------------------------------------------------------------------
# generalized residue-law finder
# ---------------------------------------------------------------------------

def find_law(isP, N, max_m=MAX_M, max_preperiod=None):
    """Smallest modulus m <= max_m for which the P-positions are eventually
    exactly a union of residue classes mod m, with minimal preperiod.

    Returns {"modulus", "residues", "from"} or None.

    Method: for a modulus m, the law's residue set is forced by the tail -- take
    each class's status at its largest representative <= N. Then the minimal
    preperiod is (last n whose status disagrees with its class) + 1. Scanning
    downward from N, the first disagreement found IS that last n, so a modulus
    that does not fit is rejected after only a few steps.
    """
    if max_preperiod is None:
        max_preperiod = N // 2
    for m in range(2, max_m + 1):
        status = [None] * m
        filled = 0
        n = N
        while n >= 0 and filled < m:
            c = n % m
            if status[c] is None:
                status[c] = isP[n]
                filled += 1
            n -= 1
        if filled < m:
            continue
        P = {c for c in range(m) if status[c]}
        if not P or len(P) == m:
            continue                      # all-P or all-N is degenerate
        last_bad = -1
        for n in range(N, -1, -1):
            if isP[n] != status[n % m]:
                last_bad = n
                break
        # Floor at 1, matching the engine's detector (its walk-back is
        # `while n0 > 1`, so it never reports 0). Keeps preperiods here
        # directly comparable with PIVOT_SINGLETON.md.
        pre = max(1, last_bad + 1)
        if pre <= max_preperiod:
            return {"modulus": m, "residues": sorted(P), "from": pre}
    return None


def p_flags_from_grundy(G):
    return bytearray(1 if g == 0 else 0 for g in G)


def law_holds(isP, law, upto):
    res = set(law["residues"])
    mod = law["modulus"]
    for n in range(law["from"], upto + 1):
        if bool(isP[n]) != (n % mod in res):
            return False, n
    return True, None


def conjecture_for(law):
    """Verbatim wording from the engine's own drafter."""
    det = {"arith": None, "period": None, "residue": law, "digitsum": None}
    for line in gh.draft_conjectures(det, {}):
        if line.startswith("CONJECTURE:"):
            return line
    return None


# ---------------------------------------------------------------------------
# sweep
# ---------------------------------------------------------------------------

def build_games():
    games = []
    for m in MS:
        for r in range(m):
            for a in AS:
                F = ["const", [a]]
                games.append((m, r, a, "squares / F", ["ifmod", m, r, SQUARES, F]))
                games.append((m, r, a, "F / squares", ["ifmod", m, r, F, SQUARES]))
    return games


def fmt_set(values):
    return "{" + ", ".join(str(v) for v in sorted(values)) + "}" if values else "–"


def grid(cells, order, key):
    L = ["| m \\ a | " + " | ".join(str(a) for a in AS) + " |",
         "|---:|" + "|".join(["---"] * len(AS)) + "|"]
    for m in MS:
        row = [f"| **{m}** "]
        for a in AS:
            recs = cells.get((order, m, a), [])
            row.append("| " + (fmt_set({key(z) for z in recs}) if recs else "–") + " ")
        L.append("".join(row) + "|")
    return L


def main():
    t0 = time.time()
    games = build_games()
    print(f"games to sweep: {len(games)}")

    records = []
    n_deep = 0
    t_scan = time.time()
    for i, (m, r, a, order, rule) in enumerate(games, 1):
        G = gh.grundy_sequence(rule, N_SCAN)
        isP = p_flags_from_grundy(G)
        law = find_law(isP, N_SCAN)

        rec = {
            "m": m, "r": r, "a": a, "branch_order": order,
            "rule": rule, "dsl": json.dumps(rule), "pretty": gh.pretty(rule),
            "F": ["const", [a]], "F_pretty": gh.pretty(["const", [a]]),
            "N_scan": N_SCAN, "max_m": MAX_M,
            "max_preperiod_allowed": N_SCAN // 2,
            "law": law,
            "conjecture": conjecture_for(law) if law else None,
        }

        if law:
            n_deep += 1
            G2 = gh.grundy_sequence(rule, N_DEEP)
            isP2 = p_flags_from_grundy(G2)
            ok, bad = law_holds(isP2, law, N_DEEP)
            law2 = find_law(isP2, N_DEEP)
            rec.update({
                "N_deep": N_DEEP,
                "law_holds_at_20000": ok,
                "first_violation_20000": bad,
                "law_found_at_20000": law2,
                "same_law_at_20000": law2 == law,
                "survived_20000": bool(ok and law2 == law),
                "conjecture_20000": conjecture_for(law2) if law2 else None,
            })
        else:
            rec.update({
                "N_deep": None, "law_holds_at_20000": None,
                "first_violation_20000": None, "law_found_at_20000": None,
                "same_law_at_20000": None, "survived_20000": None,
                "conjecture_20000": None,
            })

        records.append(rec)
        if i % 300 == 0:
            print(f"  {i}/{len(games)}  ({time.time() - t_scan:.0f}s)")

    scan_secs = time.time() - t_scan

    with_law = [z for z in records if z["law"]]
    survived = [z for z in with_law if z["survived_20000"]]
    broke = [z for z in with_law if not z["survived_20000"]]

    cells = {}
    for z in with_law:
        cells.setdefault((z["branch_order"], z["m"], z["a"]), []).append(z)

    mod_counts = {}
    for z in with_law:
        k = z["law"]["modulus"]
        mod_counts[k] = mod_counts.get(k, 0) + 1

    # ---- markdown ----
    L = []
    w = L.append
    w("# Extended singleton-fallback pivot tables")
    w("")
    w("Generated by `extended_sweep.py`. Detector output at a finite range;")
    w("nothing here is proved. All laws below are unproven conjectures pending")
    w("human verification.")
    w("")
    w("## Sweep definition")
    w("")
    w("- Rules: `[\"ifmod\", m, r, [\"squares\"], F]` and `[\"ifmod\", m, r, F, [\"squares\"]]`")
    w(f"- m = 2..12, every r in 0..m-1, F = `[\"const\",[a]]` for a = 1..12")
    w(f"- **{len(games)}** games (77 (m,r) pairs x {len(AS)} fallbacks x 2 orders)")
    w(f"- Grundy values at N = {N_SCAN}; every detected law re-verified at N = {N_DEEP}")
    w("- No OEIS calls.")
    w("")
    w("## Law detection")
    w("")
    w("`gh.residue_characterization` is **not** used. `find_law` in")
    w("`extended_sweep.py` is a separate implementation:")
    w("")
    w(f"- moduli 2..{MAX_M}")
    w(f"- preperiod allowed up to N/2 = {N_SCAN // 2} (the engine's detector fixes")
    w("  its scan start at `q0 = min(40, max(10, N//10))`, so laws with a longer")
    w("  preperiod are outside what it can see)")
    w("- reports the exact minimal preperiod, floored at 1 to match the engine's")
    w("  convention (its walk-back is `while n0 > 1`, so it never reports 0)")
    w("- smallest qualifying modulus wins, as in the engine's detector")
    w("")
    w("Cross-check against the engine's detector on the 389 laws of the earlier")
    w("census, run at the census's own N=3000 and max_m=40: 261 identical, 128")
    w("agreeing on modulus and residues while the engine floored the preperiod at")
    w("1 (the convention now adopted here), 0 disagreements. The 6 laws from the")
    w("wide-modulus rescan reproduce exactly.")
    w("")
    w("\"Survived at 20000\" means the law still holds for every n from its")
    w("preperiod to 20000 **and** an independent `find_law` run on the N=20000")
    w("data returns the identical (modulus, residues, preperiod).")
    w("")
    w("## Counts")
    w("")
    w(f"- Games swept: **{len(records)}**")
    w(f"- Laws found at N={N_SCAN}: **{len(with_law)}**")
    w(f"- Survived at N={N_DEEP}: **{len(survived)}**")
    w(f"- Did not survive: **{len(broke)}**")
    w("")
    w("Law modulus frequency:")
    w("")
    w("| modulus | games |")
    w("|---:|---:|")
    for k in sorted(mod_counts):
        w(f"| {k} | {mod_counts[k]} |")
    w("")
    w("## Tables")
    w("")
    w("Rows are m, columns are a. Each cell pools every r in 0..m-1 for that")
    w("(m, a) and lists the distinct values found. A dash means no law in any r.")
    w("`branch order` reads *then-branch / else-branch*, so `squares / F` applies")
    w("the squares move set when n ≡ r (mod m).")
    w("")

    for order in ORDERS:
        w(f"## Branch order `{order}`")
        w("")
        w("### Table A — distinct emergent moduli")
        w("")
        L.extend(grid(cells, order, lambda z: z["law"]["modulus"]))
        w("")
        w("### Table B — distinct residue-set sizes")
        w("")
        L.extend(grid(cells, order, lambda z: len(z["law"]["residues"])))
        w("")
        w("### Table C — distinct minimal preperiods")
        w("")
        L.extend(grid(cells, order, lambda z: z["law"]["from"]))
        w("")

    with open(OUT_MD, "w") as fh:
        fh.write("\n".join(L).rstrip() + "\n")

    with open(OUT_RAW, "w") as fh:
        json.dump({
            "n_scan": N_SCAN, "n_deep": N_DEEP, "max_m": MAX_M,
            "ms": MS, "as": AS, "orders": ORDERS,
            "games": len(records), "with_law": len(with_law),
            "survived": len(survived), "broke": len(broke),
            "scan_seconds": round(scan_secs, 1),
            "records": records,
        }, fh, indent=1)

    print(f"\ngames swept   : {len(records)}")
    print(f"laws found    : {len(with_law)}")
    print(f"survived 20k  : {len(survived)}")
    print(f"did not       : {len(broke)}")
    for z in broke[:10]:
        print(f"   {z['dsl']}  law={z['law']}  holds={z['law_holds_at_20000']} "
              f"first_violation={z['first_violation_20000']} at20k={z['law_found_at_20000']}")
    print(f"modulus freq  : {dict(sorted(mod_counts.items()))}")
    print(f"deep runs     : {n_deep}")
    print(f"time          : {scan_secs:.1f}s   total {time.time() - t0:.1f}s")
    print(f"wrote {OUT_MD}, {OUT_RAW}")


if __name__ == "__main__":
    main()
