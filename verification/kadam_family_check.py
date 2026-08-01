#!/usr/bin/env python3
#
# Output of `python3 verification/kadam_family_check.py`, 2026-08-01:
#
#   N = 30000
#
#   GAME 1: square mode at n = 1 (mod 5), else subtract s in {3, 4, 5}
#     claimed law : P iff n mod 25 in [0, 2, 8, 9, 10, 17, 18, 19]
#     exact match : True
#     preperiod   : 0
#     exceptions  : none
#     P-positions counted: 9601
#
#   GAME 2: square mode at n = 1 (mod 8), else subtract s in {3, 6, 7}
#     claimed law : P iff n mod 32 in [0, 2, 4, 12, 13, 14, 22, 23, 24]
#     exact match : True
#     preperiod   : 0
#     exceptions  : none
#     P-positions counted: 8439
#
#   NEGATIVE CONTROL: every single-residue perturbation must be caught
#     GAME 1: 25 single-residue flips tested (mod 25); undetected: none
#              deepest first-violation among the flips: n = 24
#     GAME 2: 32 single-residue flips tested (mod 32); undetected: none
#              deepest first-violation among the flips: n = 31
#
# The two P-position counts are independently reproducible from the laws
# alone: 30001 = 25*1200 + 1, and 1200*8 + 1 = 9601; 30001 = 32*937 + 17,
# and 937*9 + 6 = 8439. Both agree with the recursion's counts.
#
# These are finite checks to N = 30000. They are not proofs, and nothing
# here establishes either law beyond 30000.
#
"""Check two mode-switching observations against their claimed residue laws.

  GAME 1  square mode at n = 1 (mod 5); otherwise subtract s in {3, 4, 5}
          claimed law: P iff n mod 25 in {0, 2, 8, 9, 10, 17, 18, 19}

  GAME 2  square mode at n = 1 (mod 8); otherwise subtract s in {3, 6, 7}
          claimed law: P iff n mod 32 in {0, 2, 4, 12, 13, 14, 22, 23, 24}

Both solved to N = 30000 by an independent win/loss recursion: one P/N bit
per position, early exit on the first winning move, no Grundy values. For
each game the script reports whether the law matches at every n, the
preperiod (the least n0 beyond which the law holds), and every exception.

A negative control perturbs one residue of each law and confirms the checker
reports a violation, so that a clean result is not vacuous.

Self-contained: imports nothing from game_hunter, no network calls. These are
finite checks to N = 30000, not proofs.
"""

import sys

N_DEFAULT = 30000

GAMES = [
    {
        "name": "GAME 1",
        "sq_mod": 5, "sq_res": 1, "fallback": (3, 4, 5),
        "law_mod": 25, "law_res": {0, 2, 8, 9, 10, 17, 18, 19},
    },
    {
        "name": "GAME 2",
        "sq_mod": 8, "sq_res": 1, "fallback": (3, 6, 7),
        "law_mod": 32, "law_res": {0, 2, 4, 12, 13, 14, 22, 23, 24},
    },
]


def solve(sq_mod, sq_res, fallback, N):
    """isP[n] == 1 iff n is a P-position. Win/loss bits only, early exit."""
    isP = bytearray(N + 1)
    isP[0] = 1                      # no legal move from 0: previous player wins
    sq = [k * k for k in range(1, int(N ** 0.5) + 2) if k * k <= N]
    fb = sorted(fallback)
    for n in range(1, N + 1):
        found = 0
        if n % sq_mod == sq_res:
            for s in sq:
                if s > n:
                    break
                if isP[n - s]:
                    found = 1
                    break
        else:
            for s in fb:
                if s > n:
                    break
                if isP[n - s]:
                    found = 1
                    break
        if not found:
            isP[n] = 1
    return isP


def compare(isP, law_mod, law_res, N):
    """Return (exceptions, preperiod). preperiod = last mismatch + 1."""
    exc = [n for n in range(N + 1) if bool(isP[n]) != (n % law_mod in law_res)]
    pre = (exc[-1] + 1) if exc else 0
    return exc, pre


def report(g, N, law_res=None, tag=""):
    res = g["law_res"] if law_res is None else law_res
    isP = solve(g["sq_mod"], g["sq_res"], g["fallback"], N)
    exc, pre = compare(isP, g["law_mod"], res, N)
    print(f"{g['name']}{tag}: square mode at n = {g['sq_res']} (mod {g['sq_mod']}), "
          f"else subtract s in {set(g['fallback'])}")
    print(f"  claimed law : P iff n mod {g['law_mod']} in {sorted(res)}")
    print(f"  exact match : {not exc}")
    print(f"  preperiod   : {pre}")
    if exc:
        print(f"  exceptions  : {len(exc)} total; first 10 = {exc[:10]}")
        n = exc[0]
        print(f"                at n = {n}: computed "
              f"{'P' if isP[n] else 'N'}, law predicts "
              f"{'P' if n % g['law_mod'] in res else 'N'}")
    else:
        print(f"  exceptions  : none")
    print(f"  P-positions counted: {sum(isP)}")
    return isP, exc


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else N_DEFAULT
    print(f"N = {N}")
    print()
    for g in GAMES:
        report(g, N)
        print()

    print("NEGATIVE CONTROL: every single-residue perturbation must be caught")
    for g in GAMES:
        isP = solve(g["sq_mod"], g["sq_res"], g["fallback"], N)
        missed = []
        tested = 0
        for r in range(g["law_mod"]):
            bad = set(g["law_res"])
            bad.discard(r) if r in bad else bad.add(r)   # flip one residue
            exc, _ = compare(isP, g["law_mod"], bad, N)
            tested += 1
            if not exc:
                missed.append(r)
        print(f"  {g['name']}: {tested} single-residue flips tested "
              f"(mod {g['law_mod']}); undetected: {missed if missed else 'none'}")
        # depth probe: the deepest first-violation across those flips
        deepest = max(
            compare(isP, g["law_mod"],
                    (set(g["law_res"]) - {r}) if r in g["law_res"]
                    else (set(g["law_res"]) | {r}), N)[0][0]
            for r in range(g["law_mod"]))
        print(f"           deepest first-violation among the flips: n = {deepest}")


if __name__ == "__main__":
    main()
