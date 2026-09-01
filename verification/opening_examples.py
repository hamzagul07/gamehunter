#!/usr/bin/env python3
"""The two opening examples, checked to the depth they are claimed at.

PROVENANCE. Written and executed locally in this repository; the output
pasted into the header below is this file's own output, and a re-run
reproduces it.

SCOPE. Finite computation to n = 200,000. Agreement means agreement over
the range checked and nothing beyond it: no statement here is a proof, and
a disagreement past the last index checked would not contradict anything
printed. The negative controls in check (c) exist to show that the
checkers can fail -- a checker that cannot report a violation has not
verified anything.

WHAT IS CHECKED

  (a) D(3,1): squares mode at n = 1 (mod 3), else subtract exactly 3.
      Claim: the P-positions are exactly n = 0, 2 (mod 6).

  (b) D(2,1): squares mode at odd n, else subtract exactly 2.
      Claim (i):  among even n, the P-positions are exactly n = 0 (mod 4).
      Claim (ii): every odd P-position has the form n = 4t + 3, and the
                  set of such t is exactly the P-set of Golomb's
                  subtract-a-square game (OEIS A030193).
      Claim (ii) presupposes that no odd P-position is 1 (mod 4); that is
      checked separately rather than assumed.

  (c) Negative controls: each claimed law is perturbed by one residue (or,
      for Golomb, by one element) and the same checker is re-run. Each
      perturbation must produce a violation.

Outcomes are recomputed from the rules by the solvers below; nothing is
imported from game_hunter.py, so an engine fault could not be echoed here.

Local run:

    $ python3 verification/opening_examples.py

    opening_examples.py -- finite checks to n = 200000
    ========================================================================
    CHECK (a)  D(3,1): squares at n = 1 (mod 3), else subtract 3
      claim            : P-positions are exactly n = 0, 2 (mod 6)
      range            : n = 0..200000
      first disagreement: none
      P-count          : 66668   (density 0.333338; 2 of 6 residues = 0.333333)
      first 12 P       : [0, 2, 6, 8, 12, 14, 18, 20, 24, 26, 30, 32]

    CHECK (b)  D(2,1): squares at odd n, else subtract 2
      (i)  claim       : among even n, P exactly at n = 0 (mod 4)
           first disagreement: none
      (ii) odd P-positions that are NOT 3 (mod 4): 0
           claim       : odd P-positions are n = 4t+3 with t in Golomb's P-set
           index range : t = 0..49999  (n up to 199999)
           first disagreement: none

           odd P-positions of D(2,1)    Golomb P-positions
           (first 12)                   (first 12)
                3  = 4*0 + 3                 0
               11  = 4*2 + 3                 2
               23  = 4*5 + 3                 5
               31  = 4*7 + 3                 7
               43  = 4*10 + 3               10
               51  = 4*12 + 3               12
               63  = 4*15 + 3               15
               71  = 4*17 + 3               17
               83  = 4*20 + 3               20
               91  = 4*22 + 3               22
              139  = 4*34 + 3               34
              159  = 4*39 + 3               39
           counts over the checked range: 1724 odd P-positions, 1724 Golomb P-positions

    CHECK (c)  negative controls -- each perturbation must be caught
      (a) law + residue 4 (mod 6)                  violation at 4  OK
      (a) law - residue 2 (mod 6)                  violation at 2  OK
      (b)(i) law + residue 2 (mod 4)               violation at 2  OK
      (b)(ii) Golomb set - one element (t = 2)     violation at 2  OK
      (b)(ii) Golomb set + one element (t = 1)     violation at 1  OK

    ========================================================================
    claims (a), (b)(i), (b)(ii) hold over n <= 200000 : True
    every negative control produced a violation    : True
    Finite checks over the stated range; not proofs.
    elapsed: 0.9s
"""
import sys
import time

DEPTH = 200000


# ---------------------------------------------------------------------------
# solvers -- P[n] = 1 iff n is a P-position under normal play
# ---------------------------------------------------------------------------

def diagonal(m, r, N):
    """D(m,r): from n = r (mod m) subtract any positive square <= n;
    from every other position subtract exactly m."""
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
            P[n] = 1 if n < m else (0 if P[n - m] else 1)
    return P


def golomb(T):
    """Subtract-a-square: P-positions on 0..T (OEIS A030193)."""
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


# ---------------------------------------------------------------------------
# checkers -- each returns the first disagreeing index, or None
# ---------------------------------------------------------------------------

def check_residue_law(P, N, modulus, residues, restrict=None):
    """First n <= N where P-ness disagrees with 'n mod modulus in residues'.

    restrict, if given, is a predicate limiting which n are examined.
    """
    res = set(residues)
    for n in range(N + 1):
        if restrict is not None and not restrict(n):
            continue
        if bool(P[n]) != (n % modulus in res):
            return n
    return None


def check_index_set(P, N, base, step, index_set, label_limit=None):
    """Check {t : base + step*t is P} == index_set, over base+step*t <= N.

    Returns (first_disagreeing_t, kind) or None.
    """
    tmax = (N - base) // step
    for t in range(tmax + 1):
        inP = bool(P[base + step * t])
        inS = t in index_set
        if inP != inS:
            return (t, "P but not in set" if inP else "in set but not P")
    return None


# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    ok = True
    print("opening_examples.py -- finite checks to n = %d" % DEPTH)
    print("=" * 72)

    # ---------------- (a) D(3,1) ----------------
    print("CHECK (a)  D(3,1): squares at n = 1 (mod 3), else subtract 3")
    P3 = diagonal(3, 1, DEPTH)
    bad = check_residue_law(P3, DEPTH, 6, (0, 2))
    print("  claim            : P-positions are exactly n = 0, 2 (mod 6)")
    print("  range            : n = 0..%d" % DEPTH)
    print("  first disagreement: %s" % ("none" if bad is None else bad))
    pc = sum(P3)
    print("  P-count          : %d   (density %.6f; 2 of 6 residues = %.6f)"
          % (pc, pc / (DEPTH + 1), 2 / 6))
    print("  first 12 P       : %s" % [n for n in range(DEPTH + 1) if P3[n]][:12])
    ok = ok and bad is None
    print()

    # ---------------- (b) D(2,1) ----------------
    print("CHECK (b)  D(2,1): squares at odd n, else subtract 2")
    P2 = diagonal(2, 1, DEPTH)

    # (i) even positions
    bad_even = check_residue_law(P2, DEPTH, 4, (0,), restrict=lambda n: n % 2 == 0)
    print("  (i)  claim       : among even n, P exactly at n = 0 (mod 4)")
    print("       first disagreement: %s" % ("none" if bad_even is None else bad_even))
    ok = ok and bad_even is None

    # (ii) odd positions: first confirm none is 1 (mod 4)
    odd_P = [n for n in range(1, DEPTH + 1, 2) if P2[n]]
    stray = [n for n in odd_P if n % 4 != 3]
    print("  (ii) odd P-positions that are NOT 3 (mod 4): %d %s"
          % (len(stray), stray[:5] if stray else ""))
    ok = ok and not stray

    tmax = (DEPTH - 3) // 4
    G = golomb(tmax)
    Gset = {t for t in range(tmax + 1) if G[t]}
    bad_idx = check_index_set(P2, DEPTH, 3, 4, Gset)
    print("       claim       : odd P-positions are n = 4t+3 with t in Golomb's P-set")
    print("       index range : t = 0..%d  (n up to %d)" % (tmax, 3 + 4 * tmax))
    print("       first disagreement: %s"
          % ("none" if bad_idx is None else "t = %d (%s)" % bad_idx))
    ok = ok and bad_idx is None

    print()
    print("       %-28s %s" % ("odd P-positions of D(2,1)", "Golomb P-positions"))
    print("       %-28s %s" % ("(first 12)", "(first 12)"))
    gl = sorted(Gset)[:12]
    for a, b in zip(odd_P[:12], gl):
        print("       %-28s %s" % ("%6d  = 4*%d + 3" % (a, (a - 3) // 4), "%6d" % b))
    print("       counts over the checked range: %d odd P-positions, %d Golomb P-positions"
          % (len(odd_P), len(Gset)))
    print()

    # ---------------- (c) negative controls ----------------
    print("CHECK (c)  negative controls -- each perturbation must be caught")
    controls = []

    b = check_residue_law(P3, DEPTH, 6, (0, 2, 4))
    controls.append(("(a) law + residue 4 (mod 6)", b))
    b = check_residue_law(P3, DEPTH, 6, (0,))
    controls.append(("(a) law - residue 2 (mod 6)", b))
    b = check_residue_law(P2, DEPTH, 4, (0, 2), restrict=lambda n: n % 2 == 0)
    controls.append(("(b)(i) law + residue 2 (mod 4)", b))

    pert = set(Gset)
    pert.discard(sorted(Gset)[1])            # drop Golomb's second P-position
    r = check_index_set(P2, DEPTH, 3, 4, pert)
    controls.append(("(b)(ii) Golomb set - one element (t = %d)" % sorted(Gset)[1],
                     None if r is None else r[0]))
    pert = set(Gset)
    add = next(t for t in range(tmax + 1) if t not in Gset)
    pert.add(add)                            # add a non-P index
    r = check_index_set(P2, DEPTH, 3, 4, pert)
    controls.append(("(b)(ii) Golomb set + one element (t = %d)" % add,
                     None if r is None else r[0]))

    allcaught = True
    for label, first in controls:
        caught = first is not None
        allcaught = allcaught and caught
        print("  %-44s %s" % (label,
              "violation at %s  OK" % first if caught else "NO VIOLATION  *** CONTROL FAILED ***"))
    print()
    print("=" * 72)
    print("claims (a), (b)(i), (b)(ii) hold over n <= %d : %s" % (DEPTH, ok))
    print("every negative control produced a violation    : %s" % allcaught)
    print("Finite checks over the stated range; not proofs.")
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0 if (ok and allcaught) else 1


if __name__ == "__main__":
    sys.exit(main())
