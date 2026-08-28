# GameHunter: Machine-Guided Discovery in Mode-Switching Subtraction Games

**Note (added August 2026).** This report describes the project through 30
July 2026, and its statements about the division of labor were accurate on
that date. The division changed during the August 2026 extension of the paper;
see the August 2026 addendum at the end of this file. Nothing below has been
rewritten — a record edited to match a later conclusion is not a record.

**Project report — July 29, 2026.**
Compiled by the project's AI collaborator (Claude) at the student's request.
Status: active research. Nothing in this report has yet received external
human review; see Limitations.

## 1. Summary

A student researcher in Rawalpindi, working with an AI collaborator, built an
automated conjecture-discovery system for a family of invented combinatorial
games, ran a census of roughly three thousand such games, proved two of the
system's conjectures by hand, and used the census data to formulate a general
law — confirmed by a preregistered out-of-sample prediction — that is now the
target of a proof program. The proved results are small but genuinely new;
the validated general conjecture, if proved, would characterize the winning
positions of infinitely many games at once. Equally important is the working
method: a strict division of labor in which machines propose and verify data
while every mathematical claim is proved, in plain language, by the human.

## 2. Background and strategy

The project began from a structural observation about novelty. In
long-studied areas of mathematics, a newcomer competes with centuries of
prior work. In *invented* territory the situation reverses: define a new
object, and every true statement about it is automatically new to human
knowledge. Combinatorial games make this concrete. An impartial subtraction
game is specified by a rule for which amounts may be subtracted from a pile;
Sprague-Grundy theory assigns every position a value computable by machine,
and the positions of value zero (P-positions, where the player to move
loses) are the game's solution. The project's chosen family is
**mode-switching subtraction games**: the legal move set depends on the pile
size modulo m — for example, "if n ≡ 1 (mod 4) subtract any square,
otherwise subtract 3, 8, or 9." No dedicated study of this family was found
in an initial search of the literature; a fuller literature scan is on the
roadmap.

## 3. The instrument

GameHunter is a single-file, dependency-free Python system. Its architecture
follows the proposer/verifier pattern of modern discovery systems (Graffiti's
conjecture heuristics; the Ramanujan Machine's generate-then-validate
pipeline; DeepMind's FunSearch and AlphaEvolve, which pair a creative
proposer with a deterministic evaluator). Concretely: a small rule language
(DSL) describes games; an evolutionary proposer mutates rules; a Grundy
engine computes exact values; deterministic detectors search for structure
(eventual periodicity, arithmetic periodicity, modular and digit-sum
characterizations of P-positions); an OEIS filter discards already-known
sequences; an interestingness score drives selection. A "demo" mode
re-derives five classical results (for example, the subtract-{1,2,3} game's
period 4, and the subtract-a-square game's chaotic values matching OEIS
A030193) and is run before and after every session as a regression test.

Around the instrument sits a written integrity protocol, stored in the
repository itself: analysis agents may build tooling but may never verify a
conjecture, reword a law, tune thresholds to flatter results, or write
mathematical content into the human-only proofs directory. All hunts are
seeded and logged; every artifact is committed to version control with
timestamps.

## 4. The process, in depth

One full research cycle, as actually executed. Five seeded evolutionary
hunts produced forty finalist games; filtering by structure tier and OEIS
novelty left fifteen candidates, each re-verified at 20,000 positions. The
student selected one — nicknamed **Foursquare**: subtract any square when
n ≡ 1 (mod 4), otherwise subtract 3, 8, or 9 — hand-checked the machine's
conjecture at small n, and then proved it by strong induction. The AI
collaborator refereed the proof line by line and re-verified the theorem
with an independent re-implementation to n = 1,000,000. A second theorem
followed from a data anomaly: all odd single-value fallbacks at m = 2
produce literally identical games, proved via two lemmas whose key idea is
that the fallback parameter's influence is quarantined away from the Grundy
recursion.

The census phase then scaled the instrument: 1,120 games in a first sweep,
1,848 in an extended sweep over m = 2..12, yielding 842 detected laws, every
one reproduced verbatim at 20,000 positions. Verification was deliberately
adversarial: sampled and complete subfamilies were re-tested to one million
positions using a separate win/loss-only code path; a wide-modulus rescan
(ceiling raised to 200) reclassified only 6 of 731 "chaotic" games,
establishing that the family's split into lawful and lawless games is real
rather than an instrument artifact. Across six independent verification
passes, no detected law has ever failed — itself now a research question.

From pivot tables of this data the student wrote ten raw observations,
translated the strongest into a mechanism (each non-special residue class
runs an independent descending chain), and stated a conjecture: on the
diagonal a = m, the emergent modulus is 2m with exactly m−1 residues. The
decisive test was **preregistered**: before the extended sweep ran, the
student recorded the prediction that cell (11,11) would show modulus 22. It
did — along with every other new diagonal cell, at modulus 2m and residue
count m−1 throughout. Two cells, (2,2) and (4,4), are lawless exceptions and
are now study objects rather than embarrassments.

## 5. Results to date

Proved (pending external review): the Foursquare theorem — its P-positions
are exactly n ≡ 0, 2, 4, 6 (mod 16) for all n ≥ 0, with no preperiod,
sharpening the machine's own conjecture; and the odd-fallback collapse
theorem at m = 2. Validated but **not proved**: the Diagonal Law above.
Robust empirical findings: a genuine modular/chaotic dichotomy across the
family; a stark branch-order asymmetry (laws are abundant when squares fire
on one residue class and essentially absent beyond m = 2 when squares govern
all but one class, consistent with the known aperiodicity of the
subtract-a-square game); a boundary phenomenon at fallbacks that are proper
multiples of m; and exact minimal-preperiod data, previously invisible to
the instrument.

## 6. A methodological finding about AI and proofs

The project's scoreboard on proof authorship is stark. Proofs drafted in the
student's plain language: two submitted, two accepted under line-by-line
review. Proof texts produced or styled by AI fluency: three submitted, three
rejected, each with a fatal flaw at a load-bearing step hidden under
confident technical vocabulary. The working rule that emerged — every
sentence in a proof must survive having its terms replaced by their
definitions — proved more valuable than any tooling. The machine's proper
role stabilized as: propose candidates, compute exhaustively, verify
mechanically, referee skeptically. The human's role: choose questions, stare
at data, conjecture, and own every line of every proof.

## 7. Why this matters

For mathematics: the family itself is a contribution-in-progress —
thousands of concrete new games, one exactly solved, an infinite subfamily
under a single validated law, and open questions (the parameter-to-modulus
map, the lawful/lawless criterion, and whether a law that holds on a long
window must persist forever) that connect to live threads in the field. The
project sits one abstraction away from Problem A1 of the community's current
unsolved-problems list — the relationship between subtraction rules and
period structure — and adjacent to the 2024 survey literature on finite
subtraction games. The instrument and all data are reproducible from seeds.

For students and the wider public: the project is a working demonstration
that genuine mathematical research — not simulated, not pay-to-publish — is
accessible to a determined student with a laptop, if novelty is engineered
structurally and verification is taken seriously. Its honesty protocol
(agent firewalls, regression trust checks, preregistered predictions,
human-only proofs, timestamped provenance) is a transferable template for
doing research *with* AI without letting AI hollow it out. And Foursquare
itself is a classroom-ready object: the rules mention only 4 and squares,
yet 16 emerges — because odd squares are 1 or 9 modulo 16 — a
one-whiteboard "why?" with a classical answer.

## 8. Limitations, stated plainly

The proved theorems are small — exercise-level once the conjecture is in
hand; their value lies in being new and in seeding the general program. The
Diagonal Law is a conjecture: a preregistered confirmation is evidence, not
proof. Every verification so far is internal — the student's proofs were
refereed by the same AI ecosystem that built the instrument, and
computational checks, however adversarial, cover finite ranges of infinite
claims. External human review is therefore the single most important
missing ingredient, and no result should be considered established until it
has one. Detector ceilings (modulus and preperiod bounds) mean "lawless"
formally means "no law within instrument reach."

## 9. Future aims and what is still needed

The proof program: first the Chain Lemma (each non-special class alternates
with period 2m — currently assigned), then the Escape Crux (the special
class always has a square move to a chain's losing phase, which is where
quadratic-residue theory enters), then the lawless cells (2,2) and (4,4) as
corollaries of the escape criterion, assembling into the Diagonal Theorem.
Alongside it: the entry-13 proof as a second solved case; completion of the
proofs directory (both files are, at this writing, still placeholders — the
accepted proofs exist only in conversation logs and must be typed and
pushed); a proper literature scan, including the modular-Nim thread and the
finite-subtraction survey, to position novelty honestly; external
mathematician review, with an optional machine-checked (Lean) formalization
as a reviewer-independent verification path; an OEIS submission of the
Foursquare Grundy sequence after review; and finally a written paper —
census, theorem, solved cases, open questions — for an appropriate venue
(an arXiv preprint with endorsement; journals such as Integers, which
publishes combinatorial games, as a realistic target; student venues as a
fallback). Engine extensions (two-pile games, misère play, automated
base-k proofs via Walnut) are deliberately queued behind the mathematics.

## 10. Provenance and roles

The student: all strategic decisions, all operations execution, all
hand-verification, the ten observations, the chain mechanism, Conjecture 1
and its preregistered prediction, and both accepted proofs. The AI
collaborator (chat): engine authorship, referee reviews, independent
verifications, operations design, and coaching. The AI agent (editor
environment): executed operations under the written firewall and flagged
anomalies, several of which became research questions. This document is
project documentation, compiled by the AI collaborator; it is source
material, and any personal statement, essay, or submission derived from it
must be written by the student in their own words.

**Amendment (July 29):** A second AI system (Google's Gemini) was also used
at points in this project, primarily for drafting and formatting. Several
proof documents produced with its involvement were rejected at review for
errors at load-bearing steps; one later re-derivation of the collapse
theorem, produced from the referee's full specification, was verified
correct and is retained in the repository as an independent cross-check
(verification/collapse_independent_check.md). All accepted mathematics in
the proofs/ directory remains human-authored.

**Amendment (July 30):** The Diagonal Law reported in §5 as "validated but
**not proved**" is now a theorem. The student proved: for every m ≥ 3
except m = 4 and every r, the P-positions of D(m, r) are exactly the
foreign-bottom residues modulo 2m, together with an explicitly determined
exception set — n = 0 when r = 0, plus one extra P-position n = m + r in
each of the three games (9,4), (9,5), (9,6) — covering both parities of m
with no thresholds and no unverified zones. The proof route replaced the
original odd-m witness identity with a parity-free Clearing Lemma; the
diseased moduli m = 2 and m = 4 are excluded by a Confinement Lemma and
independently condemned by the failure-window analysis. Two retrodictions
are on record: the confinement fingerprints, and the D(9,4) preperiod-14
ledger line, every number of which the mechanism now derives with zero
freedom. The sole remaining open question in the program is the
aperiodicity of the two confined classes. Full text:
proofs/escape_and_diagonal.md; examination records:
verification/escape_viva.md and verification/diagonal_viva.md. External
human review remains pending for all results.

**Amendment (August 1):** First external human review received. Balaji
Kadam (postdoc, IIT Bombay, group of U. Larsson) read the Foursquare
proof; no errors were reported; he suggested a streamlined presentation
via the standard verification principle (being adopted) and conjectured
an extension of the move set leaving the P-positions invariant. The
student proved the conjecture (verbatim proof in correspondence;
machine-checked to n = 30{,}000 in
verification/kadam_extension_check.py) and it will appear as a credited
remark. The Foursquare result and proof were also posted publicly on the
Art of Problem Solving forum for independent checking.

## August 2026 addendum: a change in the division of labor

Everything above describes the project through 30 July 2026, when the division
was as stated: the instrument proposed and verified, and the author wrote
every proof. In August 2026 the paper was substantially extended — from
nineteen pages to thirty-two, with six new or rebuilt sections — and during
that work the division changed. This addendum records the change. The sections
above are left as originally written.

### What changed

The theory added in August was developed in extended dialogue with Claude
(Anthropic), which drafted the statements and the proof texts. The author set
the direction and the architecture, refereed every draft, corrected what was
wrong, verified every numerical claim against the instrument, and takes sole
responsibility for the correctness of the paper. No mathematics was accepted
on an AI's assertion; every claim that entered the paper was either proved and
refereed or checked against a machine record.

### Ledger

Drafted in dialogue and installed after refereeing:

- Corollary 3.2 (Chain Lemma, Grundy form) and the bottom / top-rung terminology
- Section 4 in its entirety — Definition 4.1 (the two residues, the hard set, s_min) through Proposition 4.9
- Theorem 5.1, Corollary 5.2, Remark 5.3, and one clause of Remark 5.4
- Section 6 in its entirety — Lemma 6.1, Theorem 6.2 (the Transfer Principle), Remarks 6.3 to 6.5
- Section 8 in its entirety — Definition 8.1 through Corollary 8.6, including Table 2 and its caption
- Section 9 in its entirety — Definition 9.1 through Remark 9.9
- Section 10 in its entirety — Lemma 10.1 through Remark 10.7
- Remark 7.4's closing sentence; Remark 11.3; the proof of Proposition 11.7; the body of Remark 11.8; the reverse-direction paragraph of Section 12; the closing paragraph of Section 13
- The abstract and Section 1
- Editorial: the Section 7 vocabulary and register revisions, the h* renaming, and the Section 11 cross-reference repairs

The author's own, unchanged: Sections 2 and 3 (Lemma 3.1), Section 7, Sections
11 through 13 apart from the items listed above, the search instrument, and
every verification run in this repository.

### What the firewall covered, and what it did not

`proofs/` was read-only throughout the August work and no AI-drafted
mathematics was written into it; the statement above that the `proofs/`
directory contains human-authored mathematics only remains true. The firewall
governed the repository. It did not govern the dialogue, and the paper's
disclosure now says so — which is the substance of the correction this
addendum records.

### Corrections ran in both directions

The record is not one-sided, and both directions are worth keeping. The
dialogue caught errors the author's machine sweeps had missed — the base-point
clause of Theorem 9.5 exists because a proof found what a base-blind sweep
could not, and a converse gap in Proposition 11.7 that had stood since July
was closed. The author's machine records caught errors in the drafting: a
claim of "no mismatches" written for Section 12 was refuted by a recorded
ledger of 77 disagreements, which on recomputation turned out to be exactly
the excluded prefixes and now appears in the paper in that corrected form; an
occurrence audit that reported eleven instances was found by relocation to
have missed ten more; and a bibliographic attribution in the draft was wrong
and was corrected against the source. Neither party's output was accepted
without the other's check, and the paper's claims stand on the checks rather
than on either party's authority.
