#!/usr/bin/env python3
"""What the squares actually do: D(m,r) against the plain subtract-{m} game.

PROVENANCE. Written and executed locally in this repository; the output
pasted into the header below is this file's own output, and a re-run
reproduces it.

SCOPE. Finite computation to n = 100,000. Every statement printed is a
statement about that range and nothing past it. No pattern reported here
is a proof, and none is claimed to persist beyond the last index checked.
The negative control at the end exists to show the comparator can report a
difference that is not there -- a comparator that always says the same
thing has compared nothing.

WHAT IS COMPARED, per game

  (A) D(m,r): from n = r (mod m) subtract any positive square <= n; from
      every other position subtract exactly m.
  (B) the plain subtraction game with move set {m}: subtract exactly m
      from every position, squares nowhere.

Reported per game: the residues modulo 2m occupied by (B) and by (A),
separating residues every one of whose positions is P ("full") from
residues holding only some ("partial"); the set difference in both
directions; and the positions P in exactly one of the two games, listed
when at most 20 and counted otherwise.

Both P-sets are recomputed from the rules by the solvers below; nothing is
imported from game_hunter.py, so an engine fault could not be echoed here.

Local run:

    $ python3 verification/squares_vs_fallback.py

    squares_vs_fallback.py -- (A) D(m,r) against (B) subtract-{m}, n = 0..100000
    ==============================================================================
    
    ### r = 0, healthy
    
      D(7,0)   modulus 2m = 14
        (B) subtract-{7}   full residues [0, 1, 2, 3, 4, 5, 6]  partial none
        (A) D(7,0)         full residues [1, 2, 3, 4, 5, 6]  partial [0]
        P in (B) only : 7142 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 7142 positions (over 20, not listed)
        observed      : residue class 0 (mod 14) deleted except 1: [0]
    
      D(5,0)   modulus 2m = 10
        (B) subtract-{5}   full residues [0, 1, 2, 3, 4]  partial none
        (A) D(5,0)         full residues [1, 2, 3, 4]  partial [0]
        P in (B) only : 10000 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 10000 positions (over 20, not listed)
        observed      : residue class 0 (mod 10) deleted except 1: [0]
    
      D(3,0)   modulus 2m = 6
        (B) subtract-{3}   full residues [0, 1, 2]  partial none
        (A) D(3,0)         full residues [1, 2]  partial [0]
        P in (B) only : 16666 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 16666 positions (over 20, not listed)
        observed      : residue class 0 (mod 6) deleted except 1: [0]
    
      D(11,0)   modulus 2m = 22
        (B) subtract-{11}  full residues [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  partial none
        (A) D(11,0)        full residues [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  partial [0]
        P in (B) only : 4545 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 4545 positions (over 20, not listed)
        observed      : residue class 0 (mod 22) deleted except 1: [0]
    
      SUMMARY [r = 0, healthy]: one class deleted, survivors listed/counted across all 4 games
    
    ### r >= 1, healthy
    
      D(3,1)   modulus 2m = 6
        (B) subtract-{3}   full residues [0, 1, 2]  partial none
        (A) D(3,1)         full residues [0, 2]  partial none
        P in (B) only : 16667 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 16667 positions (over 20, not listed)
        observed      : residue class 1 (mod 6) deleted entirely
    
      D(5,2)   modulus 2m = 10
        (B) subtract-{5}   full residues [0, 1, 2, 3, 4]  partial none
        (A) D(5,2)         full residues [0, 1, 3, 4]  partial none
        P in (B) only : 10000 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 10000 positions (over 20, not listed)
        observed      : residue class 2 (mod 10) deleted entirely
    
      D(7,3)   modulus 2m = 14
        (B) subtract-{7}   full residues [0, 1, 2, 3, 4, 5, 6]  partial none
        (A) D(7,3)         full residues [0, 1, 2, 4, 5, 6]  partial none
        P in (B) only : 7143 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 7143 positions (over 20, not listed)
        observed      : residue class 3 (mod 14) deleted entirely
    
      D(11,4)   modulus 2m = 22
        (B) subtract-{11}  full residues [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  partial none
        (A) D(11,4)        full residues [0, 1, 2, 3, 5, 6, 7, 8, 9, 10]  partial none
        P in (B) only : 4546 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 4546 positions (over 20, not listed)
        observed      : residue class 4 (mod 22) deleted entirely
    
      D(12,5)   modulus 2m = 24
        (B) subtract-{12}  full residues [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  partial none
        (A) D(12,5)        full residues [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]  partial none
        P in (B) only : 4167 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 4167 positions (over 20, not listed)
        observed      : residue class 5 (mod 24) deleted entirely
    
      SUMMARY [r >= 1, healthy]: one class deleted across all 5 games
    
    ### the exceptional trio
    
      D(9,4)   modulus 2m = 18
        (B) subtract-{9}   full residues [0, 1, 2, 3, 4, 5, 6, 7, 8]  partial none
        (A) D(9,4)         full residues [0, 1, 2, 3, 5, 6, 7, 8]  partial [13]
        P in (B) only : 5556 positions (over 20, not listed)
        P in (A) only : 1: [13]
        symmetric diff: 5557 positions (over 20, not listed)
        observed      : residue class 4 (mod 18) deleted entirely; plus 1: [13] gained at residue [13] (mod 18)
    
      D(9,5)   modulus 2m = 18
        (B) subtract-{9}   full residues [0, 1, 2, 3, 4, 5, 6, 7, 8]  partial none
        (A) D(9,5)         full residues [0, 1, 2, 3, 4, 6, 7, 8]  partial [14]
        P in (B) only : 5556 positions (over 20, not listed)
        P in (A) only : 1: [14]
        symmetric diff: 5557 positions (over 20, not listed)
        observed      : residue class 5 (mod 18) deleted entirely; plus 1: [14] gained at residue [14] (mod 18)
    
      D(9,6)   modulus 2m = 18
        (B) subtract-{9}   full residues [0, 1, 2, 3, 4, 5, 6, 7, 8]  partial none
        (A) D(9,6)         full residues [0, 1, 2, 3, 4, 5, 7, 8]  partial [15]
        P in (B) only : 5556 positions (over 20, not listed)
        P in (A) only : 1: [15]
        symmetric diff: 5557 positions (over 20, not listed)
        observed      : residue class 6 (mod 18) deleted entirely; plus 1: [15] gained at residue [15] (mod 18)
    
      SUMMARY [the exceptional trio]: one class deleted, plus gains across all 3 games
    
    ### the degenerate moduli
    
      D(2,0)   modulus 2m = 4
        (B) subtract-{2}   full residues [0, 1]  partial none
        (A) D(2,0)         full residues [1]  partial [0]
        P in (B) only : 23932 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 23932 positions (over 20, not listed)
        observed      : residue class 0 (mod 4) deleted except 1069 positions (over 20, not listed)
    
      D(2,1)   modulus 2m = 4
        (B) subtract-{2}   full residues [0, 1]  partial none
        (A) D(2,1)         full residues [0]  partial [3]
        P in (B) only : 25000 positions (over 20, not listed)
        P in (A) only : 1069 positions (over 20, not listed)
        symmetric diff: 26069 positions (over 20, not listed)
        observed      : residue class 1 (mod 4) deleted entirely; plus 1069 positions (over 20, not listed) gained at residue [3] (mod 4)
    
      D(4,0)   modulus 2m = 8
        (B) subtract-{4}   full residues [0, 1, 2, 3]  partial none
        (A) D(4,0)         full residues [1, 2, 3]  partial [0]
        P in (B) only : 11683 positions (over 20, not listed)
        P in (A) only : 0: (empty)
        symmetric diff: 11683 positions (over 20, not listed)
        observed      : residue class 0 (mod 8) deleted except 818 positions (over 20, not listed)
    
      D(4,1)   modulus 2m = 8
        (B) subtract-{4}   full residues [0, 1, 2, 3]  partial none
        (A) D(4,1)         full residues [0, 2, 3]  partial [5]
        P in (B) only : 12500 positions (over 20, not listed)
        P in (A) only : 818 positions (over 20, not listed)
        symmetric diff: 13318 positions (over 20, not listed)
        observed      : residue class 1 (mod 8) deleted entirely; plus 818 positions (over 20, not listed) gained at residue [5] (mod 8)
    
      D(4,2)   modulus 2m = 8
        (B) subtract-{4}   full residues [0, 1, 2, 3]  partial none
        (A) D(4,2)         full residues [0, 1, 3]  partial [6]
        P in (B) only : 12500 positions (over 20, not listed)
        P in (A) only : 818 positions (over 20, not listed)
        symmetric diff: 13318 positions (over 20, not listed)
        observed      : residue class 2 (mod 8) deleted entirely; plus 818 positions (over 20, not listed) gained at residue [6] (mod 8)
    
      D(4,3)   modulus 2m = 8
        (B) subtract-{4}   full residues [0, 1, 2, 3]  partial none
        (A) D(4,3)         full residues [0, 1, 2]  partial [7]
        P in (B) only : 12500 positions (over 20, not listed)
        P in (A) only : 818 positions (over 20, not listed)
        symmetric diff: 13318 positions (over 20, not listed)
        observed      : residue class 3 (mod 8) deleted entirely; plus 818 positions (over 20, not listed) gained at residue [7] (mod 8)
    
      SUMMARY [the degenerate moduli]: MIXED -- ['one class deleted, plus gains', 'one class deleted, survivors listed/counted'] across all 6 games
    
    ==============================================================================
    NEGATIVE CONTROL -- the comparator must report a difference that is not there
      baseline D(5,2): residue class 2 (mod 10) deleted entirely
      perturbed (A) += residue 2 (mod 10): identical P-sets
      perturbed (A) -= residue 4 (mod 10): deletions across residues [2, 4] (mod 10)
      control (i) changed the verdict : True
      control (ii) changed the verdict: True
    
    ==============================================================================
    18 games compared over n = 0..100000. Finite checks over the stated
    range only; no pattern above is a proof or is claimed beyond 100000.
    elapsed: 25.6s
"""
import sys
import time

DEPTH = 100000
LIST_LIMIT = 20

GROUPS = [
    ("r = 0, healthy",        [(7, 0), (5, 0), (3, 0), (11, 0)]),
    ("r >= 1, healthy",       [(3, 1), (5, 2), (7, 3), (11, 4), (12, 5)]),
    ("the exceptional trio",  [(9, 4), (9, 5), (9, 6)]),
    ("the degenerate moduli", [(2, 0), (2, 1), (4, 0), (4, 1), (4, 2), (4, 3)]),
]


# ---------------------------------------------------------------------------
# solvers -- P[n] = 1 iff n is a P-position under normal play
# ---------------------------------------------------------------------------

def diagonal(m, r, N):
    """(A) D(m,r): squares at n = r (mod m), fallback subtract m elsewhere."""
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


def plain(m, N):
    """(B) the plain subtraction game with move set {m}."""
    P = bytearray(N + 1)
    for n in range(N + 1):
        P[n] = 1 if n < m else (0 if P[n - m] else 1)
    return P


# ---------------------------------------------------------------------------
# reporting helpers
# ---------------------------------------------------------------------------

def residue_profile(P, N, mod):
    """(full, partial): residues all of whose positions are P, and residues
    holding some but not all."""
    tot = [0] * mod
    hit = [0] * mod
    for n in range(N + 1):
        tot[n % mod] += 1
        if P[n]:
            hit[n % mod] += 1
    full = [c for c in range(mod) if hit[c] == tot[c] and tot[c]]
    part = [c for c in range(mod) if 0 < hit[c] < tot[c]]
    return full, part


def show(positions):
    if len(positions) <= LIST_LIMIT:
        return "%d: %s" % (len(positions), positions) if positions else "0: (empty)"
    return "%d positions (over %d, not listed)" % (len(positions), LIST_LIMIT)


def classify(m, r, only_b, only_a, N):
    """Describe the observed difference. Purely a description of the data."""
    mod = 2 * m
    if not only_b and not only_a:
        return "identical P-sets"
    res_b = sorted({n % mod for n in only_b})
    res_a = sorted({n % mod for n in only_a})
    # is only_b exactly one whole residue class of (B)?
    parts = []
    if len(res_b) == 1:
        c = res_b[0]
        whole = [n for n in range(c, N + 1, mod)]
        survivors = [n for n in whole if n not in set(only_b)]
        if not survivors:
            parts.append("residue class %d (mod %d) deleted entirely" % (c, mod))
        else:
            parts.append("residue class %d (mod %d) deleted except %s"
                         % (c, mod, show(survivors)))
    elif res_b:
        parts.append("deletions across residues %s (mod %d)" % (res_b, mod))
    if only_a:
        parts.append("plus %s gained at residue%s %s (mod %d)"
                     % (show(only_a), "" if len(res_a) == 1 else "s", res_a, mod))
    return "; ".join(parts) if parts else "no difference"


def compare(m, r, N, perturb=None):
    A = diagonal(m, r, N)
    B = plain(m, N)
    if perturb is not None:
        A = bytearray(A)
        mod, res, val = perturb
        for n in range(res % mod, N + 1, mod):
            A[n] = val
    only_b = [n for n in range(N + 1) if B[n] and not A[n]]
    only_a = [n for n in range(N + 1) if A[n] and not B[n]]
    return A, B, only_b, only_a


def main():
    t0 = time.time()
    print("squares_vs_fallback.py -- (A) D(m,r) against (B) subtract-{m}, n = 0..%d"
          % DEPTH)
    print("=" * 78)
    verdicts = {}
    for gname, games in GROUPS:
        print("\n### %s" % gname)
        lines = []
        for m, r in games:
            mod = 2 * m
            A, B, only_b, only_a = compare(m, r, DEPTH)
            fb, pb = residue_profile(B, DEPTH, mod)
            fa, pa = residue_profile(A, DEPTH, mod)
            verdict = classify(m, r, only_b, only_a, DEPTH)
            lines.append(verdict)
            print("\n  D(%d,%d)   modulus 2m = %d" % (m, r, mod))
            print("    (B) %-14s full residues %s  partial %s"
                  % ("subtract-{%d}" % m, fb, pb if pb else "none"))
            print("    (A) %-14s full residues %s  partial %s"
                  % ("D(%d,%d)" % (m, r), fa, pa if pa else "none"))
            print("    P in (B) only : %s" % show(only_b))
            print("    P in (A) only : %s" % show(only_a))
            print("    symmetric diff: %s" % show(sorted(only_b + only_a)))
            print("    observed      : %s" % verdict)
        # group summary
        uniq = sorted(set(lines))
        kinds = []
        for v in lines:
            if v.startswith("identical"):
                kinds.append("identical")
            elif "deleted entirely" in v and "gained" not in v:
                kinds.append("one class deleted")
            elif "deleted except" in v and "gained" not in v:
                kinds.append("one class deleted, survivors listed/counted")
            elif "gained" in v:
                kinds.append("one class deleted, plus gains")
            else:
                kinds.append("other")
        agreed = len(set(kinds)) == 1
        print("\n  SUMMARY [%s]: %s across all %d games%s"
              % (gname, kinds[0] if agreed else "MIXED -- " + str(sorted(set(kinds))),
                 len(games), "" if agreed else ""))
        verdicts[gname] = (kinds, uniq)

    # ---------------- negative control ----------------
    print("\n" + "=" * 78)
    print("NEGATIVE CONTROL -- the comparator must report a difference that is not there")
    m, r = 5, 2
    _, _, ob0, oa0 = compare(m, r, DEPTH)
    print("  baseline D(5,2): %s" % classify(m, r, ob0, oa0, DEPTH))
    # (i) restore the deleted class into (A): comparison should now read identical
    _, _, ob1, oa1 = compare(m, r, DEPTH, perturb=(10, 2, 1))
    v1 = classify(m, r, ob1, oa1, DEPTH)
    print("  perturbed (A) += residue 2 (mod 10): %s" % v1)
    # (ii) delete a second class from (A): comparison should report two classes
    _, _, ob2, oa2 = compare(m, r, DEPTH, perturb=(10, 4, 0))
    v2 = classify(m, r, ob2, oa2, DEPTH)
    print("  perturbed (A) -= residue 4 (mod 10): %s" % v2)
    c1 = v1 != classify(m, r, ob0, oa0, DEPTH)
    c2 = v2 != classify(m, r, ob0, oa0, DEPTH)
    print("  control (i) changed the verdict : %s" % c1)
    print("  control (ii) changed the verdict: %s" % c2)

    print("\n" + "=" * 78)
    print("18 games compared over n = 0..%d. Finite checks over the stated" % DEPTH)
    print("range only; no pattern above is a proof or is claimed beyond %d." % DEPTH)
    print("elapsed: %.1fs" % (time.time() - t0))
    return 0 if (c1 and c2) else 1


if __name__ == "__main__":
    sys.exit(main())
