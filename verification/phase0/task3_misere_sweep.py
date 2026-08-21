#!/usr/bin/env python3
"""Phase 0, Task 3 -- misere outcome sweep.

PROVENANCE. Written and executed locally in this repository; the output
pasted below is this file's own output and a re-run reproduces it.

SCOPE. Finite computation to n = 50000. Nothing here is a proof and
nothing is claimed past that depth. "Agrees" means "no disagreement was
found below the depth swept".

CONVENTION. Misere play: the player who cannot move WINS, so a terminal
position is an N-position. A position is misere-P iff it has at least one
option and every option is misere-N.

PREDICTION UNDER TEST
    misere-P = { n = c + m (mod 2m) : c a foreign bottom }   [top rungs]
               union { smallest free member }
with the rebels dissolving -- in particular 13 should be misere-N in
D(9,4). Foreign bottoms are the residues c in {0,...,m-1} with c != r; the
smallest free member is r when r >= 1 and m when r = 0.

Local run:

    $ python3 verification/phase0/task3_misere_sweep.py

    Phase 0 / Task 3 -- misere outcome sweep, depth n = 0..50000
    games: 68 healthy + 3 exceptional = 71

    EXACT AGREEMENT to depth 50000: 68 of 71 games
      D(3,0), D(3,1), D(3,2), D(5,0), D(5,1), D(5,2), D(5,3), D(5,4), D(6,0), D(6,1), D(6,2), D(6,3), D(6,4), D(6,5), D(7,0), D(7,1), D(7,2), D(7,3), D(7,4), D(7,5), D(7,6), D(8,0), D(8,1), D(8,2), D(8,3), D(8,4), D(8,5), D(8,6), D(8,7), D(9,0), D(9,1), D(9,2), D(9,3), D(9,7), D(9,8), D(10,0), D(10,1), D(10,2), D(10,3), D(10,4), D(10,5), D(10,6), D(10,7), D(10,8), D(10,9), D(11,0), D(11,1), D(11,2), D(11,3), D(11,4), D(11,5), D(11,6), D(11,7), D(11,8), D(11,9), D(11,10), D(12,0), D(12,1), D(12,2), D(12,3), D(12,4), D(12,5), D(12,6), D(12,7), D(12,8), D(12,9), D(12,10), D(12,11)

    DISAGREEMENTS: 3 of 71 games
      D(9,4): first disagreement at n = 22
          misere-P but not predicted (1): [22]
          predicted but not misere-P (0): []
      D(9,5): first disagreement at n = 23
          misere-P but not predicted (1): [23]
          predicted but not misere-P (0): []
      D(9,6): first disagreement at n = 24
          misere-P but not predicted (1): [24]
          predicted but not misere-P (0): []

    REBEL CHECK -- the prediction says rebels dissolve
      D(9,4): rebel n = 13 is misere-N   (normal play: P-position)
      D(9,5): rebel n = 14 is misere-N   (normal play: P-position)
      D(9,6): rebel n = 15 is misere-N   (normal play: P-position)
      prediction was that 13 in D(9,4) is misere-N.

    OBSERVATION, recorded not claimed: the three disagreeing positions are
    r + 18 (22, 23, 24), which are the same positions Task 2 lists as the second
    genuine palette deficiency in each exceptional game. The two sweeps are
    independent runs; the coincidence is reported, not explained.

    elapsed: 1.1s
"""
import sys
import time

DEPTH = 50000
MODULI = [3, 5, 6, 7, 8, 9, 10, 11, 12]
EXCEPTIONAL = [(9, 4), (9, 5), (9, 6)]


def misere_outcomes(m, r, N):
    """True = misere-P. Terminal positions are misere-N."""
    P = bytearray(N + 1)
    sq, k = [], 1
    while k * k <= N:
        sq.append(k * k)
        k += 1
    nsq = 0
    for n in range(0, N + 1):
        while nsq < len(sq) and sq[nsq] <= n:
            nsq += 1
        if n % m == r:
            if nsq == 0:
                P[n] = 0                       # terminal -> N
            else:
                allN = 1
                for i in range(nsq):
                    if P[n - sq[i]]:
                        allN = 0
                        break
                P[n] = allN
        else:
            P[n] = 0 if n < m else (0 if P[n - m] else 1)
    return P


def predicted(m, r, N):
    bottoms = [c for c in range(m) if c != r]
    tops = {(c + m) % (2 * m) for c in bottoms}
    free_min = r if r >= 1 else m
    S = set()
    for n in range(N + 1):
        if n % (2 * m) in tops:
            S.add(n)
    S.add(free_min)
    return S


def main():
    t0 = time.time()
    healthy = [(m, r) for m in MODULI for r in range(m) if (m, r) not in set(EXCEPTIONAL)]
    games = healthy + EXCEPTIONAL
    print("Phase 0 / Task 3 -- misere outcome sweep, depth n = 0..%d" % DEPTH)
    print("games: %d healthy + %d exceptional = %d" % (len(healthy), len(EXCEPTIONAL), len(games)))
    print()
    agree, disagree = [], []
    for m, r in games:
        P = misere_outcomes(m, r, DEPTH)
        obs = {n for n in range(DEPTH + 1) if P[n]}
        pred = predicted(m, r, DEPTH)
        only_obs = sorted(obs - pred)
        only_pred = sorted(pred - obs)
        if not only_obs and not only_pred:
            agree.append((m, r))
        else:
            first = min(only_obs[:1] + only_pred[:1])
            disagree.append((m, r, first, only_obs[:8], only_pred[:8],
                             len(only_obs), len(only_pred)))
    print("EXACT AGREEMENT to depth %d: %d of %d games" % (DEPTH, len(agree), len(games)))
    if agree:
        print("  %s" % ", ".join("D(%d,%d)" % g for g in agree))
    print()
    print("DISAGREEMENTS: %d of %d games" % (len(disagree), len(games)))
    for m, r, first, oo, op, no, np_ in disagree:
        print("  D(%d,%d): first disagreement at n = %d" % (m, r, first))
        print("      misere-P but not predicted (%d): %s" % (no, oo))
        print("      predicted but not misere-P (%d): %s" % (np_, op))
    print()
    print("REBEL CHECK -- the prediction says rebels dissolve")
    for m, r in EXCEPTIONAL:
        P = misere_outcomes(m, r, DEPTH)
        rebel = m + r
        print("  D(%d,%d): rebel n = %d is misere-%s   (normal play: P-position)"
              % (m, r, rebel, "P" if P[rebel] else "N"))
    print("  prediction was that 13 in D(9,4) is misere-N.")
    print()
    print("OBSERVATION, recorded not claimed: the three disagreeing positions are")
    print("r + 18 (22, 23, 24), which are the same positions Task 2 lists as the second")
    print("genuine palette deficiency in each exceptional game. The two sweeps are")
    print("independent runs; the coincidence is reported, not explained.")
    print()
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
