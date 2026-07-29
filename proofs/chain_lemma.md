# The Chain Lemma

*Human-authored. Referee-accepted and viva-passed, July 29, 2026. Examination
transcript: verification/chain_lemma_viva.md.*

**Statement.** Fix integers m ≥ 2 and r with 0 ≤ r ≤ m−1, and let c be any
residue with 0 ≤ c ≤ m−1 and c ≠ r. In D(m, r), for every position n ≥ 0 with
n ≡ c (mod m):

n is a P-position ⟺ n ≡ c (mod 2m).

**Setup and notation.** Chain c is the set {c + jm : j = 0, 1, 2, …}, i.e.
all positions ≡ c (mod m); call c + jm rung j. Two arithmetic remarks used
throughout. (i) Every rung satisfies c + jm ≡ c ≢ r (mod m), so every
position of the chain is in fallback mode: its only candidate move is
subtract-m, legal exactly when the position is ≥ m. (ii) Since n ≡ c
(mod m), the residue of n mod 2m is either c or c + m; and n = c + jm ≡ c
(mod 2m) ⟺ 2m divides jm ⟺ j is even. So the Lemma is equivalent to:
rung j is P iff j is even. The definition doing all the work: a terminal
position is P; a position is N iff at least one legal move reaches a
P-position; a position is P iff every legal move reaches an N-position, the
terminal case being this clause satisfied vacuously.

**Closure.** Let n = c + jm be a rung. Its only candidate move is
n → n − m. If j = 0, the move is illegal, since n = c ≤ m − 1 < m. If
j ≥ 1, the move is legal, since n = c + jm ≥ 0 + m = m, and it lands on
c + (j−1)m: the same residue c mod m, hence rung j − 1 of the same chain.
So every legal move from a chain-c position stays inside chain c, descending
exactly one rung, and the set of positions reachable from the chain is
contained in the chain.

**Independence.** Positions outside chain c — in particular class-r
positions firing squares — may well have moves that land on rungs of the
chain. This cannot disturb the rungs' statuses: by the definition just
quoted, the status of a position is a function only of the statuses of its
options, the positions reachable from it; the definition never mentions
moves arriving at a position. By Closure, every option of every rung is
again a rung, so the statuses of chain c are computed entirely within chain
c and would be identical if the rest of D(m, r) were deleted. Incoming
traffic affects only the travellers, never the rungs.

**The bottom.** Rung 0 is the position c, the least element of the chain,
with 0 ≤ c ≤ m−1. It is in fallback mode (because c ≢ r) and its single
candidate move is illegal (because c < m). Both facts hold equally for
c = 0 and for c ≥ 1 — note that for c = 0 no appeal to squares is needed:
0 ≠ r already puts the position 0 in fallback mode, where m ≤ 0 fails. So
rung 0 is terminal, hence a P-position: "every legal move reaches an N"
holds vacuously. This matches the claim, since j = 0 is even.

**Alternation.** Claim: rung j is P for even j and N for odd j. Strong
induction on j. Base, j = 0: done above. Step, j ≥ 1: assume the claim for
all smaller indices. By Closure, rung j has exactly one legal move — legal
precisely because j ≥ 1, the boundary check (rung 0 has no move at all;
rung 1's move is legal since c + m ≥ m) — and it goes to rung j − 1. For a
position with a single option x, the definition specializes: "some option
is P" means x is P, so the position is N iff x is P; "every option is N"
means x is N, so the position is P iff x is N. By the induction hypothesis,
rung j − 1 is P iff j − 1 is even. Hence rung j is N iff j − 1 is even,
i.e. iff j is odd; and rung j is P iff j − 1 is odd, i.e. iff j is even.
Induction closed.

**Assembly.** Let c ≢ r be any class and n ≡ c (mod m) any position; write
n = c + jm with j ≥ 0 uniquely determined. Closure and Independence license
computing n's status inside the chain alone; the bottom is the base of the
induction and Alternation is its step, giving: n is P ⟺ j is even ⟺
jm ≡ 0 (mod 2m) ⟺ n ≡ c (mod 2m). Nothing about c was used beyond
0 ≤ c ≤ m−1 and c ≠ r, so the result holds for all m − 1 such classes
simultaneously. ∎

**Scope.** The Lemma classifies no position of class r itself — it is
silent about every n ≡ r (mod m), and in particular does not assert those
are N-positions; that claim is Milestone 2, and only the two together give
the full mod-2m law.

## Closing remarks: checks and observations

Workbook, D(5,2), n = 0…24, from the raw definition: P at 0, 1, 3, 4, 10,
11, 13, 14, 20, 21, 23, 24; N everywhere else — exactly residues 0, 1, 3, 4
(mod 10), with class 2 (n ≡ 2, 7 mod 10) all N so far. The decoding in the
brief checks out. Also verified mechanically to n = 400: no violations of
the Lemma in (5,2), (3,1), (7,3), (2,1), or (4,1) for any class c ≠ r.

The one honest observation about the diseased pages: the chains stay
healthy even where the game is sick. In D(2,1) and D(4,1) every non-r chain
alternates exactly as the Lemma predicts; what breaks is class r, which
grows P-positions of its own — first at n = 3 in (2,1) and n = 5 in (4,1)
(then 11, 23, … and 13, 37, …). So the disease lives entirely in Milestone
2, not in this page — consistent with the fact that the proof above never
once mentions squares.
