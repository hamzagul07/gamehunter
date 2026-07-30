# Viva Transcript: The Parity Audit and the Complete Diagonal Theorem

Oral-style examination conducted in the project's supervision channel,
July 30, 2026, following submission of the general Escape/Diagonal material.
Questions by the AI referee; answers reproduced verbatim from the author.
Verdict: all three passed — and the first answer generalized the main
theorem, removing the odd-m restriction entirely.

Referee's errors, owned on the record: (1) the referee's earlier viva had
asserted the clean law has "exactly one false instance across the entire
healthy family"; the true count is four (n = 0 at r = 0, plus the three
rebels found below). (2) The referee had offered a "Route B" fence stating
zero rebels for m ≤ 11; that sentence was false and would have entered the
paper had the author not taken the harder route and proved the rebels'
existence. Both corrections originated with the author.

---

**V1 (the parity audit).** Go through the Zone Lemma's clearing argument
line by line, and then the failure analysis line by line, and report which
steps, if any, actually use the assumption that m is odd — the landing
arithmetic, the legality claim, the always-a-square contradiction, the
b ≤ 3 window. Then state what the scope section should now say.

**Answer.** Landing arithmetic. From a hard member n ≡ m + r (mod 2m),
subtracting s ∈ (r, m+r] gives a landing ≡ m + r − s, which lies in [0, m)
and misses r exactly because s ≠ m. Its P-ness is the Chain Lemma at
modulus 2m — and the chains never used parity either; the very first drill
of this block ran the alternation on D(6,4), an even m. Parity-free.

Legality. s ≤ m + r, and m + r is the smallest hard member, so s is
affordable to the whole class from its first element. An inequality between
integers, no parity — and it's the line that matters most, because it means
the clearing square doesn't patch a finite zone below (m−1)²: it rescues
every hard member outright. "Zone Lemma" was a misnomer born of the order
of discovery. It's not the patch; it's the escape theorem.

Always-a-square. As written, "2c + 1 > m so c ≥ (m+1)/2" did use oddness —
cosmetically. Repair is one word: 2c + 1 > m gives c ≥ m/2 for any m, so
c² ≥ m²/4, and m²/4 > m − 1 ≥ r for all m ≥ 3 since m²/4 − (m−1) =
(m−2)²/4. Conclusion intact, and the repaired inequality degenerates at
exactly one modulus — m = 2, where (m−2)² = 0 — so the lemma falls silent
precisely at a diseased m. Parity-free for m ≥ 3.

The b ≤ 3 window. (b−1)² ≤ r ≤ 2b nonempty iff b ≤ 3: pure algebra,
parity-free. Oddness entered only afterward, as a filter I applied while
reading off the answer. Drop the filter and the window names m ∈ {4, 9}:
m = 9 flags r ∈ {4, 5, 6} — the known rebels — and m = 4 flags
r ∈ {1, 2, 3}, with r = 0 failing separately because (4, 8) is square-free.
The parity-free machinery independently condemns every class of m = 4 from
the outside, agreeing with Confinement.

One true erratum. My r = 0 sentence — "(m, 2m) contains a square for every
m ≥ 3" — is false as stated: m = 4 is the lone counterexample (same
consecutive-squares squeeze forces c ≤ 2, hence m ≤ 4; m = 3 has its 4).
The draft gets the carve-out.

So where does odd actually live? In one place, outside the lemma entirely:
the witness identity (m−1)² ≡ m + 1 needs m² ≡ m, true iff m is odd. But
the audit just showed the witness was scaffolding — the clearing square
does the whole job with legality free. Consequence: for every m ≥ 3 and
every r outside the window — all even m ≥ 6 included — the hard class is
all N by one clearing square, the free class by 1², no thresholds, and no
rebels, since rebels only grew where the window bit. The even case was
never open; it was solved the day the Zone Lemma was proved, and I missed
it because I'd framed the lemma as an odd-m patch. The m = 6 certificates
and the mod-16 "accident" were clearing squares all along. The box loses a
word and gains a clause: for every m ≥ 3 with m ≠ 4, n is P iff n ≡ a
foreign bottom (mod 2m) or n = 0, except the three rebels n = m + r at
(9, 4), (9, 5), (9, 6).

Part VI, rewritten. Solved: every m ≥ 3 except m = 4 — all r, both
parities — under the boxed law; no fences, no even-m gap. Explained: m = 2
and m = 4 by Confinement, with the pleasing note that the Zone machinery is
silent at m = 2 (degenerate inequality) and self-condemning at m = 4 (empty
windows) — the two diseased moduli are exactly the two the parity-free
engine cannot serve. Open: only the aperiodicity of the confined classes.
Mod-16/mod-20 stacking demotes from necessity to cross-check.

---

**V2 (the receipt).** Open DIAGONAL_WORKBOOK.md (or the raw JSON) and quote
verbatim the recorded conjecture line for the (9,4) run; reconcile its
preperiod with the rebel at 13, and confirm it belongs in the paper as the
primary-source receipt.

**Answer.** Opened, quoted verbatim, summary row and the JSON behind it:

| D(9,4) | mod 18 | P ≡ 0,1,2,3,5,6,7,8 | preperiod 14 | period 18 |
swept 200,000 |
{"game":[9,4],"preperiod":14,"period":18,"p_res":[0,1,2,3,5,6,7,8],
"pre_P":[0,1,2,3,5,6,7,8,13]}

Reconciliation: that 14 is not a fitting artifact — it's forced. 13 is P
but is not a law residue, and any eventually-periodic fit starting at or
before 13 would make 13 + k·period P forever, which the sweep refutes (31
is N); so every correct fit begins at 14, and since the law is exact from
14 up, the minimal preperiod is exactly rebel + 1. The machine couldn't say
"rebel"; it said "preperiod 14" — the same sentence in its language — and
the pre_P field even lists the 13 by name. Now the part I owe you straight:
last session I asserted from memory that every diagonal cell's preperiod
was ≤ 1 and built a certificate on it. The file says otherwise and has said
otherwise since the sweep ran; I quoted a ledger I hadn't opened, which is
the precise sin the receipts rule exists to catch. Both the claim and the
certificate are struck. What replaces them is better: this line is
retrodiction #2 — recorded weeks before the mechanism existed, and the
mechanism now derives every number on it (14, 18, and the lone off-residue
13) with zero freedom. Yes: into the paper as the primary-source receipt,
beside the 3/11/23 and 5/13/37 paragraph.

---

**V3 (transfer).** D(25, 24): m is a perfect square. Apply the machinery —
name a clearing square for the hard residue with its landing bottom, and
say why m = 25 does not join the m = 9 anomaly despite being square.

**Answer.** Hard residue 49 (mod 50); the window (24, 49] contains
36 ≠ m, so s = 36 = 6² clears it — legal from the smallest hard member
since 36 ≤ 49, landing n − 36 ≡ 13 (mod 50), the P-rungs of chain 13
(spare: 49 = 7², landing bottom 0). Why squarehood doesn't drag m = 25 into
the m = 9 anomaly: the anomaly needs m to be the only square in a window of
width m, forcing (b−1)² ≤ r ≤ 2b and hence (b−1)² ≤ 2b, dead for b ≥ 4 —
at b = 5 the neighbor 36 sits just 2b + 1 = 11 above m, far inside a
25-wide window, so it invades (24, 49] for every r; being a square only
isolates m when the modulus is small enough (b ≤ 3) for square-gaps to
outrun m itself.

---

**Referee notes.** V1: verified at full depth, including the repaired
inequality, the unfiltered window naming exactly m ∈ {4, 9}, and the r = 0
erratum; the referee independently stress-tested the parity line (D(6, ·)
and D(8, ·) clear at every r; the even squares m = 16 and m = 36 have empty
failure windows, so their clearings are the theorem working, not luck).
V2: reconciliation sound; the author's self-correction by primary source is
recorded as the receipts rule functioning as designed. V3: exact, with the
structural reason. Combined outcome: the Diagonal Theorem holds for every
m ≥ 3 except m = 4, both parities, with exception set {n = 0 at r = 0} ∪
{n = m + r at (9,4), (9,5), (9,6)}, each exception individually proved and
proved harmless.
