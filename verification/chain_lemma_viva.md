# Viva Transcript: The Chain Lemma

Oral-style examination conducted in the project's supervision channel,
July 29, 2026, prior to formal acceptance of proofs/chain_lemma.md. Three
fresh questions (transfer, perturbation, bridge), answered live by the
author in their own words. Questions by the AI referee; answers reproduced
verbatim. Verdict: all three correct; lemma formally accepted.

---

**V1 (transfer).** In D(6, 4), take chain 1. List its P-positions among
n ≤ 30, name the bottom, say in one sentence why the bottom is terminal,
and give the final mod-12 description of the chain's P-set.

**Answer.** Chain 1 is 1, 7, 13, 19, 25 (next rung is 31, past 30).
Climbing from the bottom: 1 is stuck so it's P; 7 can drop to 1, so N; 13's
only move is down to 7, which is N, so 13 is P; 19 drops to 13 (P), so N;
25's only move is 19 (N), so P. So the P-positions in this chain up to 30
are 1, 13, 25. The bottom of the chain is 1. It has no legal move because 1
isn't in class 4 (1 ≡ 1 mod 6), so squares mode is off, and the fallback
move of subtracting 6 would push it below zero. Closing line: P exactly
when n ≡ 1 (mod 12).

---

**V2 (perturbation).** Keep everything the same but change the fallback
move from subtract-m to subtract-2m. (a) Which parts of your page survive
with content unchanged? (b) What is the new set of terminal rungs of chain
c, and the new P-pattern in j?

**Answer.** (a) Going section by section: everything on the definitions
part survives untouched — P means all moves land on N, N means some move
reaches a P, and a position with no moves at all is automatically P. None
of those sentences ever used the number m. The chain decomposition also
survives, because the only thing it needed was that the fallback move is a
multiple of m, so it can't change your class — and 2m is still a multiple
of m. So the game still splits into separate chains and class r is still
the only one with squares. What does not survive is every sentence that
used the amount being exactly m: "only the bottom is stuck," "each rung
sees the rung directly below it," "P and N alternate," "period 2m."
(b) Now a rung is terminal when it's less than 2m, so each chain has two
dead rungs at the bottom, b and b+m, both P. Each rung above only sees the
rung two below it, so the chain really splits into two interleaved ladders
(even rungs and odd rungs), each alternating like the old chain did. Going
up you get P, P, N, N, P, P, N, N, ... — in mod language, P exactly when
n ≡ b or b+m (mod 4m). (And the class-r checks would all need redoing,
since they leaned on where the P's used to sit.)

---

**V3 (bridge).** Point to one row of your own D(5,2) table with n ≥ 13 in
class 2, and using only that row's move list, explain why that single row
is a preview of what Milestone 2 must prove in general.

**Answer.** Row 17's move list reads 17−1=16 (N), 17−4=13 (P), 17−9=8 (N),
17−16=1 (P): the row shows that a class-2 number doesn't need all its
square moves to be good — it just needs one square that lands on a P-rung
of some fallback chain, and 17 actually has two. That's exactly Milestone 2
in miniature: the general claim is that every n ≡ 2 (mod 5), no matter how
large, always has at least one subtractable square landing on a P-rung (a
number matching a chain bottom mod 10), which forces the whole class to
be N.

---

**Referee notes.** V1: correct throughout, including the two-premise bottom
argument. V2: correct, and part (b) is an original mini-result — with
fallback 2m each chain has two terminal rungs and splits into interleaved
alternating ladders, P exactly at n ≡ b or b + m (mod 4m); the natural
generalization (fallback km: k dead rungs, period 2km) is recorded here as
a candidate remark for the paper. V3: correct in shape; the general proof
must additionally carry the legality condition k² ≤ n explicitly, which is
the source of small-n rebels and preperiods (noted for Milestone 2).
