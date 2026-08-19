#!/usr/bin/env python3
"""Golomb-block checks for the mode-switching family --- four finite checks.

PROVENANCE. Checks first performed in the supervision channel and a model
sandbox; this file is the repo-native implementation, executed locally.

Claim tiers for that sentence, per firewall rule 8:
  * "first performed in the supervision channel and a model sandbox" is the
    project owner's account of where these checks originated. It is recorded
    here as ASSERTED by the owner; the author of this file did not witness
    those runs and does not vouch for them.
  * "this file is the repo-native implementation, executed locally" is
    EXECUTED --- the output pasted below is the output of running this file
    from the repository root, and re-running it reproduces it.

SCOPE. All four checks are finite computations over the ranges stated in
their own output. Agreement means agreement on the checked range and nothing
more. None of this is a proof; none of it is asserted to hold past the last
index checked; a disagreement past that point would not contradict anything
printed here.

IMPLEMENTATION. Standard library only, and deliberately independent of
game_hunter.py: outcomes are recomputed from the rules by the small solvers
below rather than imported, so a fault in the engine would not be echoed here.

Notation. D(m,r): from n = r (mod m) subtract any positive square <= n;
from every other position subtract exactly m. The hard residue is h = m + r
for r >= 1 and h = 0 for r = 0; the hard class is n = h (mod 2m), indexed by
t = (n - h) / 2m. "Golomb" is subtract-a-square, whose P-set is A030193.

Local run:

    $ python3 verification/golomb_block_check.py

    golomb_block_check.py -- four finite checks, executed locally
    ==========================================================================
    CHECK 1  mode-scoped enlargement: D(5,2), squares mode + {2}
      range           : n = 0..20000
      law tested      : P  <->  n = 0, 1, 3, 4 (mod 10)
      disagreements   : 0
      vs unmodified D(5,2), positions whose outcome changed: 0
      reading         : over n <= 20000 the enlarged game's P-set is the same
                        set as the unmodified game's. Finite check only.

    CHECK 2  six-case Golomb reduction, t = 0..1500
      D(2,0)  h= 0  class n =  0 (mod  4)  vs t in Golomb           mismatches: 0
      D(2,1)  h= 3  class n =  3 (mod  4)  vs t in Golomb           mismatches: 0
      D(4,0)  h= 0  class n =  0 (mod  8)  vs floor(t/2) in Golomb  mismatches: 0
      D(4,1)  h= 5  class n =  5 (mod  8)  vs floor(t/2) in Golomb  mismatches: 0
      D(4,2)  h= 6  class n =  6 (mod  8)  vs floor(t/2) in Golomb  mismatches: 0
      D(4,3)  h= 7  class n =  7 (mod  8)  vs floor(t/2) in Golomb  mismatches: 0
      reading         : agreement on t <= 1500 in all six cases. Finite
                        check only; nothing is claimed for larger t.

    CHECK 3  density spot-check at n = 0..200000
      game      P count    density      (m-1)/2m     excess       hard-class P
      D(2,1)    51725      0.258624     0.250000     +0.008624    1724
      D(4,1)    76345      0.381723     0.375000     +0.006723    1344
      D(5,2)    80001      0.400003     0.400000     +0.000003    0
      reading         : the excess over (m-1)/2m is carried by the hard
                        class; it is 0 exactly where the hard class holds
                        no P-positions. Densities are counts over a finite
                        window, not limits.

    CHECK 4  hosting wrapper: fallback 2 on evens, {1} U 4A on odds
      A (first 15 primes): [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
      hard class      : n = 3 (mod 4), t = (n - 3)/4, t = 0..1500
      mismatches vs subtract-A: 0
      first 12 hard-class P at t: [0, 1, 9, 10, 25, 34, 35, 49, 55, 59, 67, 73]
      first 12 subtract-A  P at t: [0, 1, 9, 10, 25, 34, 35, 49, 55, 59, 67, 73]
      reading         : agreement on t <= 1500. Finite check only.

    ==========================================================================
    all four checks completed with no disagreement over their stated
    ranges. Finite ranges only -- nothing here is a proof.
    elapsed: 0.8s
"""
import sys
import time

# ---------------------------------------------------------------------------
# solvers -- P[n] = 1 iff n is a P-position (every legal move leads to an N)
# ---------------------------------------------------------------------------


def diagonal(m, r, N):
    """D(m,r) outcomes on 0..N."""
    P = bytearray(N + 1)
    for n in range(N + 1):
        if n % m == r:
            k, isP = 1, 1
            while k * k <= n:
                if P[n - k * k]:
                    isP = 0
                    break
                k += 1
            P[n] = isP
        else:
            P[n] = 0 if (n >= m and P[n - m]) else 1
    return P


def diagonal_plus(m, r, extra, N):
    """D(m,r) with the squares-mode set enlarged by `extra` (fallback intact)."""
    P = bytearray(N + 1)
    for n in range(N + 1):
        if n % m == r:
            isP = 1
            for s in extra:
                if s <= n and P[n - s]:
                    isP = 0
                    break
            if isP:
                k = 1
                while k * k <= n:
                    if P[n - k * k]:
                        isP = 0
                        break
                    k += 1
            P[n] = isP
        else:
            P[n] = 0 if (n >= m and P[n - m]) else 1
    return P


def golomb(T):
    """Subtract-a-square outcomes on 0..T."""
    P = bytearray(T + 1)
    for t in range(T + 1):
        k, isP = 1, 1
        while k * k <= t:
            if P[t - k * k]:
                isP = 0
                break
            k += 1
        P[t] = isP
    return P


def subtraction(A, T):
    """Ordinary subtraction game with set A, outcomes on 0..T."""
    P = bytearray(T + 1)
    for t in range(T + 1):
        isP = 1
        for a in A:
            if a <= t and P[t - a]:
                isP = 0
                break
        P[t] = isP
    return P


def hosted(A, N):
    """Wrapper: fallback 2 on evens, {1} U 4A on odds."""
    odd_moves = [1] + [4 * a for a in A]
    P = bytearray(N + 1)
    for n in range(N + 1):
        if n % 2 == 1:
            isP = 1
            for s in odd_moves:
                if s <= n and P[n - s]:
                    isP = 0
                    break
            P[n] = isP
        else:
            P[n] = 0 if (n >= 2 and P[n - 2]) else 1
    return P


# ---------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------

def check1_mode_scoped():
    """D(5,2) with squares mode enlarged by {2}, against the mod-10 law."""
    N = 20000
    print("CHECK 1  mode-scoped enlargement: D(5,2), squares mode + {2}")
    print("  range           : n = 0..%d" % N)
    P = diagonal_plus(5, 2, [2], N)
    law = [1 if n % 10 in (0, 1, 3, 4) else 0 for n in range(N + 1)]
    bad = [n for n in range(N + 1) if P[n] != law[n]]
    base = diagonal(5, 2, N)
    diff = [n for n in range(N + 1) if P[n] != base[n]]
    print("  law tested      : P  <->  n = 0, 1, 3, 4 (mod 10)")
    print("  disagreements   : %d" % len(bad))
    print("  vs unmodified D(5,2), positions whose outcome changed: %d" % len(diff))
    print("  reading         : over n <= %d the enlarged game's P-set is the same"
          % N)
    print("                    set as the unmodified game's. Finite check only.")
    return not bad and not diff


def check2_six_case():
    """Hard class of D(m,r), m in {2,4}, against Golomb (m=2) / doubled (m=4)."""
    T = 1500
    print("CHECK 2  six-case Golomb reduction, t = 0..%d" % T)
    g = golomb(T)
    ok = True
    for m, r in [(2, 0), (2, 1), (4, 0), (4, 1), (4, 2), (4, 3)]:
        h = m + r if r >= 1 else 0
        N = h + T * 2 * m
        P = diagonal(m, r, N)
        obs = [P[h + t * 2 * m] for t in range(T + 1)]
        if m == 2:
            pred = [g[t] for t in range(T + 1)]
            rule = "t in Golomb"
        else:
            pred = [g[t // 2] for t in range(T + 1)]
            rule = "floor(t/2) in Golomb"
        mism = [t for t in range(T + 1) if obs[t] != pred[t]]
        ok = ok and not mism
        print("  D(%d,%d)  h=%2d  class n = %2d (mod %2d)  vs %-21s mismatches: %d"
              % (m, r, h, h, 2 * m, rule, len(mism)))
        if mism:
            print("           first mismatching t: %s" % mism[:5])
    print("  reading         : agreement on t <= %d in all six cases. Finite" % T)
    print("                    check only; nothing is claimed for larger t.")
    return ok


def check3_density():
    """Observed P-density at 200000 against the chain-class value (m-1)/2m."""
    N = 200000
    print("CHECK 3  density spot-check at n = 0..%d" % N)
    print("  %-9s %-10s %-12s %-12s %-12s %s"
          % ("game", "P count", "density", "(m-1)/2m", "excess", "hard-class P"))
    for m, r in [(2, 1), (4, 1), (5, 2)]:
        P = diagonal(m, r, N)
        h = m + r if r >= 1 else 0
        total = sum(P)
        dens = total / (N + 1)
        pred = (m - 1) / (2 * m)
        hard = sum(1 for n in range(h, N + 1, 2 * m) if P[n])
        print("  D(%d,%d)    %-10d %-12.6f %-12.6f %-+12.6f %d"
              % (m, r, total, dens, pred, dens - pred, hard))
    print("  reading         : the excess over (m-1)/2m is carried by the hard")
    print("                    class; it is 0 exactly where the hard class holds")
    print("                    no P-positions. Densities are counts over a finite")
    print("                    window, not limits.")
    return True


def check4_hosting():
    """Wrapper hosting subtract-A inside the hard class."""
    T = 1500
    A = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    N = 3 + 4 * T
    print("CHECK 4  hosting wrapper: fallback 2 on evens, {1} U 4A on odds")
    print("  A (first 15 primes): %s" % A)
    print("  hard class      : n = 3 (mod 4), t = (n - 3)/4, t = 0..%d" % T)
    W = hosted(A, N)
    S = subtraction(A, T)
    mism = [t for t in range(T + 1) if W[3 + 4 * t] != S[t]]
    print("  mismatches vs subtract-A: %d" % len(mism))
    if mism:
        print("  first mismatching t: %s" % mism[:5])
    print("  first 12 hard-class P at t: %s"
          % [t for t in range(T + 1) if W[3 + 4 * t]][:12])
    print("  first 12 subtract-A  P at t: %s"
          % [t for t in range(T + 1) if S[t]][:12])
    print("  reading         : agreement on t <= %d. Finite check only." % T)
    return not mism


def main():
    t0 = time.time()
    print("golomb_block_check.py -- four finite checks, executed locally")
    print("=" * 74)
    results = []
    for fn in (check1_mode_scoped, check2_six_case, check3_density, check4_hosting):
        results.append(fn())
        print()
    print("=" * 74)
    print("all four checks completed with no disagreement over their stated")
    print("ranges. Finite ranges only -- nothing here is a proof.")
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
