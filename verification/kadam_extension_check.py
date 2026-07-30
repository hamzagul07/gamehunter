#!/usr/bin/env python3
#
# Output of `python3 verification/kadam_extension_check.py`, 2026-07-30:
#
#   N = 30000
#   law: n is P iff n mod 16 in [0, 2, 4, 6]
#   extended standard set: s <= n with s mod 16 in [3, 8, 9]  (5625 values <= 30000)
#
#   original matches law : True   first difference: none
#   extended matches law : True   first difference: none
#   original == extended : True   first difference: none
#
#   P-positions counted  : original 7501, extended 7501
#
# Negative controls run alongside (not part of this script's output), to
# establish that the three Trues above are not vacuous:
#   - replacing the residue set {3,8,9} with {3,8,10} makes the checker
#     report "matches law = False", first difference at n = 11;
#   - 1491 standard-mode positions below 3000 have an extended-only move
#     landing on a P-position, so the added moves are genuinely live rather
#     than inert.
#
# This is a finite check to N = 30000. It is not a proof.
#
"""Kadam extension check for the Foursquare subtraction game.

Two games are solved to N = 30000 by an independent win/loss recursion:

  ORIGINAL  square mode  (n = 1 mod 4): subtract any square k^2 <= n
            standard mode              : subtract s in {3, 8, 9}, s <= n

  EXTENDED  square mode  (n = 1 mod 4): subtract any square k^2 <= n
            standard mode              : subtract any s <= n with
                                         s mod 16 in {3, 8, 9}

Both P-sets are compared against the law  n mod 16 in {0, 2, 4, 6}  and
against each other. Three booleans and the first differing position in each
comparison are printed.

Self-contained: imports nothing from game_hunter, computes win/loss bits only
(no Grundy values), and makes no network calls. Numbers below are a finite
check to N = 30000, not a proof.
"""

import sys

N_DEFAULT = 30000
LAW_RESIDUES = {0, 2, 4, 6}
BASE_SET = (3, 8, 9)
MOD = 16


def standard_moves(N, extended):
    """Ascending list of legal standard-mode subtraction amounts up to N."""
    if not extended:
        return list(BASE_SET)
    return [s for s in range(1, N + 1) if s % MOD in BASE_SET]


def solve(N, extended):
    """isP[n] == 1 iff n is a P-position. Win/loss only, early exit."""
    subs = standard_moves(N, extended)
    isP = bytearray(N + 1)
    isP[0] = 1                       # no legal move from 0: previous player wins
    for n in range(1, N + 1):
        found = 0
        if n % 4 == 1:               # square mode
            k = 1
            while k * k <= n:
                if isP[n - k * k]:
                    found = 1
                    break
                k += 1
        else:                        # standard mode
            for s in subs:
                if s > n:
                    break
                if isP[n - s]:
                    found = 1
                    break
        if not found:
            isP[n] = 1
    return isP


def first_diff_from_law(isP, N):
    for n in range(N + 1):
        if bool(isP[n]) != (n % MOD in LAW_RESIDUES):
            return n
    return None


def first_diff_between(a, b, N):
    for n in range(N + 1):
        if a[n] != b[n]:
            return n
    return None


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else N_DEFAULT

    original = solve(N, extended=False)
    extended = solve(N, extended=True)

    d_orig = first_diff_from_law(original, N)
    d_ext = first_diff_from_law(extended, N)
    d_both = first_diff_between(original, extended, N)

    print(f"N = {N}")
    print(f"law: n is P iff n mod {MOD} in {sorted(LAW_RESIDUES)}")
    print(f"extended standard set: s <= n with s mod {MOD} in {sorted(BASE_SET)}"
          f"  ({len(standard_moves(N, True))} values <= {N})")
    print()
    print(f"original matches law : {d_orig is None}"
          f"   first difference: {d_orig if d_orig is not None else 'none'}")
    print(f"extended matches law : {d_ext is None}"
          f"   first difference: {d_ext if d_ext is not None else 'none'}")
    print(f"original == extended : {d_both is None}"
          f"   first difference: {d_both if d_both is not None else 'none'}")
    print()
    print(f"P-positions counted  : original {sum(original)}, extended {sum(extended)}")


if __name__ == "__main__":
    main()
