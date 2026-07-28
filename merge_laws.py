#!/usr/bin/env python3
"""Merge the census laws and the rescan laws into one provenance-tagged file.

Sources:
  family_census_raw.json  -- 389 games with a residue law, detector default
                             max_m=40, detected at N=3000, re-checked at N=20000
  rescan_raw.json         -- 6 games the census tiered CHAOTIC that show a law
                             once the modulus cap is raised (N=6000, max_m=200)

Writes laws_merged.json. Every record carries provenance: "census" or "rescan".

Reads only; modifies neither source. No OEIS calls. Conjecture lines are copied
through untouched -- this script never rewords one -- and it proposes nothing.
"""

import json

CENSUS = "family_census_raw.json"
RESCAN = "rescan_raw.json"
OUT = "laws_merged.json"

SQUARES = ["squares"]


def fallback_of(rule):
    """The non-squares branch F of ["ifmod", m, r, A, B]."""
    a, b = rule[3], rule[4]
    return b if a == SQUARES else a


def main():
    census = json.load(open(CENSUS))
    rescan = json.load(open(RESCAN))

    merged = []

    for x in census["records"]:
        if not x["law"]:
            continue
        law = x["law_deep"] or x["law"]
        merged.append({
            "provenance": "census",
            "rule": x["rule"],
            "dsl": json.dumps(x["rule"]),
            "pretty": x["pretty"],
            "m": x["m"], "r": x["r"],
            "branch_order": x["branch_order"],
            "F": x["F"], "F_pretty": x["F_pretty"],
            "game_hash": x["game_hash"],
            "law": law,
            "conjecture": x["conjecture_deep"] or x["conjecture_scan"],
            "detected_at_N": census["n_scan"],
            "confirmed_at_N": census["n_deep"],
            "max_m": 40,
            "census_tier": x["tier"],
            "survived_20000": x["survived_20000"],
        })

    for x in rescan["records"]:
        if not x["law"]:
            continue
        F = fallback_of(x["rule"])
        merged.append({
            "provenance": "rescan",
            "rule": x["rule"],
            "dsl": x["dsl"],
            "pretty": x["pretty"],
            "m": x["m"], "r": x["r"],
            "branch_order": x["branch_order"],
            "F": F, "F_pretty": x["F_pretty"],
            "game_hash": x["census_hash"],
            "law": x["law"],
            "conjecture": x["conjecture"],
            "detected_at_N": x["N_rescan"],
            "confirmed_at_N": None,
            "max_m": x["max_m"],
            "census_tier": x["census_tier"],
            "survived_20000": None,
        })

    merged.sort(key=lambda z: (z["law"]["modulus"], z["m"], z["r"],
                               z["branch_order"], z["F_pretty"]))

    by_prov = {}
    for z in merged:
        by_prov[z["provenance"]] = by_prov.get(z["provenance"], 0) + 1

    # Distinct DSL parameterizations can denote the same underlying game, so
    # game_hash repeats are expected here. game_hash fingerprints G[1:300], so a
    # repeat means the two agree to n=299 -- it is not a claim they agree beyond.
    from collections import Counter
    counts = Counter(z["game_hash"] for z in merged)
    dup_groups = {h: n for h, n in counts.items() if n > 1}
    dup = sum(n - 1 for n in dup_groups.values())
    spanning = 0
    for h in dup_groups:
        if len({z["provenance"] for z in merged if z["game_hash"] == h}) > 1:
            spanning += 1

    with open(OUT, "w") as fh:
        json.dump({
            "sources": {"census": CENSUS, "rescan": RESCAN},
            "total": len(merged),
            "by_provenance": by_prov,
            "repeated_game_hash_groups": len(dup_groups),
            "records_beyond_first_in_a_group": dup,
            "groups_spanning_both_sources": spanning,
            "laws": merged,
        }, fh, indent=1)

    print(f"census laws : {by_prov.get('census', 0)}")
    print(f"rescan laws : {by_prov.get('rescan', 0)}")
    print(f"total       : {len(merged)}")
    print(f"repeated game_hash groups: {len(dup_groups)} "
          f"({dup} records beyond the first in a group)")
    print(f"  groups spanning census+rescan: {spanning}")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
