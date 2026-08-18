#!/usr/bin/env python3
"""Regression: the OEIS filter must recognize Golomb-reindexed classics.

Both games below have P-sets that miss OEIS outright but are subtract-a-square's
losing positions (A030193) once read on the right sublattice. Before the affine
reindexing pass they were scored as novelty candidates.

Run offline against oeis_cache.json:  python3 test_filter_affine_reindex.py

Actual output of this file at the commit that introduced it:

    (a) D(2,1) -- confined class n = 3 (mod 4)
        raw P-set lookup      : not_found
        affine match          : A030193 at d=4, h=3
        A030193 name          : Let S = squares; a(0)=0; a(n) = smallest m such that m - a(i) is not in S for any i < n.
        reindexed head        : [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 34, 39]
        novelty_verdict       : known
        PASS
    (b) D(4,1) -- confined class n = 5 (mod 8), split by the doubled step
        raw P-set lookup      : not_found
        step-16 sublattices matching: h=5 -> A030193, h=13 -> A030193
        h=5  reindexed head   : [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 34, 39]
        h=13 reindexed head   : [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 34, 39]
        step-8 sublattice h=5 : not_found  (does not match; the doubling is load-bearing)
        novelty_verdict       : known
        PASS

    all tests passed
"""
import sys

import game_hunter as gh

N = 4000
CACHE = "oeis_cache.json"
D21 = ["ifmod", 2, 1, ["squares"], ["const", [2]]]
D41 = ["ifmod", 4, 1, ["squares"], ["const", [4]]]


def analyze(rule):
    cache = gh.load_cache(CACHE)
    return gh.analyze_rule(rule, N, cache, offline=True, deep=True)


def sublattice(rule, d, h):
    G = gh.grundy_sequence(rule, N)
    return [(n - h) // d for n in range(1, N + 1) if G[n] == 0 and n % d == h]


def test_d21_hard_class():
    print("    (a) D(2,1) -- confined class n = 3 (mod 4)")
    rec = analyze(D21)
    aff = rec["oeis_p_affine"]
    print("        raw P-set lookup      : %s" % rec["oeis_p_positions"]["status"])
    assert rec["oeis_p_positions"]["status"] == "not_found"
    print("        affine match          : %s at d=%d, h=%d" % (aff["A"], aff["d"], aff["h"]))
    assert aff["status"] == "found"
    assert aff["A"] == "A030193"
    assert (aff["d"], aff["h"]) == (4, 3)
    print("        A030193 name          : %s" % aff["name"])
    print("        reindexed head        : %s" % sublattice(D21, 4, 3)[:12])
    print("        novelty_verdict       : %s" % rec["novelty_verdict"])
    assert rec["novelty_verdict"] == "known"
    print("        PASS")


def test_d41_both_sublattices():
    print("    (b) D(4,1) -- confined class n = 5 (mod 8), split by the doubled step")
    rec = analyze(D41)
    aff = rec["oeis_p_affine"]
    print("        raw P-set lookup      : %s" % rec["oeis_p_positions"]["status"])
    assert rec["oeis_p_positions"]["status"] == "not_found"
    hits = {m["h"]: m["A"] for m in aff["matches"] if m["d"] == 16}
    print("        step-16 sublattices matching: %s"
          % ", ".join("h=%d -> %s" % (h, hits[h]) for h in sorted(hits)))
    assert hits == {5: "A030193", 13: "A030193"}, hits
    print("        h=5  reindexed head   : %s" % sublattice(D41, 16, 5)[:12])
    print("        h=13 reindexed head   : %s" % sublattice(D41, 16, 13)[:12])
    step8 = [t for t in aff["tried"] if (t["d"], t["h"]) == (8, 5)]
    assert step8 and step8[0]["status"] != "found", step8
    print("        step-8 sublattice h=5 : %s  (does not match; the doubling is "
          "load-bearing)" % step8[0]["status"])
    print("        novelty_verdict       : %s" % rec["novelty_verdict"])
    assert rec["novelty_verdict"] == "known"
    print("        PASS")


if __name__ == "__main__":
    try:
        test_d21_hard_class()
        test_d41_both_sublattices()
    except AssertionError as e:
        print("FAIL: %s" % e)
        sys.exit(1)
    print("\n    all tests passed")
