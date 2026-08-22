#!/usr/bin/env python3
"""Corollary 8.3 collapse sweep -- r enters the class-index Grundy sequence
only through beta.

PROVENANCE. Written and executed locally in this repository; the JSON
beside it, verification/cor83_collapse_raw.json, is this script's own
output and a re-run reproduces it.

SCOPE. A finite computation over a stated range. Agreement means agreement
on the class indices swept and nothing more; this is not a proof.

PINNED SPECIFICATION (the paper sentence is written against exactly this):
  * moduli m in {3, 5, 6, 7, 9, 10, 11, 12} -- eight moduli;
  * at each m, every healthy r >= 1 (at m = 9 that is r in {1,2,3,7,8}),
    class-index Grundy sequence of D(m,r) for t = 0..5000, asserted
    identical across those r;
  * additionally at m = 9, the three exceptional games r in {4,5,6} to the
    same depth, asserted identical to one another.
Any failed assertion aborts the run with a nonzero exit status.

The Grundy engine is the repository's own: game_hunter.grundy_sequence,
driven by the DSL rule ["ifmod", m, r, ["squares"], ["const", [m]]].
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import game_hunter as gh                                    # noqa: E402

MODULI = [3, 5, 6, 7, 9, 10, 11, 12]
EXCEPTIONAL_R = {4, 5, 6}          # only at m = 9
TMAX = 5000
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "cor83_collapse_raw.json")


def class_index_grundy(m, r, tmax):
    """[G(r + t*m) : t = 0..tmax] using the repository's Grundy engine."""
    rule = ["ifmod", m, r, ["squares"], ["const", [m]]]
    N = r + tmax * m
    G = gh.grundy_sequence(rule, N)
    return [G[r + t * m] for t in range(tmax + 1)]


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return None


def main():
    t0 = time.time()
    results, failures = [], []
    print("Corollary 8.3 collapse sweep -- t = 0..%d, engine = game_hunter" % TMAX)
    print("=" * 72)
    for m in MODULI:
        healthy = [r for r in range(1, m) if not (m == 9 and r in EXCEPTIONAL_R)]
        seqs = {r: class_index_grundy(m, r, TMAX) for r in healthy}
        ref = healthy[0]
        bad = []
        for r in healthy[1:]:
            d = first_diff(seqs[ref], seqs[r])
            if d is not None:
                bad.append({"r_pair": [ref, r], "first_disagreement_index": d,
                            "values": [seqs[ref][d], seqs[r][d]]})
        entry = {"m": m, "healthy_r": healthy, "games": len(healthy),
                 "depth_t": TMAX, "pass": not bad}
        if bad:
            entry["failures"] = bad
            failures.append(entry)
        results.append(entry)
        print("  m=%-3d healthy r=%-18s games=%-3d depth=%-6d %s"
              % (m, str(healthy), len(healthy), TMAX, "PASS" if not bad else "FAIL"))

    # the three exceptional games at m = 9
    exc = sorted(EXCEPTIONAL_R)
    eseqs = {r: class_index_grundy(9, r, TMAX) for r in exc}
    ebad = []
    for r in exc[1:]:
        d = first_diff(eseqs[exc[0]], eseqs[r])
        if d is not None:
            ebad.append({"r_pair": [exc[0], r], "first_disagreement_index": d,
                         "values": [eseqs[exc[0]][d], eseqs[r][d]]})
    eentry = {"m": 9, "exceptional_r": exc, "games": len(exc),
              "depth_t": TMAX, "pass": not ebad}
    if ebad:
        eentry["failures"] = ebad
        failures.append(eentry)
    print("  m=9   exceptional r=%-15s games=%-3d depth=%-6d %s"
          % (str(exc), len(exc), TMAX, "PASS" if not ebad else "FAIL"))

    payload = {
        "spec": {"moduli": MODULI, "depth_t": TMAX,
                 "exceptional_r_at_9": exc,
                 "engine": "game_hunter.grundy_sequence",
                 "rule": '["ifmod", m, r, ["squares"], ["const", [m]]]'},
        "healthy": results,
        "exceptional_trio": eentry,
        "all_pass": not failures,
        "note": ("Finite check over the stated class-index range; "
                 "not a proof."),
    }
    with open(OUT, "w") as fh:
        json.dump(payload, fh, indent=2)
        fh.write("\n")
    print("=" * 72)
    print("moduli swept        : %d" % len(MODULI))
    print("healthy games swept : %d" % sum(e["games"] for e in results))
    print("exceptional games   : %d" % eentry["games"])
    print("ALL PASS            : %s" % (not failures))
    print("raw output          : %s" % os.path.relpath(OUT))
    print("elapsed             : %.1fs" % (time.time() - t0))
    if failures:
        print("\nFAILURES:")
        print(json.dumps(failures, indent=2))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
