# Register audit of `paper/main.tex` (report only)

Produced 2026-09-05. `paper/main.tex` was read and not modified; this file
is the whole output. Nothing here is a proof claim or a mathematical
judgement -- it is a register survey to support a plain-language revision,
and every entry is a candidate for the author to accept or reject.

## Method and its limits

Sentences were segmented from the LaTeX source between `\begin{abstract}`
and `\begin{thebibliography}`. Comments, tables, the bibliography and the
literal `alltt` block were excluded. Inline and display mathematics were
collapsed to a single token `MATH`, and `\ref`/`\cite`/`\url` to `REF`;
both count as one word each in the word counts below, so a sentence heavy
in symbols scores lower here than it reads on the page. Headings, blank
lines and theorem-environment boundaries were treated as hard sentence
breaks. 708 sentences were extracted. Two segmentation faults were found
and fixed during construction (sentences merging across section headings,
and the abbreviation list swallowing the stop in words ending `-al.`); a
residual miss rate is possible and the line numbers, not the segmentation,
are the authoritative pointer.

## LIST 1 -- ornamental phrasing

Sentences where a figurative or rhetorical construction stands where a
plain statement would do, grouped by kind. Of the seventeen terms named in
the brief, **seven are already absent** from the source: *indictment*,
*constitutional*, *costume*, *wearing*, *demolish*, *conviction*,
*diseased*. The first, third and last were removed by the earlier register
pass; the others never appear. Everything below is present now.

### 1a. Named figures still present

**S2 (Preliminaries), line 297** -- *eyebrow*; the whole clause is a rhetorical gesture

> One eyebrow kept raised on purpose: the thinnest odd table is mod MATH , thinned because MATH is itself a square and the rows MATH and MATH collide there --- MATH 's anomaly is foreshadowed in its own table.

**S6 (The Transfer Principle), line 890** -- *phantom*

> The first prevents a member of MATH from masquerading as a good position: a single MATH with MATH would inject a phantom value into MATH at every good position having MATH as an option, and the identification of MATH with the internal Grundy function would fail there and everywhere above it.

**S7 (The degenerate moduli), line 1020** -- *in the flesh*

> For MATH these positions have real moves, but by (a) every one of them exits onto an N-position; for MATH the alignment is literal: MATH , so MATH is MATH , a moveless position --- Golomb's own terminal in the flesh.

**S7 (The degenerate moduli), line 1041** -- *codebook*, and *the anomaly ledger*

> The anomaly ledger now reads as a codebook: MATH 's recorded fingerprints MATH are MATH over MATH --- the opening P-positions of Golomb's game (OEIS REF A030193 ) --- and MATH 's MATH are MATH over MATH , half-indices MATH : the same openers arriving through the two interleaved copies.

**S7 (The degenerate moduli), line 1047** -- *aliases*; also *the instrument had been filing*

> The instrument had been filing Golomb's sequence under two aliases for the entire census --- while re-deriving that very sequence as a calibration classic before every session.

**S11 (Further solved games), line 2136** -- *governor*, *three jobs, zero waste*, *double life*, *the entire upper odd world leaning on the value 9*

> So "why MATH " has its complete answer --- three moves, three jobs, zero waste: one governor MATH whose doubling is the modulus, plus a pair of odd rescuers whose residues cover all four standard-odd classes; and the number MATH 's double life upgrades rather than dissolves --- rescuer in both modes, carrying MATH as a move and MATH as a square, the entire upper odd world leaning on the value MATH .

**S11 (Further solved games), line 2093** -- *the governor's clones*

> Those differences are MATH , so the harmless amounts are exactly the odd ones and those MATH --- the governor's clones.

**S11 (Further solved games), line 2009** -- *the governor's clones* again, in the Austin/Ho lead-in

> Proposition~ REF and Remark~ REF answer the same question for a mode-switching game, at the level of P-positions: the additions Foursquare tolerates are exactly the odd moves and the governor's clones MATH , and the parity-and-residue argument that certifies them does for mode-switching games the job that reversibility did classically.

**S11 (Further solved games), line 2144** -- *tampering*, *a clone of the governor*

> The mechanism classifies tampering as well: an enlargement of the standard set leaves the P-set fixed exactly when every added move is either odd, landing, from any candidate position, on the all-N odd world, or MATH , a clone of the governor --- verified: MATH , MATH , and MATH preserve the law, MATH , MATH , and MATH break it at MATH , and the maximal enlargement, every odd number plus the whole clone class, holds to MATH .

**S10.1 (Misere play, 10.1), line 1744** -- *receipts*, *the rebel dissolves*; the remark at line 760 is titled `Receipts`

> The receipts, at MATH : the rebel MATH dissolves because its option MATH is a top rung and hence MATH , while MATH is MATH because its four options MATH , MATH , MATH and MATH are respectively a bottom, a bottom, a hard member of MATH , and a bottom --- all MATH .

**S12 (Discovery methodology), line 2253** -- *the sweep's ledger is itself a receipt*

> The Grundy Transfer law was confirmed against 68 games and 1.7 million positions, and the sweep's ledger is itself a receipt: its 77 disagreements are precisely the members of the excluded prefixes MATH --- the mismatches map the theorem's boundary rather than breaching it.

### 1b. Personification of the instrument, the engine and the moves

This is a register running through the paper rather than a set of isolated
lapses. The search program is *the instrument* in twelve sentences; the
parity argument is *the engine*, which is *silent*, *cannot serve* and
*convicts*; the moves *police*, *rescue* and are *decoys*. Representative
entries:

**S7 (The degenerate moduli), line 969** -- *the parity-free engine cannot serve*, *the engine is silent*, *the engine convicts every class from the outside*. The remark's own title, `Double condemnation` (line 967), is the last survivor of the conviction register

> The two degenerate moduli are exactly the two the parity-free engine cannot serve.

**S7 (The degenerate moduli), line 959** -- *no square door onto the foreign bottoms, so the class turns inward*

> Calibration: for MATH and MATH we prove confinement --- no square door onto the foreign bottoms, so the class turns inward.

**S11 (Further solved games), line 2122** -- *not decoys*, *the sole rescuers*, *the squares police only their legal home*

> And MATH and MATH are not decoys --- delete them and the law breaks at once, first at MATH --- for on the standard-mode odds, where squares are illegal, they are the sole rescuers: residue MATH 's only witness is MATH (to bottom MATH ), residue MATH 's is MATH (to MATH ), residue MATH 's is MATH (to MATH ), residue MATH 's is MATH (to MATH ) --- while the squares police only their legal home, the value MATH carrying residues MATH to bottoms MATH and MATH and the value MATH carrying MATH to the same two bottoms.

**S11 (Further solved games), line 2115** -- *bottoms too poor to afford the jump*, *minting a law of modulus 2m*

> That world under one jump of MATH is precisely the shape of the Chain Lemma (Lemma~ REF ) --- four chains by residue modulo MATH , with bottoms MATH too poor to afford the jump, and a jump of size MATH minting a law of modulus MATH --- so MATH mints MATH , with P at the even rungs: MATH , Theorem~ REF , its four residues revealed as chain bottoms; and running the law modulo MATH instead kills closure on the spot, MATH being a move from the candidate into itself.

**S11 (Further solved games), line 2129** -- *the number-theoretic heart at its true address*, *poverty of squares*, *just barely wealth enough*, *stranded*

> Here is the number-theoretic heart at its true address: odd squares modulo MATH take exactly two values, MATH and MATH (Remark~ REF ), and the second is load-bearing precisely at residues MATH and MATH --- the square-mode residues, no others --- while modulo MATH every odd square is MATH and those residues would be stranded: the same poverty of squares modulo powers of two that confines MATH and MATH , one refinement up and just barely wealth enough.

**S13 (What is closed), line 2278** -- *the instrument's old verdict ... is upgraded from a reading to three theorems*

> The instrument's old verdict --- lawless to MATH , no modulus up to MATH --- is upgraded from a reading to three theorems.

**S13 (What is closed), line 2280** -- *the verdict was also, we can now say, slightly modest*

> The verdict was also, we can now say, slightly modest: the instrument's own density figures were carrying the answer all along.

### 1c. Figurative framing in the introduction and the closing section

**S1 (Introduction), line 128** -- *can be tasted before any machinery arrives*

> The main outcome law can be tasted before any machinery arrives: for every MATH except MATH and every MATH , the P-positions of MATH are exactly MATH residue classes modulo MATH --- the bottoms of the game's fallback chains --- together with a finite exception set read off a single parameter, with no thresholds and no unverified zones.

**S1 (Introduction), line 170** -- *not casualties but the first instance of a phenomenon*

> The excluded moduli are not casualties but the first instance of a phenomenon.

**S1 (Introduction), line 180** -- *The consequence closes a door*; also *exactly as wild as*

> The consequence closes a door: a classification theorem for mode-switching subtraction games with arbitrary mode sets would classify all subtraction games, so no such theorem exists to be proved --- one construction away from the solved family lies a class exactly as wild as subtraction games themselves.

**S5 (The Diagonal Theorem), line 784** -- *the cleanest line in this development and the historical door to everything above*

> The identity remains the cleanest line in this development and the historical door to everything above.

**S9 (The Universal Embedding Theorem), line 1538** -- *both disappear under cosmetic changes we do not make*

> Both are absorbed as one-element MATH sets, and both disappear under cosmetic changes we do not make: the theorem's content is the progression based at MATH , where the embedding is exact with no prefix for every MATH and MATH --- the formal statement of the prefix- MATH observation recorded by the search instrument, now with its base point made explicit.

**S10.2 (Misere play, 10.2), line 1829** -- *not a case split in the mechanism but in the geography*

> The sign is not a case split in the mechanism but in the geography: for MATH the free residue sits below the hard one, at MATH above it, and the index set never moves.

**S12 (Discovery methodology), line 2248** -- *The traffic also ran the other way.*

> The traffic also ran the other way.

**S13 (What is closed), line 2289** -- *wedged between two proven bounds*, *must stay instrument-tier forever*

> The true growth rate of Golomb's P-set is wedged between two proven bounds --- the MATH floor (Corollary~ REF , second half) and the MATH ceiling that Furstenberg--S\'ark\"ozy places on any square-difference-free set (Corollary~ REF , first half) --- and our instrument reads a count near MATH across its whole range: a reading, not a theorem, and one that must stay instrument-tier forever unless a genuinely new bound arrives, since no finite prefix can certify an exponent.

**S13 (What is closed), line 2309** -- *a class exactly as wild as subtraction games themselves*

> One construction away from the solved family lies a class exactly as wild as subtraction games themselves.


### 1d. Dash-separated asides longer than eight words

Every sentence containing an em-dash aside of more than eight words. The
aside length is given; several sentences carry two. Sorted by section.

**S1 (Introduction), line 117** -- 11-word aside

> This paper studies a structured family at that frontier and solves it completely --- outcomes and Grundy values under normal play, outcomes under mis\`ere --- and then shows that the structure making the family solvable sits one construction away from universality: the same mode-switching format can host any subtraction game whatever.

**S1 (Introduction), line 195** -- 12-word aside

> Section~ REF puts the machinery to work three times: MATH solved in full as the worked example; Foursquare --- the machine's first find, moves MATH with a square mode at MATH --- solved with its mechanism exposed and Kadam's Extension established; and a criterion determining exactly which enlargements of a mode's move set preserve a law.

**S4 (Escape: the parameter s_min), line 375** -- 10-word aside

> Write MATH for the set of foreign bottoms --- the bottoms of the MATH chains classified by Lemma~ REF --- and define the hard set MATH For MATH this is MATH , and for MATH it is MATH .

**S4 (Escape: the parameter s_min), line 491** -- 9-word aside

> One square, two jobs: the witness that lands the hard residue on a bottom --- the escape that Section~ REF converts into the classification --- is at the same time the Grundy- MATH half of the palette, which Section~ REF converts into a transfer of Grundy values.

**S4 (Escape: the parameter s_min), line 531** -- 10-word aside

> Indeed, a square MATH has residue MATH (as MATH ), and every residue in MATH exceeds MATH when read in MATH --- its elements are MATH for MATH and MATH for MATH --- so MATH and squares up to MATH never certify.

**S7 (The degenerate moduli), line 944** -- 13-word aside

> For MATH and every MATH : MATH --- read directly off the mod- MATH and mod- MATH rows of Table~ REF --- while every hard set MATH excludes MATH , MATH , and MATH (Definition~ REF ).

**S7 (The degenerate moduli), line 1041** -- 9-word aside

> The anomaly ledger now reads as a codebook: MATH 's recorded fingerprints MATH are MATH over MATH --- the opening P-positions of Golomb's game (OEIS REF A030193 ) --- and MATH 's MATH are MATH over MATH , half-indices MATH : the same openers arriving through the two interleaved copies.

**S8 (The Grundy Transfer Theorem), line 1325** -- 16-word aside

> Restrict to the class- MATH positions on a single copy MATH : adding MATH to MATH preserves the class and the copy --- MATH is the period of the copy structure in MATH , so any multiple of it does --- and, beyond MATH , the Grundy value, so by Theorem~ REF the sequence MATH is eventually periodic with period MATH .

**S9 (The Universal Embedding Theorem), line 1506** -- 12-word aside

> Theorem~ REF gives MATH equal to the Grundy function of the internal game --- the subtraction game MATH on the index MATH , by Lemma~ REF (iv) --- with the index MATH deleted; moves onto index MATH are excluded from the mex as moves into MATH .

**S9 (The Universal Embedding Theorem), line 1516** -- 10-word aside

> The least member MATH already affords both witnesses, so (H1) holds everywhere with the values exchanged --- MATH lands on a bottom, MATH on a top rung --- and (H2) is as before.

**S10 (Misere play), line 1600** -- 30-word aside

> No Grundy theory is available here --- mis\`ere outcomes of a disjunctive sum are not determined by the summands' outcomes REF , and the mis\`ere quotient of even a simple subtraction game may be large REF --- so this section classifies outcomes only.

**S11 (Further solved games), line 2003** -- 26-word aside

> The question of which moves may be added to a subtraction game without changing it is an old one: Austin answered it in 1976 for purely periodic subtraction games --- for each move MATH already present, the move MATH may be adjoined, since the reply MATH reverses it out and the period MATH absorbs the pair --- and Ho, in 2015, gave the idea its modern name, expansion sets REF .

**S11 (Further solved games), line 2037** -- 9-word aside

> In the other direction, the extended move set contains the original one and square mode is untouched, so every escape witness of the original proof --- the standard moves and the squares MATH and MATH --- remains a legal move of MATH with the same landing, and a move set that only grows cannot lose an escape: every position outside the candidate still has its move into it.

**S11 (Further solved games), line 2042** -- 9-word aside

> The candidate therefore meets all three conditions of Lemma~ REF in MATH --- terminals inside, closed against return, reachable from everywhere outside --- so it is the P-set of MATH , and it coincides with Foursquare's.

**S11 (Further solved games), line 2066** -- 9-word aside

> A position MATH with MATH has all of its old options outside MATH , hence N-positions by the induction hypothesis; its possible new option MATH --- present only when MATH is in the enlarged mode --- cannot lie in MATH , since that would contradict the minimality of MATH ; so every option of MATH is an N-position and MATH remains a P-position.

**S11 (Further solved games), line 2080** -- 33-word aside

> Enlarging MATH 's squares-mode set by the amount MATH leaves its law untouched --- and provably so, no longer by sweep: by Corollary~ REF the class MATH of MATH contains no P-position at all, so the criterion's condition holds vacuously and Proposition~ REF returns the law unchanged --- even though MATH is a difference of two P-positions of the game ( MATH modulo MATH ).

**S11 (Further solved games), line 2115** -- 27-word aside

> That world under one jump of MATH is precisely the shape of the Chain Lemma (Lemma~ REF ) --- four chains by residue modulo MATH , with bottoms MATH too poor to afford the jump, and a jump of size MATH minting a law of modulus MATH --- so MATH mints MATH , with P at the even rungs: MATH , Theorem~ REF , its four residues revealed as chain bottoms; and running the law modulo MATH instead kills closure on the spot, MATH being a move from the candidate into itself.

**S11 (Further solved games), line 2122** -- 11-word aside

> And MATH and MATH are not decoys --- delete them and the law breaks at once, first at MATH --- for on the standard-mode odds, where squares are illegal, they are the sole rescuers: residue MATH 's only witness is MATH (to bottom MATH ), residue MATH 's is MATH (to MATH ), residue MATH 's is MATH (to MATH ), residue MATH 's is MATH (to MATH ) --- while the squares police only their legal home, the value MATH carrying residues MATH to bottoms MATH and MATH and the value MATH carrying MATH to the same two bottoms.

**S11 (Further solved games), line 2136** -- 38-word aside

> So "why MATH " has its complete answer --- three moves, three jobs, zero waste: one governor MATH whose doubling is the modulus, plus a pair of odd rescuers whose residues cover all four standard-odd classes; and the number MATH 's double life upgrades rather than dissolves --- rescuer in both modes, carrying MATH as a move and MATH as a square, the entire upper odd world leaning on the value MATH .

**S12 (Discovery methodology), line 2215** -- 9-word aside

> Before and after every session the engine re-derives five classical laws --- the subtraction game MATH and Golomb's subtract-a-square among them --- so that drift anywhere in the stack would announce itself in the classics first.

**S12 (Discovery methodology), line 2231** -- 9-word aside

> The protocol earns its keep rather than asserting itself: one drafting error --- a subtly different game verified faithfully across three documents --- was caught only because the discipline requires sentences to follow printouts, never precede them.

**S12 (Discovery methodology), line 2248** -- 10-word aside

> Corollary~ REF --- that MATH enters the class-index Grundy sequence only through MATH --- was derived before it was swept, and a sweep across eight moduli then returned the collapse exactly: at each modulus, every healthy game with MATH produced one and the same class-index sequence, and the three exceptional games at MATH produced theirs.

**S13 (What is closed), line 2289** -- 24-word aside

> The true growth rate of Golomb's P-set is wedged between two proven bounds --- the MATH floor (Corollary~ REF , second half) and the MATH ceiling that Furstenberg--S\'ark\"ozy places on any square-difference-free set (Corollary~ REF , first half) --- and our instrument reads a count near MATH across its whole range: a reading, not a theorem, and one that must stay instrument-tier forever unless a genuinely new bound arrives, since no finite prefix can certify an exponent.

**S* (Acknowledgments), line 2330** -- 30-word aside

> Separately, much of the theory in this paper --- the MATH apparatus of Sections~ REF and~ REF , and the transfer, Grundy, embedding and mis\`ere results of Sections~ REF and~ REF through~ REF , together with the abstract and introduction --- was developed in extended dialogue with Claude (Anthropic), which drafted statements and proofs.


## LIST 2 -- sentences over 45 words

**81 sentences**, longest first. Word counts treat each collapsed
mathematical expression and each cross-reference as one word, so these are
lower bounds on what a reader parses.

**93 words** -- S11 (Further solved games), line 2122

> And MATH and MATH are not decoys --- delete them and the law breaks at once, first at MATH --- for on the standard-mode odds, where squares are illegal, they are the sole rescuers: residue MATH 's only witness is MATH (to bottom MATH ), residue MATH 's is MATH (to MATH ), residue MATH 's is MATH (to MATH ), residue MATH 's is MATH (to MATH ) --- while the squares police only their legal home, the value MATH carrying residues MATH to bottoms MATH and MATH and the value MATH carrying MATH to the same two bottoms.

**90 words** -- S11 (Further solved games), line 2028

> From a candidate position --- even, hence standard mode --- every legal move of MATH subtracts some MATH or MATH , and the closure argument of Theorem~ REF consumed exactly two facts about MATH , its parity and its residue modulo MATH , never its actual size, so it transfers verbatim to every member of the extended family: the MATH and MATH moves are odd and land on odd residues, none of which lie in the all-even candidate, while the MATH moves land on MATH , also outside --- no move from the candidate returns to it.

**89 words** -- S1 (Introduction), line 214

> Section~ REF fixes notation and the verification lemma; Sections~ REF through~ REF build chains, the MATH apparatus, and the Diagonal Law; Section~ REF isolates the Transfer Principle; Section~ REF proves confinement at MATH and MATH ; Sections~ REF and~ REF carry the principle forward to the Grundy solution and backward to the universal embedding; Section~ REF settles mis\`ere play; Section~ REF solves further games; Section~ REF opens the instrument; and Section~ REF closes what the census could not settle --- and locates the question that remains, older than this paper.

**85 words** -- S11 (Further solved games), line 2115

> That world under one jump of MATH is precisely the shape of the Chain Lemma (Lemma~ REF ) --- four chains by residue modulo MATH , with bottoms MATH too poor to afford the jump, and a jump of size MATH minting a law of modulus MATH --- so MATH mints MATH , with P at the even rungs: MATH , Theorem~ REF , its four residues revealed as chain bottoms; and running the law modulo MATH instead kills closure on the spot, MATH being a move from the candidate into itself.

**79 words** -- S10.2 (Misere play, 10.2), line 1814

> The index sets coincide because the two internal games are identical --- subtract-a-square at MATH , subtract- MATH at MATH --- with index origin in each case at a position too small to afford any internal move, since MATH ; and both are evaluated by the normal-play recursion: the hard side because play there is normal, the free side by Lemma~ REF , whose conclusion is precisely that the mis\`ere outcomes of the confined class are the normal-play outcomes of its internal game.

**75 words** -- S13 (What is closed), line 2289

> The true growth rate of Golomb's P-set is wedged between two proven bounds --- the MATH floor (Corollary~ REF , second half) and the MATH ceiling that Furstenberg--S\'ark\"ozy places on any square-difference-free set (Corollary~ REF , first half) --- and our instrument reads a count near MATH across its whole range: a reading, not a theorem, and one that must stay instrument-tier forever unless a genuinely new bound arrives, since no finite prefix can certify an exponent.

**74 words** -- S11 (Further solved games), line 2129

> Here is the number-theoretic heart at its true address: odd squares modulo MATH take exactly two values, MATH and MATH (Remark~ REF ), and the second is load-bearing precisely at residues MATH and MATH --- the square-mode residues, no others --- while modulo MATH every odd square is MATH and those residues would be stranded: the same poverty of squares modulo powers of two that confines MATH and MATH , one refinement up and just barely wealth enough.

**72 words** -- S11 (Further solved games), line 2144

> The mechanism classifies tampering as well: an enlargement of the standard set leaves the P-set fixed exactly when every added move is either odd, landing, from any candidate position, on the all-N odd world, or MATH , a clone of the governor --- verified: MATH , MATH , and MATH preserve the law, MATH , MATH , and MATH break it at MATH , and the maximal enlargement, every odd number plus the whole clone class, holds to MATH .

**69 words** -- S11 (Further solved games), line 2136

> So "why MATH " has its complete answer --- three moves, three jobs, zero waste: one governor MATH whose doubling is the modulus, plus a pair of odd rescuers whose residues cover all four standard-odd classes; and the number MATH 's double life upgrades rather than dissolves --- rescuer in both modes, carrying MATH as a move and MATH as a square, the entire upper odd world leaning on the value MATH .

**68 words** -- S9 (The Universal Embedding Theorem), line 1581

> The construction uses only three properties of the host: that the foreign classes are step- MATH chains, so that the ceiling of Theorem~ REF is the alternation of Corollary~ REF ; that the mode set contains two amounts whose residues lie on opposite sides of the partition of Lemma~ REF (ii), so that the palette is available; and that the remaining amounts are MATH , so that they are internal.

**66 words** -- S11 (Further solved games), line 2037

> In the other direction, the extended move set contains the original one and square mode is untouched, so every escape witness of the original proof --- the standard moves and the squares MATH and MATH --- remains a legal move of MATH with the same landing, and a move set that only grows cannot lose an escape: every position outside the candidate still has its move into it.

**66 words** -- S11 (Further solved games), line 2003

> The question of which moves may be added to a subtraction game without changing it is an old one: Austin answered it in 1976 for purely periodic subtraction games --- for each move MATH already present, the move MATH may be adjoined, since the reply MATH reverses it out and the period MATH absorbs the pair --- and Ho, in 2015, gave the idea its modern name, expansion sets REF .

**66 words** -- S7 (The degenerate moduli), line 1150

> Written out at MATH , where the accounting is least obvious: by Theorem~ REF the confined P-set is MATH , the even and odd parities of MATH ; an affine map MATH scales a counting function by the constant MATH , so each image inherits density zero from MATH , and a union of two density-zero sets is density zero --- two, not infinitely many, is what makes that last step safe.

**66 words** -- S4 (Escape: the parameter s_min), line 604

> An internal move --- a square MATH --- has residue MATH or MATH modulo MATH ; the residue- MATH case is exactly divisibility by MATH , just excluded, so within MATH every internal move has residue MATH , and by Lemma~ REF (iii) it exchanges the two residues of the class while landing on a smaller class member, which lies in MATH since MATH is an initial segment of the class.

**63 words** -- S11 (Further solved games), line 2150

> The extension of Proposition~ REF adds precisely the residue classes of MATH , MATH , and MATH themselves, squarely inside the harmless family, so the conjecture is not merely true but forced --- and busy rather than idle: below MATH the new moves serve as genuine witnesses at MATH positions, MATH of them odd, the smallest being MATH , a new odd move rescuing its own residue.

**61 words** -- S12 (Discovery methodology), line 2237

> Twice the instrument recorded numbers that no theory then existed to explain, and both entries were later derived exactly: the unexplained P-positions MATH in MATH and MATH in MATH are the images of Golomb's opening losing positions under the reindexings of Theorem~ REF , and the recorded preperiod MATH for MATH is one more than the rebel position MATH of Corollary~ REF .

**61 words** -- S11 (Further solved games), line 2080

> Enlarging MATH 's squares-mode set by the amount MATH leaves its law untouched --- and provably so, no longer by sweep: by Corollary~ REF the class MATH of MATH contains no P-position at all, so the criterion's condition holds vacuously and Proposition~ REF returns the law unchanged --- even though MATH is a difference of two P-positions of the game ( MATH modulo MATH ).

**60 words** -- S4 (Escape: the parameter s_min), line 467

> Finally, since MATH and MATH are disjoint and MATH by (iv), the residue MATH does not lie in MATH ; the square MATH therefore never certifies, and as no square lies strictly between MATH and MATH , it follows that MATH whenever MATH is finite --- and since the residues MATH and MATH are outside MATH , MATH is never a multiple of MATH .

**60 words** -- S0 (abstract), line 81

> The mechanism is isolated as a Transfer Principle for arbitrary impartial games, and it runs backward: a host construction embeds any subtraction game whatever as a mode class of a mode-switching game, at outcome level and, with one added move, at Grundy level --- so a classification theorem for mode-switching subtraction games with arbitrary mode sets would classify all subtraction games.

**59 words** -- S9 (The Universal Embedding Theorem), line 1538

> Both are absorbed as one-element MATH sets, and both disappear under cosmetic changes we do not make: the theorem's content is the progression based at MATH , where the embedding is exact with no prefix for every MATH and MATH --- the formal statement of the prefix- MATH observation recorded by the search instrument, now with its base point made explicit.

**59 words** -- S8 (The Grundy Transfer Theorem), line 1311

> By Proposition~ REF (i) the deleted set is an initial segment of the class index, hence by Proposition~ REF (iii) an initial run of length MATH within each copy; since the move set MATH is translation-invariant, deleting an initial run and re-basing yields Golomb's game itself, shifted, so on copy MATH the function MATH at half-index MATH equals MATH .

**58 words** -- S11 (Further solved games), line 2066

> A position MATH with MATH has all of its old options outside MATH , hence N-positions by the induction hypothesis; its possible new option MATH --- present only when MATH is in the enlarged mode --- cannot lie in MATH , since that would contradict the minimality of MATH ; so every option of MATH is an N-position and MATH remains a P-position.

**58 words** -- S7 (The degenerate moduli), line 997

> If MATH then MATH : at MATH this is MATH and the move stays in the class, while at MATH the landing MATH is the free residue ( MATH , or MATH when MATH ), every member of which is N because it subtracts MATH onto the foreign bottom directly beneath it --- P by Lemma~ REF , legal from the smallest free member.

**58 words** -- S4 (Escape: the parameter s_min), line 458

> Second, the hole in MATH sits at the residue MATH and is the image, under the bijection of (i), of the omitted bottom MATH --- the bottom that class MATH would have if its members were in fallback mode; the gap in the hard set and the uselessness of the amounts MATH are one fact seen from two sides.

**58 words** -- S3 (The Chain Lemma), line 323

> Step: assume the claim for rung MATH ; rung MATH 's single option is rung MATH , and a single-option position is P if and only if its option is N --- so for MATH even, rung MATH is N by the assumption and rung MATH is P, while for MATH odd, rung MATH is P and rung MATH is N.

**58 words** -- S1 (Introduction), line 154

> Behind the outcome argument sits a mechanism worth isolating, and Section~ REF states it for an arbitrary impartial game: if a set of positions has, off a finite bad prefix, external options realising exactly the Grundy values MATH and MATH , then its Grundy values are the internal game's values shifted by MATH , the periphery and the prefix invisible.

**57 words** -- S6 (The Transfer Principle), line 913

> If MATH and MATH , the same two lines give MATH ; and if (H1) and (H2) are replaced by the requirement that the external options of a good position realise exactly the values MATH and never exceed them, and (H3) by MATH on MATH , then the conclusion becomes MATH on MATH with MATH satisfying the same internal recursion.

**56 words** -- S10.2 (Misere play, 10.2), line 1804

> At MATH a square divisible by MATH is divisible by MATH , hence of the form MATH , so the internal moves read MATH , with legality MATH equivalent to MATH ; this is subtract- MATH , which preserves the parity of MATH and splits into two interleaved copies of subtract-a-square in the half-index MATH , exactly as in Theorem~ REF (d).

**56 words** -- S8 (The Grundy Transfer Theorem), line 1325

> Restrict to the class- MATH positions on a single copy MATH : adding MATH to MATH preserves the class and the copy --- MATH is the period of the copy structure in MATH , so any multiple of it does --- and, beyond MATH , the Grundy value, so by Theorem~ REF the sequence MATH is eventually periodic with period MATH .

**56 words** -- S7 (The degenerate moduli), line 1011

> The three-way sort is genuinely three-way only at MATH : modulo MATH the values MATH and MATH collapse into one residue, so at MATH parity alone decides --- every even square stays internal --- which is why MATH hosts Golomb's game whole while MATH , whose middle class defects to the free residue, keeps only the doubled cousin subtract- MATH .

**56 words** -- S4 (Escape: the parameter s_min), line 642

> The regime values: for healthy MATH , MATH gives MATH ; for healthy MATH , every square up to MATH has residue at most MATH , outside MATH , so MATH , while MATH as in Lemma~ REF --- hence MATH , with MATH hard and MATH free; for MATH , MATH with MATH gives MATH , so MATH with the free--hard--free pattern MATH , MATH , MATH .

**55 words** -- S12 (Discovery methodology), line 2257

> And once, theory corrected a reading rather than confirming it: the embedding sweeps behind Section~ REF reported hard-side exactness for every index, which was true of an index based at the second member and false at the first --- the base-point clause of Theorem~ REF exists because the proof caught what a base-blind sweep could not.

**55 words** -- S11 (Further solved games), line 1935

> When MATH is empty --- every healthy game with MATH --- the P-set is the bottom classes alone, which is the coincidence observed above for MATH ; at MATH and on MATH the set MATH contributes its single position; and at the degenerate moduli, where MATH , the class- MATH contribution is the infinite confined set of Section~ REF .

**55 words** -- S9 (The Universal Embedding Theorem), line 1556

> For the second sentence, a property of the Grundy sequence of MATH that is invariant under an affine reindexing and a shift by MATH transports to the host's class MATH ; and outside class MATH the host's values are MATH and MATH , which cannot restore periodicity to an aperiodic class, by the argument of Corollary~ REF .

**55 words** -- S1 (Introduction), line 128

> The main outcome law can be tasted before any machinery arrives: for every MATH except MATH and every MATH , the P-positions of MATH are exactly MATH residue classes modulo MATH --- the bottoms of the game's fallback chains --- together with a finite exception set read off a single parameter, with no thresholds and no unverified zones.

**55 words** -- S0 (abstract), line 73

> The Grundy function on the square-mode class is, beyond the finite prefix, an explicit shift of the nim-sequence of Golomb's subtract-a-square game; consequently no member of the family is eventually periodic at the level of Grundy values, and each has bounded Grundy values if and only if Golomb's game does --- a question that is open.

**54 words** -- S1 (Introduction), line 195

> Section~ REF puts the machinery to work three times: MATH solved in full as the worked example; Foursquare --- the machine's first find, moves MATH with a square mode at MATH --- solved with its mechanism exposed and Kadam's Extension established; and a criterion determining exactly which enlargements of a mode's move set preserve a law.

**53 words** -- S13 (What is closed), line 2272

> The two columns the census could never fit --- the confined classes of MATH and MATH --- are Golomb's subtract-a-square game up to an affine change of coordinates (Theorem~ REF ); they never settle into any eventual period (Corollary~ REF ); and their P-positions thin toward density zero while never falling below the MATH floor (Corollary~ REF ).

**53 words** -- S12 (Discovery methodology), line 2248

> Corollary~ REF --- that MATH enters the class-index Grundy sequence only through MATH --- was derived before it was swept, and a sweep across eight moduli then returned the collapse exactly: at each modulus, every healthy game with MATH produced one and the same class-index sequence, and the three exceptional games at MATH produced theirs.

**53 words** -- S10.2 (Misere play, 10.2), line 1845

> The square-difference-free property transfers because two MATH positions of the confined class are both in squares mode and their difference, were it a square, would be a legal move from one to the other --- a move between two P-positions of the mis\`ere internal game, which the normal-play recursion of Lemma~ REF forbids.

**53 words** -- S9 (The Universal Embedding Theorem), line 1572

> Taking instead MATH to be the move set of the aperiodic game of Larsson and Fox REF produces a mode-switching subtraction game of Nim-dimension two, and taking MATH finite reproduces, inside a non-invariant host, the classical periodicity of REF on one residue class while the rest of the board obeys the chain law.

**53 words** -- S4 (Escape: the parameter s_min), line 361

> This section builds the apparatus for class MATH itself: the two residues the class occupies modulo MATH , the hard set of useful residues, and a single parameter, MATH , from which the classification of Section~ REF , its exception sets, and the Grundy and mis\`ere laws of Sections~ REF and~ REF are all read.

**52 words** -- S12 (Discovery methodology), line 2224

> The division of labor between the instrument and the mathematics is strict, and the repository states it in writing: the instrument proposes and verifies mechanically and constructs no proofs, and each numerical claim above regenerates from the seeded scripts at REF , where the integrity protocol and its full session logs also live.

**52 words** -- S10 (Misere play), line 1657

> The last sentence is the point on which the section turns, and it is worth isolating: a position of MATH with no internal options is not terminal in the host, so the mis\`ere convention never reaches it, and it is labelled P by the vacuous clause exactly as in normal play.

**52 words** -- S7 (The degenerate moduli), line 1032

> In subtract- MATH every move is even, so the parity of MATH is invariant, and on each parity class the move MATH reads MATH in the half-index MATH (legality MATH on both parities), with terminal MATH on each side: two interleaved, independent copies of Golomb's game, so MATH is P iff MATH .

**52 words** -- S6 (The Transfer Principle), line 903

> When MATH the hypothesis (H3) is vacuous, no shift arises, and MATH is the internal Grundy function on the whole of MATH --- this is the situation of the embedding of Section~ REF on its hard progression, where the host is built so that the palette is available from the base point onward.

**52 words** -- S4 (Escape: the parameter s_min), line 386

> The point of taking MATH in MATH rather than in MATH is that the free residue is not the smaller of the two representatives but the one from which the move MATH reaches the bottom layer: from residue MATH the move MATH lands on MATH , which lies in MATH precisely when MATH .

**51 words** -- S* (Acknowledgments), line 2330

> Separately, much of the theory in this paper --- the MATH apparatus of Sections~ REF and~ REF , and the transfer, Grundy, embedding and mis\`ere results of Sections~ REF and~ REF through~ REF , together with the abstract and introduction --- was developed in extended dialogue with Claude (Anthropic), which drafted statements and proofs.

**51 words** -- S11 (Further solved games), line 2197

> By induction the entire Grundy sequence is therefore identical for every odd fallback MATH : the parameter is invisible to the game, because the squares already supply, from every odd position, a move to an even one, and the fallback can only ever move between residues that Part (i) has already flattened.

**51 words** -- S10.2 (Misere play, 10.2), line 1834

> For MATH and every MATH , the mis\`ere P-set of MATH is not eventually periodic; the confined free class contains no two elements differing by a perfect square, hence has asymptotic density zero, while retaining at least MATH members up to MATH ; and the mis\`ere P-set has asymptotic density MATH .

**51 words** -- S6 (The Transfer Principle), line 890

> The first prevents a member of MATH from masquerading as a good position: a single MATH with MATH would inject a phantom value into MATH at every good position having MATH as an option, and the identification of MATH with the internal Grundy function would fail there and everywhere above it.

**51 words** -- S2 (Preliminaries), line 293

> The mod- MATH and mod- MATH rows are the diagnosis written out: $ (4) = \ 0, 1\ MATH (8) = \ 0, 1, 4\ $ both sit entirely inside the triple MATH , so their complements swallow every value any hard set will ever contain (Section~ REF ) --- the degeneracy of MATH and MATH is visible in these two rows before any game logic starts.

**51 words** -- S0 (abstract), line 65

> For every MATH except MATH and every MATH , the P-positions are the MATH residue classes modulo MATH of the fallback chains' bottoms, together with the hard half of a finite set MATH read off a single parameter MATH --- the boundary position MATH when MATH , and a single rebel MATH at MATH .

**50 words** -- S10.1 (Misere play, 10.1), line 1728

> For normal play, Proposition~ REF (ii) assigns Grundy value MATH to the hard members of MATH and MATH to the free members, so the former are P-positions and the latter are not; and by Theorem~ REF every class- MATH position at or above MATH has Grundy value at least MATH .

**50 words** -- S9 (The Universal Embedding Theorem), line 1448

> It follows by induction on MATH that a hard member is P if and only if all of its internal options are N, and N if and only if some internal option is P --- which is the recursion of the subtraction game MATH under the index of Lemma~ REF (iv).

**50 words** -- S8 (The Grundy Transfer Theorem), line 1342

> Outside class MATH the values are MATH and MATH by Corollary~ REF ; inside class MATH they are MATH beyond a finite set by Theorem~ REF , and the argument of MATH ranges over all sufficiently large integers on the copy MATH , which is nonempty for every MATH since it contains MATH .

**50 words** -- S8 (The Grundy Transfer Theorem), line 1268

> The recursion of Theorem~ REF below is determined by MATH , which depends only on MATH , and by the deleted initial segment, whose length is MATH ; the external landings enter only through their Grundy values, which are MATH or MATH by Corollary~ REF irrespective of which foreign chain they lie on.

**50 words** -- S7 (The degenerate moduli), line 1024

> The status of a position is determined by its options alone, and by (a) every exiting option is N; so a hard-class position is P iff all of its internal options are N, and N iff some internal option is P --- exits can neither supply a P-witness nor block one.

**50 words** -- S4 (Escape: the parameter s_min), line 659

> Residue in MATH is external: by Lemma~ REF (iii) it lands a free position on a foreign bottom, of Grundy value MATH by Corollary~ REF , and a hard position on a top rung, of value MATH --- and the move MATH is of this kind (Lemma~ REF (iv)), legal whenever MATH .

**50 words** -- S4 (Escape: the parameter s_min), line 536

> A square MATH with MATH has residue MATH , which lies in MATH exactly when MATH is not a multiple of MATH ; the window contains exactly one multiple of MATH (any MATH consecutive integers do), namely MATH itself when MATH and MATH when MATH , and if MATH its residue is MATH .

**50 words** -- S1 (Introduction), line 117

> This paper studies a structured family at that frontier and solves it completely --- outcomes and Grundy values under normal play, outcomes under mis\`ere --- and then shows that the structure making the family solvable sits one construction away from universality: the same mode-switching format can host any subtraction game whatever.

**49 words** -- S11 (Further solved games), line 2009

> Proposition~ REF and Remark~ REF answer the same question for a mode-switching game, at the level of P-positions: the additions Foursquare tolerates are exactly the odd moves and the governor's clones MATH , and the parity-and-residue argument that certifies them does for mode-switching games the job that reversibility did classically.

**49 words** -- S10 (Misere play), line 1625

> In normal play the useful landing is a bottom, supplied to the hard residue by MATH and to the free residue by the always-legal MATH ; in mis\`ere the useful landing is a top rung, supplied to the hard residue by MATH and to the free residue by MATH .

**49 words** -- S9 (The Universal Embedding Theorem), line 1379

> Notation and terminology for the host are those of Definition~ REF --- MATH , MATH , MATH , bottoms, top rungs --- which depend only on MATH and MATH and so apply verbatim; Lemma~ REF and Corollary~ REF likewise apply verbatim, since the foreign classes of the host are the same step- MATH chains.

**48 words** -- S* (Acknowledgments), line 2336

> The author directed that work, refereed and corrected every draft, verified every claim against independent computation, and takes sole responsibility for the correctness of what is stated here; individual results and remarks elsewhere in the paper come from the same dialogue, as do the results of Section~ REF .

**48 words** -- S10.1 (Misere play, 10.1), line 1744

> The receipts, at MATH : the rebel MATH dissolves because its option MATH is a top rung and hence MATH , while MATH is MATH because its four options MATH , MATH , MATH and MATH are respectively a bottom, a bottom, a hard member of MATH , and a bottom --- all MATH .

**48 words** -- S9 (The Universal Embedding Theorem), line 1588

> A host whose fallback mode has a larger move set will fail the first of these and present a taller ceiling; by Remark~ REF the Transfer Principle survives such a change with MATH replaced by the appropriate MATH , and the corresponding embedding theorem is the natural next question.

**48 words** -- S5 (The Diagonal Theorem), line 761

> The closure argument, instantiated at the rebel MATH of MATH : the legal squares are MATH , of residues MATH modulo MATH ; the first two lie in MATH and land on the top rungs MATH and MATH ; the third has residue MATH and lands on the free MATH member MATH .

**48 words** -- S2 (Preliminaries), line 231

> A terminal position (no legal moves) is a -position; a position is an -position if and only if at least one legal move reaches a -position; a position is a -position if and only if every legal move reaches an -position, the terminal case satisfying this clause vacuously.

**48 words** -- S1 (Introduction), line 175

> Section~ REF shows the phenomenon is universal: for any subtraction game MATH , a mode-switching host with fallback MATH and mode set MATH reproduces MATH 's P-set on an arithmetic progression, and adding the single move MATH upgrades the embedding to Grundy values, exact from the base point MATH .

**48 words** -- S1 (Introduction), line 159

> Run forward on the diagonal family, the principle yields the complete Grundy solution (Section~ REF ): on the square-mode class, beyond MATH , MATH along an explicit reindexing, where MATH is the nim-sequence of Golomb's subtract-a-square game and the offset is read from MATH and the squarefree part of MATH .

**47 words** -- S12 (Discovery methodology), line 2205

> The conjectures in this paper were proposed by GameHunter, a closed loop of four parts: a proposer that varies rulesets, a Grundy engine that computes exact values, deterministic detectors that flag periodicity and modular structure, and a novelty filter that discards sequences already catalogued in the OEIS.

**47 words** -- S10.2 (Misere play, 10.2), line 1854

> The mis\`ere picture is therefore complete for the whole family and follows the normal-play picture clause for clause: chains classified with values inverted, class MATH settled by a single parameter, exceptional positions confined to MATH , and the two degenerate moduli confined and equivalent to Golomb's game.

**47 words** -- S7 (The degenerate moduli), line 984

> Then for MATH the position MATH is P in MATH if and only if MATH , and for MATH the position MATH is P in MATH if and only if MATH --- the confined class consisting of two interleaved copies of Golomb's game, one on each parity of MATH .

**47 words** -- S7 (The degenerate moduli), line 947

> Hence from any hard-residue position, every legal square move either stays inside class MATH (a square $ 0 MATH m MATH 2m MATH 0 MATH m$) or lands one below on the odd rung above a bottom (a square MATH ), an -position --- never on a -position of a foreign chain.

**47 words** -- S1 (Introduction), line 139

> The MATH -duality lemma matches amounts to landings: an amount is useful from the square-mode class exactly when its residue modulo MATH avoids MATH and MATH , and the useful residues split into a hard set MATH and its shift, serving the class's two residues in complementary pairs.

**46 words** -- S10.1 (Misere play, 10.1), line 1700

> By the definition of MATH no legal square of MATH has residue in MATH , so by Lemma~ REF (ii)--(iii) every legal square is either internal or of residue in MATH ; the latter carries the free residue onto a bottom, which is MATH by Lemma~ REF .

**46 words** -- S9 (The Universal Embedding Theorem), line 1535

> On the free residue it is the least member MATH , which cannot afford MATH ; at MATH on the hard residue it is MATH , which can afford nothing at all and is the host's inheritance of the boundary position audited for the diagonal family in Section~ REF .

**46 words** -- S3 (The Chain Lemma), line 353

> We call a position of a foreign class a bottom if it is an even rung and a top rung if it is an odd rung; Corollary~ REF says bottoms carry Grundy value MATH and top rungs carry Grundy value MATH , uniformly across all foreign classes.

**46 words** -- S2 (Preliminaries), line 241

> If (i) every terminal position lies in MATH , (ii) no move from a position in MATH leads to a position in MATH , and (iii) from every position not in MATH some move leads to a position in MATH , then MATH is exactly the set of -positions.

**46 words** -- S1 (Introduction), line 180

> The consequence closes a door: a classification theorem for mode-switching subtraction games with arbitrary mode sets would classify all subtraction games, so no such theorem exists to be proved --- one construction away from the solved family lies a class exactly as wild as subtraction games themselves.


## LIST 3 — undefined or late-defined terminology

Line numbers are the first use. "Defined" means introduced by a
`\begin{definition}`, by an `\emph{}` naming, or by an explicit "we call".

### 3a. Used in Sections 1–3, defined only in Section 4 or later

| term | first use | defined at |
|---|---|---|
| `s_min` | abstract, line 69; §1 line 144 | §4, Definition 4.1 (line 368) |
| `Bad(m,r)`, and *bad set* | abstract, line 68; §1 line 148 | §4, Definition 4.7 (line 578) |
| *hard set* `H` | §1, line 141 | §4, Definition 4.1 (line 368) |
| *hard half* / *free half* | abstract, lines 68 and 72; §1 line 148 | §4, Definition 4.7 defines `Bad_h`, `Bad_f`; the words "half" are never defined |
| *healthy* | §1, line 144 | §4, Proposition 4.6(a) (line 517) |
| *exceptional* | abstract, line 72 | §4, Proposition 4.6(b) |
| *degenerate* | §1, line 190 | §4, Proposition 4.6(c); §7 title |
| *Transfer Principle* | §1, line 217 | §6, Theorem 6.2 (line 823) |

Eight terms. All eight are load-bearing in the sentences that use them: a
reader of the abstract meets `s_min`, `Bad(m,r)`, *hard half*, *rebel* and
*exceptional* before any of them exists.

### 3b. Never defined anywhere in the paper

**`rebel`** — eight occurrences: abstract line 70; §1 line 151; §5 lines 755
and 761; §10.1 lines 1736, 1743, 1745; §12 line 2242. The term is used as
though defined, including in the abstract and in the statement-adjacent
prose of §5, but no definition survives. It was carried by the deleted
`Proposition [The rebels]`, removed when §4 was rebuilt around `s_min`; the
word outlived its definition.

**`Nim-dimension`** — five occurrences: §1 line 168; §8 line 1351; §9 lines
1367, 1551, 1552, 1575. Never defined, and the only gloss is in a
bibliography title (line 2371). §1 calls it "Golomb's Nim-dimension
question" on first use.

### 3c. Used before a definition that does arrive within Sections 1–3

Weaker than 3a — the definition is not late by the brief's criterion — but
the first use still precedes it.

| term | first use | defined at |
|---|---|---|
| *bottom*, *bottoms* | abstract, line 67 | §3, line 353 |
| *top rung*, *rung* | §1, line 188 | §3, lines 353–354 |
| *chain*, *fallback chain* | abstract, line 67 | §3, Lemma 3.1 (line 305) |

### 3d. Defined more than once, or used in two senses

**`window`** — two incompatible senses, neither formally defined.

1. §4 uses it for the clearing interval `(f, f+m]`: the title of Lemma 4.5
   is "A square in the window" (line 499), and Proposition 4.6 repeats it
   (lines 521, 531, 538, 549, 551, 557, 559), as does §5 line 783.
2. §7 line 973 uses it in the retired sense: "the failure window covers
   `r ∈ {1,2,3}`". That sense belonged to the deleted
   `Proposition [The failure window]`, and this is a dangling survivor of
   the same removal that orphaned *rebel*.

**`free` / `hard`** — emphasised as definitions twice: §4 line 374
(Definition 4.1, "the *free* and *hard* residues") and §10 line 1628, where
the terms are re-introduced with emphasis in the paragraph following
Lemma 10.1.

**`normal-play`** — emphasised three times in §10: lines 1643, 1661, 1819.
The first is a genuine contrast with misère; the later two repeat it.

## Counts

### Word count, Sections 1–5

**4,036 words**, over 216 sentences (lines 108–787, i.e. the Introduction
through the end of the Diagonal Theorem section). That figure excludes the
collapsed `MATH` and `REF` placeholders; counting each of those as one word
gives 4,849 tokens. The abstract is not included.

For scale, the whole body between the abstract and the bibliography is
**14,693 words** on the same convention, so Sections 1–5 are about 27% of
the prose.

### Ten most frequent non-mathematical content words

Whole body, stopwords and the `MATH`/`REF` placeholders removed. These are
English content words; "non-mathematical" is read as excluding symbols and
formulae, not as excluding the vocabulary of the subject.

| word | count |
|---|---|
| every | 166 |
| residue | 128 |
| class | 112 |
| move | 105 |
| game | 104 |
| position | 102 |
| set | 94 |
| square | 88 |
| exactly | 80 |
| lemma | 76 |

Next ten, for context: *hard* 73, *internal* 73, *grundy* 70, *free* 64,
*option* 60, *member* 58, *odd* 55, *theorem* 51, *let* 51, *legal* 50.

**One observation for the revision, not a recommendation.** *every* at 166
and *exactly* at 80 are the two most frequent non-noun content words in the
paper. Both are quantifier-emphasis words; a plain-language pass that
removes even a third of them would be the single largest register change
available, and it touches no mathematics.
