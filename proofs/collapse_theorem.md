# The Odd-Fallback Collapse Theorem (m = 2 Family)
*Human-authored; referee-accepted July 29, 2026, with two referee-dictated
corrections incorporated. Examination record and independent cross-check:
see verification/.*

**Setup.** We fix r = 1: squares fire on odd n, and the fallback rule
applies on even n, making the allowed move from n to n − a. Let G(n) denote
the Grundy value of state n, with G(0) = 0.

## Lemma A (P-positions = Even Numbers)

**Theorem.** For every odd integer a ≥ 1, the set of P-positions (states n
with G(n) = 0) consists precisely of all even integers. Consequently, the
emergent period is 2 with a residue-set size of 1.

**Proof.** We proceed by induction on n.

**Base case (n = 0).** Terminal position, G(0) = 0, so 0 is a P-position.

**Inductive step.** Assume for all k < n that G(k) = 0 ⟺ k is even
(equivalently, G(k) > 0 ⟺ k is odd).

**Case 1: n is even.** The only available move is subtraction of the odd
fallback a: n → n − a. Since n is even and a is odd, the destination n − a
is strictly odd. By the induction hypothesis, G(n − a) ≠ 0 (if n − a ≥ 0),
or the move set is empty (if a > n).

- If a > n: the move set is ∅, so mex(∅) = 0 and G(n) = 0.
- If a ≤ n: the set of reachable values is {G(n − a)} with G(n − a) ≠ 0,
  so mex({G(n − a)}) = 0 and G(n) = 0.

In both cases G(n) = 0. Thus all even positions are P-positions.

**Case 2: n is odd.** The move set consists of square subtractions
n → n − k² for all integers k ≥ 1 with k² ≤ n. Choosing k = 1 gives a legal
move to n − 1. Since n is odd, n − 1 is even, so G(n − 1) = 0 by the strong
induction hypothesis. Thus 0 ∈ {G(n − k²) : k² ≤ n}, forcing the mex to be
positive, so G(n) ≠ 0.

Therefore G(n) = 0 ⟺ n ≡ 0 (mod 2). ∎

## Lemma B (Full Sequence Equivalence)

**Theorem.** For all odd fallbacks a, a′ ≥ 1 and all states n ≥ 0, the
Grundy values satisfy G_a(n) = G_{a′}(n).

**Answers to the Referee Questions.**

**Question 1 (even positions).** What is mex({v}) when v ≠ 0, and what does
that force G(n) to be for even n?

For even n, the reachable set is either empty (if n < a) or {G(n − a)}. By
Lemma A, since n − a is odd, G(n − a) = v > 0. Now mex(∅) = 0, and
mex({v}) = 0 whenever v > 0. Therefore G(n) = 0 for every even n,
regardless of the specific value of v, and regardless of whether the move
exists at all. The parameter a evaporates at every even step.

**Question 2 (odd positions).** At odd n, split the available squares k² by
parity: which earlier positions' Grundy values enter the mex?

For odd n: if k is even, k² is even, so n − k² is odd; if k is odd, k² is
odd, so n − k² is even. By Lemma A, for every odd k the landing n − k² is
even with G(n − k²) = 0. Thus the reachable Grundy values from odd n are
{0} ∪ {G(n − k²) : k even, k² ≤ n}. The value 0 is guaranteed by the odd
square moves (k = 1, 3, 5, …), and the non-zero entries depend exclusively
on G(n − k²) for even k — landings on smaller odd numbers. So G at odd n is
computed purely from earlier odd states, completely bypassing all even
positions, and thus bypassing a entirely.

By induction on n: G(0) = 0; every even state yields G = 0 independent of
a; and every odd state's value is computed from prior odd states via
even-square subtractions, in which a nowhere appears. The parameter a never
impacts the Grundy sequence, so all odd fallbacks collapse to the exact
same game. ∎