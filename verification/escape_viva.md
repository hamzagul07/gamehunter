# Viva Transcript: The Escape Theorem and the Diagonal Program

Oral-style examination conducted in the project's supervision channel,
July 29, 2026, prior to formal acceptance of the Escape/Diagonal material.
Questions by the AI referee; answers reproduced verbatim from the author.
Verdict: all three correct; Milestones 2 and 3 cleared.

Procedural note: an earlier viva round (a D(7,3) keystone computation and a
"useless square" question) was superseded — the author's Part E submission
answered both in generalized form (the Q(14) analysis with 8 ∈ H(7, r) for
every r, and the proof that square values ≡ 0, 1, or m (mod 2m) are
constitutionally useless to the hard residue), and the referee accepted
that document as absorbing those questions. Its third question was carried
into this round as Q3.

---

**Q1 (the false instance).** The general theorem, as assembled, has exactly
one false instance across the entire healthy family. Find the exceptional
position, say why it breaks the clean law, and restate the theorem so it is
true — one added clause suffices.

**Answer.** It's n = 0, and it lives in every game with r = 0 — the one
parameter value the workbook never opened. For r ≥ 1 zero is a foreign
bottom, filed P by the Chain Lemma, and the law agrees. But when r = 0,
zero gets claimed by squares mode (0 ≡ 0 mod m), and it's the unique
squares-mode position that can't afford any square: k ≥ 1 forces
k² ≥ 1 > 0. So it's terminal, hence P — while the clean law, whose window
is now {1, ..., m−1}, declares residue 0 to be N. The proof's hidden
assumption was that every squares-mode position has a move, which is true
from n = 1 up because 1² is always affordable; 0 is the lone
counterexample, the one position where "terminal ⇒ P" and "class r ⇒ N"
collide. And it breaks nothing else: n = m escapes by 1² to the bottom
m−1, n = 2m escapes by (m−1)² or a spare — spot-checked 10 in D(5,0),
where −9 lands on 1 (P), and 14 in D(7,0), where −9 lands on 5 (P) —
fallback chains never visit class 0, and any n = k² that can drop to 0 was
already N by the law, so zero's P-ness corrupts nobody. Restatement, one
clause added: n is P if and only if n ≡ a foreign bottom (mod 2m), or
n = 0. For r ≥ 1 the clause is absorbed, since 0 is itself a foreign
bottom; it earns its keep exactly at r = 0.

---

**Q2 (calibration).** Two sentences, one each: "For m = 2 and m = 4, we
prove that…" and "We do not prove that…" — phrased as they would appear in
the paper.

**Answer.** For m = 2 and m = 4, we prove that the hard residue class is
confined: Q(2m) ⊆ {0, 1, m} while every hard set excludes those three
values, so no square move from the hard class reaches the target window —
every move stays inside class r or falls on an N-rung — and its P/N
structure is therefore decided by a self-contained internal game, which
the recorded witnesses 3 and 5 show already violates the chain law. We do
not prove that these confined classes obey no eventual law of their own:
"no period and no modulus up to 200 fits" is a reading from the search
instrument, not a theorem, and their aperiodicity remains open. (The
inward turn is now drafted as its own two-line Confinement Lemma, mirror
image of the Independence section, as ordered.)

---

**Q3 (carried over: the non-coincidence).** The P-set of D(5,2) equalling
the target window T is not a coincidence. One sentence: what is it?

**Answer.** The equality is the theorem wearing a disguise: the game's
P-set is (chain P's) ∪ (class-r P's), the window T was defined to be
exactly the first set, and Escape is precisely the assertion that the
second is empty — so P-set = T ∪ ∅ = T by construction, and the equality
fails exactly where escape does, which is why the diseased games' P-sets
properly contain their windows.

---

**Referee notes.** Q1: independently verified, including both spot-checks;
the boundary clause absorbs invisibly for r ≥ 1 — model boundary work. The
answer also surfaced that the below-threshold zone at the hard residue is
genuinely nonempty for m ≥ 5 (the main witness (m−1)² is illegal at
n = 2m), so the general write-up must state and account for that finite
zone. Q2: confinement stress-tested concretely at both diseased games;
sentences accepted as paper-ready. Q3: correct, and the formulation
automatically houses both deviations (diseased games: P ⊋ T; the r = 0
clause: P = T ∪ {0}). Retrodiction on record: the disease fingerprints
recorded during the Chain Lemma checks (3, 11, 23 in D(2,1); 5, 13, 37 in
D(4,1)) fall exactly on the hard residues the confinement mechanism
predicts (≡ 3 mod 4 and ≡ 5 mod 8 respectively) — coordinates recorded
before the mechanism existed.
