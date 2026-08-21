#!/usr/bin/env python3
"""Phase 0, Task 2 -- palette-deficiency catalogue.

PROVENANCE. Written and executed locally in this repository; the output
pasted below is this file's own output and a re-run reproduces it.

SCOPE. Finite computation over a stated range. Nothing here is a proof and
nothing is claimed beyond the depth reported.

WHAT IS LISTED. For each healthy D(m,r), every class-r position that lacks
a Grundy-0 foreign landing, or lacks a Grundy-1 foreign landing. A foreign
landing is a legal square move n - k^2 whose target is NOT in class r; its
Grundy value is read from the computed array, not assumed.

The prediction under test is that the deficient set is exactly the first
free member -- r when r >= 1, m when r = 0 -- with extras expected at
m = 9, r in {4,5,6} around 4, 13, 22 and analogues. The three m=9
exceptional games are swept here alongside the healthy ones so that the
predicted extras can actually be looked for.

Local run:

    $ python3 verification/phase0/task2_palette_catalogue.py

    Phase 0 / Task 2 -- palette-deficiency catalogue, depth n = 0..20000
    games: 68 healthy + 3 exceptional (m=9, r=4,5,6) = 71

    game       predict  deficient class-r positions (missing Grundy values)
    --------------------------------------------------------------------------------------------
    D(3,0 )   3        0(missing 0,1), 3(missing 1)
    D(3,1 )   1        1(missing 1)
    D(3,2 )   2        2(missing 1)
    D(5,0 )   5        0(missing 0,1), 5(missing 1)
    D(5,1 )   1        1(missing 1)
    D(5,2 )   2        2(missing 1)
    D(5,3 )   3        3(missing 1)
    D(5,4 )   4        4(missing 1)
    D(6,0 )   6        0(missing 0,1), 6(missing 1)
    D(6,1 )   1        1(missing 1)
    D(6,2 )   2        2(missing 1)
    D(6,3 )   3        3(missing 1)
    D(6,4 )   4        4(missing 1)
    D(6,5 )   5        5(missing 1)
    D(7,0 )   7        0(missing 0,1), 7(missing 1)
    D(7,1 )   1        1(missing 1)
    D(7,2 )   2        2(missing 1)
    D(7,3 )   3        3(missing 1)
    D(7,4 )   4        4(missing 1)
    D(7,5 )   5        5(missing 1)
    D(7,6 )   6        6(missing 1)
    D(8,0 )   8        0(missing 0,1), 8(missing 1)
    D(8,1 )   1        1(missing 1)
    D(8,2 )   2        2(missing 1)
    D(8,3 )   3        3(missing 1)
    D(8,4 )   4        4(missing 1)
    D(8,5 )   5        5(missing 1)
    D(8,6 )   6        6(missing 1)
    D(8,7 )   7        7(missing 1)
    D(9,0 )   9        0(missing 0,1), 9(missing 1)
    D(9,1 )   1        1(missing 1)
    D(9,2 )   2        2(missing 1)
    D(9,3 )   3        3(missing 1)
    D(9,7 )   7        7(missing 1)
    D(9,8 )   8        8(missing 1)
    D(10,0 )   10       0(missing 0,1), 10(missing 1)
    D(10,1 )   1        1(missing 1)
    D(10,2 )   2        2(missing 1)
    D(10,3 )   3        3(missing 1)
    D(10,4 )   4        4(missing 1)
    D(10,5 )   5        5(missing 1)
    D(10,6 )   6        6(missing 1)
    D(10,7 )   7        7(missing 1)
    D(10,8 )   8        8(missing 1)
    D(10,9 )   9        9(missing 1)
    D(11,0 )   11       0(missing 0,1), 11(missing 1)
    D(11,1 )   1        1(missing 1)
    D(11,2 )   2        2(missing 1)
    D(11,3 )   3        3(missing 1)
    D(11,4 )   4        4(missing 1)
    D(11,5 )   5        5(missing 1)
    D(11,6 )   6        6(missing 1)
    D(11,7 )   7        7(missing 1)
    D(11,8 )   8        8(missing 1)
    D(11,9 )   9        9(missing 1)
    D(11,10)   10       10(missing 1)
    D(12,0 )   12       0(missing 0,1), 12(missing 1)
    D(12,1 )   1        1(missing 1)
    D(12,2 )   2        2(missing 1)
    D(12,3 )   3        3(missing 1)
    D(12,4 )   4        4(missing 1)
    D(12,5 )   5        5(missing 1)
    D(12,6 )   6        6(missing 1)
    D(12,7 )   7        7(missing 1)
    D(12,8 )   8        8(missing 1)
    D(12,9 )   9        9(missing 1)
    D(12,10)   10       10(missing 1)
    D(12,11)   11       11(missing 1)
    D(9,4 )   4        4(missing 1), 13(missing 0), 22(missing 1)
    D(9,5 )   5        5(missing 1), 14(missing 0), 23(missing 1)
    D(9,6 )   6        6(missing 1), 15(missing 0), 24(missing 1)

    PREDICTION: deficient set == {first free member} exactly
      games matching exactly            : 59
      games with extras or shortfalls   : 12

      EXTRAS / DEVIATIONS, in full:
        D(3,0): first free = 3, deficient = [0, 3]  ->  extras [0]
        D(5,0): first free = 5, deficient = [0, 5]  ->  extras [0]
        D(6,0): first free = 6, deficient = [0, 6]  ->  extras [0]
        D(7,0): first free = 7, deficient = [0, 7]  ->  extras [0]
        D(8,0): first free = 8, deficient = [0, 8]  ->  extras [0]
        D(9,0): first free = 9, deficient = [0, 9]  ->  extras [0]
        D(10,0): first free = 10, deficient = [0, 10]  ->  extras [0]
        D(11,0): first free = 11, deficient = [0, 11]  ->  extras [0]
        D(12,0): first free = 12, deficient = [0, 12]  ->  extras [0]
        D(9,4): first free = 4, deficient = [4, 13, 22]  ->  extras [13, 22]
        D(9,5): first free = 5, deficient = [5, 14, 23]  ->  extras [14, 23]
        D(9,6): first free = 6, deficient = [6, 15, 24]  ->  extras [15, 24]

      Not every extra is structural. n = 0 has no legal move at all (no square is
      <= 0), so it is vacuously deficient; it appears only in the r = 0 games, where
      0 is a class-r position. Classifying the extras accordingly:
        extras that are exactly the terminal n = 0 : 9 games [(3, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0)]
        genuine non-terminal extras                : 3 games
            D(9,4) -> [13, 22]
            D(9,5) -> [14, 23]
            D(9,6) -> [15, 24]

      predicted-extra games were m = 9, r in {4,5,6} around 4, 13, 22 and analogues.
      games with genuine extras         : [(9, 4), (9, 5), (9, 6)]
      matches the predicted set exactly : True
      predicted positions 4, 13, 22 (and analogues r, r+9, r+18) observed: True
    elapsed: 1.7s
"""
import sys
import time

DEPTH = 20000
MODULI = [3, 5, 6, 7, 8, 9, 10, 11, 12]
EXCEPTIONAL = [(9, 4), (9, 5), (9, 6)]


def grundy_diagonal(m, r, N):
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
            g = 0
            while mark[g] == n:
                g += 1
            G[n] = g
        elif n < m:
            G[n] = 0
        else:
            G[n] = 1 if G[n - m] == 0 else 0
    return G


def deficiencies(m, r, G, N):
    """class-r positions missing a Grundy-0 or Grundy-1 foreign landing."""
    out = []
    for n in range(r, N + 1, m):
        has0 = has1 = False
        k = 1
        while k * k <= n:
            tgt = n - k * k
            if tgt % m != r:                      # foreign landing
                v = G[tgt]
                if v == 0:
                    has0 = True
                elif v == 1:
                    has1 = True
            if has0 and has1:
                break
            k += 1
        if not (has0 and has1):
            miss = []
            if not has0:
                miss.append(0)
            if not has1:
                miss.append(1)
            out.append((n, miss))
    return out


def main():
    t0 = time.time()
    healthy = [(m, r) for m in MODULI for r in range(m) if (m, r) not in set(EXCEPTIONAL)]
    print("Phase 0 / Task 2 -- palette-deficiency catalogue, depth n = 0..%d" % DEPTH)
    print("games: %d healthy + %d exceptional (m=9, r=4,5,6) = %d"
          % (len(healthy), len(EXCEPTIONAL), len(healthy) + len(EXCEPTIONAL)))
    print()
    print("%-10s %-8s %s" % ("game", "predict", "deficient class-r positions (missing Grundy values)"))
    print("-" * 92)
    exact, extras_found = [], []
    for m, r in healthy + EXCEPTIONAL:
        G = grundy_diagonal(m, r, DEPTH)
        d = deficiencies(m, r, G, DEPTH)
        first_free = r if r >= 1 else m
        got = [n for n, _ in d]
        is_exact = (got == [first_free])
        (exact if is_exact else extras_found).append((m, r, got))
        shown = ", ".join("%d(missing %s)" % (n, ",".join(map(str, ms))) for n, ms in d[:6])
        if len(d) > 6:
            shown += "  ...(%d total)" % len(d)
        print("D(%d,%-2d)   %-8d %s" % (m, r, first_free, shown if shown else "(none)"))
    print()
    print("PREDICTION: deficient set == {first free member} exactly")
    print("  games matching exactly            : %d" % len(exact))
    print("  games with extras or shortfalls   : %d" % len(extras_found))
    if extras_found:
        print()
        print("  EXTRAS / DEVIATIONS, in full:")
        for m, r, got in extras_found:
            ff = r if r >= 1 else m
            print("    D(%d,%d): first free = %d, deficient = %s  ->  extras %s"
                  % (m, r, ff, got, [x for x in got if x != ff]))
    print()
    print("  Not every extra is structural. n = 0 has no legal move at all (no square is")
    print("  <= 0), so it is vacuously deficient; it appears only in the r = 0 games, where")
    print("  0 is a class-r position. Classifying the extras accordingly:")
    trivial, genuine = [], []
    for m, r, got in extras_found:
        ff = r if r >= 1 else m
        ex = [x for x in got if x != ff]
        (trivial if ex == [0] else genuine).append((m, r, ex))
    print("    extras that are exactly the terminal n = 0 : %d games %s"
          % (len(trivial), sorted((m, r) for m, r, _ in trivial)))
    print("    genuine non-terminal extras                : %d games" % len(genuine))
    for m, r, ex in genuine:
        print("        D(%d,%d) -> %s" % (m, r, ex))
    print()
    print("  predicted-extra games were m = 9, r in {4,5,6} around 4, 13, 22 and analogues.")
    pred = {(9, 4), (9, 5), (9, 6)}
    actual = {(m, r) for m, r, _ in genuine}
    print("  games with genuine extras         : %s" % sorted(actual))
    print("  matches the predicted set exactly : %s" % (actual == pred))
    print("  predicted positions 4, 13, 22 (and analogues r, r+9, r+18) observed: %s"
          % all(ex == [r + 9, r + 18] for m, r, ex in genuine))
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
