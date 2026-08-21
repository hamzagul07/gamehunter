#!/usr/bin/env python3
"""Phase 0, Task 1 -- Grundy census for the healthy diagonal games.

PROVENANCE. Written and executed locally in this repository; the output
pasted below is this file's own output and a re-run reproduces it.

SCOPE. Everything here is a finite computation over a stated range. No
claim is made about any n beyond the depth reported, and nothing below is
a proof. "Holds beyond N0" means "no mismatch was found between N0 and the
depth computed", nothing more.

WHAT IS TESTED. For D(m,r) with 3 <= m <= 12, m != 4, over class-r
positions n = r + t*m, the hypothesis

    g(n) = 2 + Gamma(floor(t/d) - a_rho),   rho = t mod d,

where Gamma is the nim-sequence of subtract-a-square and d = m0^2/m with
m = prod p^e and m0 = prod p^ceil(e/2). The offsets a_rho are FITTED here,
not derived: for each residue rho the script picks the shift minimising
mismatches. A fitted offset is a description of the data, not a result.

The three exceptional games D(9,4), D(9,5), D(9,6) are excluded: the paper
calls m = 9 healthy at every r except 4, 5, 6. They are swept in Task 3.

Local run:

    $ python3 verification/phase0/task1_grundy_census.py

    Phase 0 / Task 1 -- Grundy census, depth n = 0..200000
    healthy games swept: 68   (3 <= m <= 12, m != 4, minus the three m=9 exceptions)
    Gamma (subtract-a-square nim-sequence) computed to u = 22322
    Gamma(0..11) = [0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1]   [OEIS A014586 opening]

    game      d   fitted offsets a_rho       bad below N0      mismatch above N0
    ----------------------------------------------------------------------------------------
    D(3,0 )  3   1,1,0                      [0, 3]    4       none
    D(3,1 )  3   1,0,0                      [1]       2       none
    D(3,2 )  3   1,0,0                      [2]       3       none
    D(5,0 )  5   1,1,0,0,0                  [0, 5]    6       none
    D(5,1 )  5   1,0,0,0,0                  [1]       2       none
    D(5,2 )  5   1,0,0,0,0                  [2]       3       none
    D(5,3 )  5   1,0,0,0,0                  [3]       4       none
    D(5,4 )  5   1,0,0,0,0                  [4]       5       none
    D(6,0 )  6   1,1,0,0,0,0                [0, 6]    7       none
    D(6,1 )  6   1,0,0,0,0,0                [1]       2       none
    D(6,2 )  6   1,0,0,0,0,0                [2]       3       none
    D(6,3 )  6   1,0,0,0,0,0                [3]       4       none
    D(6,4 )  6   1,0,0,0,0,0                [4]       5       none
    D(6,5 )  6   1,0,0,0,0,0                [5]       6       none
    D(7,0 )  7   1,1,0,0,0,0,0              [0, 7]    8       none
    D(7,1 )  7   1,0,0,0,0,0,0              [1]       2       none
    D(7,2 )  7   1,0,0,0,0,0,0              [2]       3       none
    D(7,3 )  7   1,0,0,0,0,0,0              [3]       4       none
    D(7,4 )  7   1,0,0,0,0,0,0              [4]       5       none
    D(7,5 )  7   1,0,0,0,0,0,0              [5]       6       none
    D(7,6 )  7   1,0,0,0,0,0,0              [6]       7       none
    D(8,0 )  2   1,1                        [0, 8]    9       none
    D(8,1 )  2   1,0                        [1]       2       none
    D(8,2 )  2   1,0                        [2]       3       none
    D(8,3 )  2   1,0                        [3]       4       none
    D(8,4 )  2   1,0                        [4]       5       none
    D(8,5 )  2   1,0                        [5]       6       none
    D(8,6 )  2   1,0                        [6]       7       none
    D(8,7 )  2   1,0                        [7]       8       none
    D(9,0 )  1   2                          [0, 9]    10      none
    D(9,1 )  1   1                          [1]       2       none
    D(9,2 )  1   1                          [2]       3       none
    D(9,3 )  1   1                          [3]       4       none
    D(9,7 )  1   1                          [7]       8       none
    D(9,8 )  1   1                          [8]       9       none
    D(10,0 )  10  1,1,0,0,0,0,0,0,0,0        [0, 10]   11      none
    D(10,1 )  10  1,0,0,0,0,0,0,0,0,0        [1]       2       none
    D(10,2 )  10  1,0,0,0,0,0,0,0,0,0        [2]       3       none
    D(10,3 )  10  1,0,0,0,0,0,0,0,0,0        [3]       4       none
    D(10,4 )  10  1,0,0,0,0,0,0,0,0,0        [4]       5       none
    D(10,5 )  10  1,0,0,0,0,0,0,0,0,0        [5]       6       none
    D(10,6 )  10  1,0,0,0,0,0,0,0,0,0        [6]       7       none
    D(10,7 )  10  1,0,0,0,0,0,0,0,0,0        [7]       8       none
    D(10,8 )  10  1,0,0,0,0,0,0,0,0,0        [8]       9       none
    D(10,9 )  10  1,0,0,0,0,0,0,0,0,0        [9]       10      none
    D(11,0 )  11  1,1,0,0,0,0,0,0,0,0,0      [0, 11]   12      none
    D(11,1 )  11  1,0,0,0,0,0,0,0,0,0,0      [1]       2       none
    D(11,2 )  11  1,0,0,0,0,0,0,0,0,0,0      [2]       3       none
    D(11,3 )  11  1,0,0,0,0,0,0,0,0,0,0      [3]       4       none
    D(11,4 )  11  1,0,0,0,0,0,0,0,0,0,0      [4]       5       none
    D(11,5 )  11  1,0,0,0,0,0,0,0,0,0,0      [5]       6       none
    D(11,6 )  11  1,0,0,0,0,0,0,0,0,0,0      [6]       7       none
    D(11,7 )  11  1,0,0,0,0,0,0,0,0,0,0      [7]       8       none
    D(11,8 )  11  1,0,0,0,0,0,0,0,0,0,0      [8]       9       none
    D(11,9 )  11  1,0,0,0,0,0,0,0,0,0,0      [9]       10      none
    D(11,10)  11  1,0,0,0,0,0,0,0,0,0,0      [10]      11      none
    D(12,0 )  3   1,1,0                      [0, 12]   13      none
    D(12,1 )  3   1,0,0                      [1]       2       none
    D(12,2 )  3   1,0,0                      [2]       3       none
    D(12,3 )  3   1,0,0                      [3]       4       none
    D(12,4 )  3   1,0,0                      [4]       5       none
    D(12,5 )  3   1,0,0                      [5]       6       none
    D(12,6 )  3   1,0,0                      [6]       7       none
    D(12,7 )  3   1,0,0                      [7]       8       none
    D(12,8 )  3   1,0,0                      [8]       9       none
    D(12,9 )  3   1,0,0                      [9]       10      none
    D(12,10)  3   1,0,0                      [10]      11      none
    D(12,11)  3   1,0,0                      [11]      12      none

    Every row's 'mismatch above N0' is none by construction: N0 is set to one past the
    largest mismatching position, so the finite bad set printed is the COMPLETE list of
    disagreements found anywhere in 0..200000.

    FITTED OFFSETS -- fit output, not a result. A nonzero a_rho describes the data;
    it is not a failure of anything.
      m=3   d=3
          a_rho = 1,1,0                    for r in [0]
          a_rho = 1,0,0                    for r in [1, 2]
      m=5   d=5
          a_rho = 1,1,0,0,0                for r in [0]
          a_rho = 1,0,0,0,0                for r in [1, 2, 3, 4]
      m=6   d=6
          a_rho = 1,1,0,0,0,0              for r in [0]
          a_rho = 1,0,0,0,0,0              for r in [1, 2, 3, 4, 5]
      m=7   d=7
          a_rho = 1,1,0,0,0,0,0            for r in [0]
          a_rho = 1,0,0,0,0,0,0            for r in [1, 2, 3, 4, 5, 6]
      m=8   d=2
          a_rho = 1,1                      for r in [0]
          a_rho = 1,0                      for r in [1, 2, 3, 4, 5, 6, 7]
      m=9   d=1
          a_rho = 2                        for r in [0]
          a_rho = 1                        for r in [1, 2, 3, 7, 8]
      m=10  d=10
          a_rho = 1,1,0,0,0,0,0,0,0,0      for r in [0]
          a_rho = 1,0,0,0,0,0,0,0,0,0      for r in [1, 2, 3, 4, 5, 6, 7, 8, 9]
      m=11  d=11
          a_rho = 1,1,0,0,0,0,0,0,0,0,0    for r in [0]
          a_rho = 1,0,0,0,0,0,0,0,0,0,0    for r in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      m=12  d=3
          a_rho = 1,1,0                    for r in [0]
          a_rho = 1,0,0                    for r in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    MISMATCHES -- the failures, reported in full
      games with at least one mismatch: 68 of 68
        D(3,0): bad = [0, 3]   N0 = 4
        D(3,1): bad = [1]   N0 = 2
        D(3,2): bad = [2]   N0 = 3
        D(5,0): bad = [0, 5]   N0 = 6
        D(5,1): bad = [1]   N0 = 2
        D(5,2): bad = [2]   N0 = 3
        D(5,3): bad = [3]   N0 = 4
        D(5,4): bad = [4]   N0 = 5
        D(6,0): bad = [0, 6]   N0 = 7
        D(6,1): bad = [1]   N0 = 2
        D(6,2): bad = [2]   N0 = 3
        D(6,3): bad = [3]   N0 = 4
        D(6,4): bad = [4]   N0 = 5
        D(6,5): bad = [5]   N0 = 6
        D(7,0): bad = [0, 7]   N0 = 8
        D(7,1): bad = [1]   N0 = 2
        D(7,2): bad = [2]   N0 = 3
        D(7,3): bad = [3]   N0 = 4
        D(7,4): bad = [4]   N0 = 5
        D(7,5): bad = [5]   N0 = 6
        D(7,6): bad = [6]   N0 = 7
        D(8,0): bad = [0, 8]   N0 = 9
        D(8,1): bad = [1]   N0 = 2
        D(8,2): bad = [2]   N0 = 3
        D(8,3): bad = [3]   N0 = 4
        D(8,4): bad = [4]   N0 = 5
        D(8,5): bad = [5]   N0 = 6
        D(8,6): bad = [6]   N0 = 7
        D(8,7): bad = [7]   N0 = 8
        D(9,0): bad = [0, 9]   N0 = 10
        D(9,1): bad = [1]   N0 = 2
        D(9,2): bad = [2]   N0 = 3
        D(9,3): bad = [3]   N0 = 4
        D(9,7): bad = [7]   N0 = 8
        D(9,8): bad = [8]   N0 = 9
        D(10,0): bad = [0, 10]   N0 = 11
        D(10,1): bad = [1]   N0 = 2
        D(10,2): bad = [2]   N0 = 3
        D(10,3): bad = [3]   N0 = 4
        D(10,4): bad = [4]   N0 = 5
        D(10,5): bad = [5]   N0 = 6
        D(10,6): bad = [6]   N0 = 7
        D(10,7): bad = [7]   N0 = 8
        D(10,8): bad = [8]   N0 = 9
        D(10,9): bad = [9]   N0 = 10
        D(11,0): bad = [0, 11]   N0 = 12
        D(11,1): bad = [1]   N0 = 2
        D(11,2): bad = [2]   N0 = 3
        D(11,3): bad = [3]   N0 = 4
        D(11,4): bad = [4]   N0 = 5
        D(11,5): bad = [5]   N0 = 6
        D(11,6): bad = [6]   N0 = 7
        D(11,7): bad = [7]   N0 = 8
        D(11,8): bad = [8]   N0 = 9
        D(11,9): bad = [9]   N0 = 10
        D(11,10): bad = [10]   N0 = 11
        D(12,0): bad = [0, 12]   N0 = 13
        D(12,1): bad = [1]   N0 = 2
        D(12,2): bad = [2]   N0 = 3
        D(12,3): bad = [3]   N0 = 4
        D(12,4): bad = [4]   N0 = 5
        D(12,5): bad = [5]   N0 = 6
        D(12,6): bad = [6]   N0 = 7
        D(12,7): bad = [7]   N0 = 8
        D(12,8): bad = [8]   N0 = 9
        D(12,9): bad = [9]   N0 = 10
        D(12,10): bad = [10]   N0 = 11
        D(12,11): bad = [11]   N0 = 12

      pattern check on the bad sets (observation, not a claim):
        every bad set equals {r} for r >= 1 and {0, m} for r = 0: True
        exceptions to that pattern: none

    total class-r positions checked : 1733343
    total disagreements found       : 77
    elapsed: 49.0s
"""
import sys
import time

DEPTH = 200000
MODULI = [3, 5, 6, 7, 8, 9, 10, 11, 12]
EXCLUDE = {(9, 4), (9, 5), (9, 6)}
FIT_RANGE = range(-5, 51)


def squarefree_step(m):
    """d = m0^2 / m with m0 = prod p^ceil(e/2); the squarefree part of m."""
    n, m0 = m, 1
    p = 2
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


def grundy_diagonal(m, r, N):
    """Exact Grundy values of D(m,r) on 0..N. No structure assumed."""
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


def gamma_sequence(T):
    """Nim-sequence of subtract-a-square on 0..T (OEIS A014586)."""
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


def fit_game(m, r, G, Gam, N):
    d = squarefree_step(m)
    ts = range(0, (N - r) // m + 1)
    obs = {}                       # rho -> list of (u, t, n, value)
    for t in ts:
        n = r + t * m
        obs.setdefault(t % d, []).append((t // d, t, n, G[n]))
    offsets, bad = {}, []
    for rho in range(d):
        rows = obs.get(rho, [])
        best, best_mis = None, None
        for a in FIT_RANGE:
            mis = 0
            for u, t, n, g in rows:
                idx = u - a
                if idx < 0 or idx >= len(Gam) or g != 2 + Gam[idx]:
                    mis += 1
            if best_mis is None or mis < best_mis or (mis == best_mis and abs(a) < abs(best)):
                best, best_mis = a, mis
        offsets[rho] = best
        for u, t, n, g in rows:
            idx = u - best
            if idx < 0 or idx >= len(Gam) or g != 2 + Gam[idx]:
                bad.append(n)
    bad.sort()
    N0 = (bad[-1] + 1) if bad else 0
    return d, offsets, bad, N0


def main():
    t0 = time.time()
    games = [(m, r) for m in MODULI for r in range(m) if (m, r) not in EXCLUDE]
    print("Phase 0 / Task 1 -- Grundy census, depth n = 0..%d" % DEPTH)
    print("healthy games swept: %d   (3 <= m <= 12, m != 4, minus the three m=9 exceptions)" % len(games))
    umax = max((DEPTH // m) // squarefree_step(m) for m in MODULI) + 100
    Gam = gamma_sequence(umax)
    print("Gamma (subtract-a-square nim-sequence) computed to u = %d" % umax)
    print("Gamma(0..11) = %s   [OEIS A014586 opening]" % list(Gam[:12]))
    print()
    print("%-9s %-3s %-26s %-9s %-7s %s" % ("game", "d", "fitted offsets a_rho", "bad below", "N0", "mismatch above N0"))
    print("-" * 88)
    all_bad, failures = {}, []
    for m, r in games:
        G = grundy_diagonal(m, r, DEPTH)
        d, off, bad, N0 = fit_game(m, r, G, Gam, DEPTH)
        all_bad[(m, r)] = (d, off, bad, N0)
        offs = ",".join(str(off[i]) for i in range(d))
        shown = str(bad[:6]) + (" ...(%d)" % len(bad) if len(bad) > 6 else "")
        print("D(%d,%-2d)  %-3d %-26s %-9s %-7d %s"
              % (m, r, d, offs if len(offs) <= 26 else offs[:23] + "...", shown, N0, "none"))
        if any(a != 0 for a in off.values()):
            failures.append(("nonzero fitted offset", m, r, off))
    print()
    print("Every row's \'mismatch above N0\' is none by construction: N0 is set to one past the")
    print("largest mismatching position, so the finite bad set printed is the COMPLETE list of")
    print("disagreements found anywhere in 0..%d." % DEPTH)
    print()
    print("FITTED OFFSETS -- fit output, not a result. A nonzero a_rho describes the data;")
    print("it is not a failure of anything.")
    for m in MODULI:
        d = squarefree_step(m)
        pats = {}
        for r in range(m):
            if (m, r) in all_bad:
                pats.setdefault(tuple(all_bad[(m, r)][1][i] for i in range(d)), []).append(r)
        print("  m=%-3d d=%-3d" % (m, d))
        for pat, rs in sorted(pats.items(), key=lambda kv: kv[1]):
            print("      a_rho = %-24s for r in %s" % (",".join(map(str, pat)), rs))
    print()
    print("MISMATCHES -- the failures, reported in full")
    nonempty = [(k, v) for k, v in sorted(all_bad.items()) if v[2]]
    print("  games with at least one mismatch: %d of %d" % (len(nonempty), len(games)))
    for (m, r), (d, off, bad, N0) in nonempty:
        print("    D(%d,%d): bad = %s   N0 = %d" % (m, r, bad, N0))
    print()
    print("  pattern check on the bad sets (observation, not a claim):")
    as_pred = all((bad == [r]) if r >= 1 else (bad == [0, m])
                  for (m, r), (d, o, bad, N0) in all_bad.items())
    print("    every bad set equals {r} for r >= 1 and {0, m} for r = 0: %s" % as_pred)
    odd = [(m, r, v[2]) for (m, r), v in all_bad.items()
           if (v[2] != [r] if r >= 1 else v[2] != [0, m])]
    print("    exceptions to that pattern: %s" % (odd if odd else "none"))
    tot = sum(len(v[2]) for v in all_bad.values())
    print()
    print("total class-r positions checked : %d" % sum((DEPTH - r) // m + 1 for m, r in games))
    print("total disagreements found       : %d" % tot)
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
