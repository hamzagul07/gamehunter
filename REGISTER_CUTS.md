# Register cuts — proposals for a plain-language pass (report only)

Produced 2026-09-06 against `paper/main.tex` at commit `5292faa`.
**`paper/main.tex` was read and not modified in any phase.** Everything here
is a proposal for the author to accept or reject; nothing has been applied.

Constraints taken from the brief: no new prose, no rewording that changes
meaning — only deletions of emphasis words, sentence splits, and unpacking of
dash asides. Where a proposal cannot be made under that constraint without a
small grammatical repair, the repair is named rather than smuggled in.

Sentence segmentation, `MATH`/`REF` collapsing and word counts follow the
method recorded in `REGISTER_AUDIT.md`.

## Headline

| phase | proposals | of which need a grammatical repair |
|---|---:|---:|
| 1 — cut *every* / *exactly* | 10 of 246 occurrences | 0 |
| 2 — split long sentences | 20 | 6 |
| 3 — unpack dash asides | 24 (9 promote, 15 parenthesise) | 8 |

**The main finding of Phase 1 is negative, and it corrects a suggestion I
made in the previous audit.** `REGISTER_AUDIT.md` observed that *every* (166)
and *exactly* (80) are the paper's most frequent non-noun content words and
said that cutting a third of them would be the largest available register
change. That was a claim about frequency, and it does not survive contact
with the sentences: **236 of the 246 occurrences are load-bearing.** *every*
is an English quantifier governing a singular noun, so deleting it is almost
never grammatical — "every internal option is N" cannot lose the word without
becoming "internal option is N". Only 10 occurrences are pure emphasis. The
frequency count was real; the inference from it was wrong.

## Phase 1 -- every occurrence of *every* and *exactly*

246 occurrences in 196 sentences: **every** 166, **exactly** 80.

| verdict | every | exactly | total |
|---|---:|---:|---:|
| KEEP | 164 | 72 | 236 |
| CUT | 2 | 8 | 10 |

### CUT -- 10 occurrences

**S1 (Introduction), line 180 — `exactly`** — intensifier on a simile; "as wild as" is identical

> The consequence closes a door: a classification theorem for mode-switching subtraction games with arbitrary mode sets would classify all subtraction games, so no such theorem exists to be proved --- one construction away from the solved family lies a class exactly as wild as subtraction games themselves.

**S7 (Degenerate moduli), line 1006 — `exactly`** — intensifier on the verb; the colon already promises the detail

> Legality transfers exactly: since the amounts and MATH are multiples of MATH while MATH , we have MATH and MATH .

**S10 (Misere play), line 1657 — `exactly`** — "as in Lemma/Theorem X" already carries it

> The last sentence is the point on which the section turns, and it is worth isolating: a position of MATH with no internal options is not terminal in the host, so the mis\`ere convention never reaches it, and it is labelled P by the vacuous clause exactly as in normal play.

**S10.2 (Misere 10.2), line 1804 — `exactly`** — "as in Lemma/Theorem X" already carries it

> At MATH a square divisible by MATH is divisible by MATH , hence of the form MATH , so the internal moves read MATH , with legality MATH equivalent to MATH ; this is subtract- MATH , which preserves the parity of MATH and splits into two interleaved copies of subtract-a-square in the half-index MATH , exactly as in Theorem~ REF (d).

**S11 (Further solved games), line 1911 — `exactly`** — intensifier on "as the congruence says"

> Rescue MATH present MATH ; the MATH is wasted exactly as the congruence says ( MATH mod MATH , landing MATH ).

**S11 (Further solved games), line 1924 — `every`** — third beat of a three-"every" cadence in one sentence

> The check came back stronger than required: not only does the predicted rescue sit in every row, every wasted square is wasted for the predicted reason --- its residue misses the survivor set, and every wasted landing is MATH or MATH , both -residues.

**S11 (Further solved games), line 2098 — `every`** — already quantified by "over every added amount" earlier in the sentence

> A sweep over every added amount from MATH to MATH matches the criterion's prediction in every case, and the breaks land where the converse says they must, at MATH and MATH for the amounts MATH and MATH .

**S12 (Discovery methodology), line 2237 — `exactly`** — intensifier on the verb; the colon already promises the detail

> Twice the instrument recorded numbers that no theory then existed to explain, and both entries were later derived exactly: the unexplained P-positions MATH in MATH and MATH in MATH are the images of Golomb's opening losing positions under the reindexings of Theorem~ REF , and the recorded preperiod MATH for MATH is one more than the rebel position MATH of Corollary~ REF .

**S12 (Discovery methodology), line 2248 — `exactly`** — intensifier on the verb; the colon already promises the detail

> Corollary~ REF --- that MATH enters the class-index Grundy sequence only through MATH --- was derived before it was swept, and a sweep across eight moduli then returned the collapse exactly: at each modulus, every healthy game with MATH produced one and the same class-index sequence, and the three exceptional games at MATH produced theirs.

**S13 (What is closed), line 2309 — `exactly`** — intensifier on a simile; "as wild as" is identical

> One construction away from the solved family lies a class exactly as wild as subtraction games themselves.

### KEEP -- 236 occurrences

Grouped by sentence; a sentence contributing more than one occurrence is
listed once with the count. No information is lost by the grouping.

**S0 (abstract), line 61 — `every`**

> In the diagonal family MATH , a position MATH permits the subtraction of any positive square at most MATH ; every other position permits only MATH .

**S0 (abstract), line 65 — `every`x2**

> For every MATH except MATH and every MATH , the P-positions are the MATH residue classes modulo MATH of the fallback chains' bottoms, together with the hard half of a finite set MATH read off a single parameter MATH --- the boundary position MATH when MATH , and a single rebel MATH at MATH .

**S0 (abstract), line 71 — `exactly`**

> Under mis\`ere play the chains invert and the exceptional positions are exactly the free half of the same set: one exception set, two conventions.

**S0 (abstract), line 90 — `every`**

> Every conjecture was machine-proposed from a census of roughly 3,000 games; twice, theory constructed afterwards rederived numbers the instrument had recorded before the theory existed.

**S1 (Introduction), line 124 — `every`**

> The protagonist is the two-parameter family MATH : from a position MATH a player may subtract any positive square not exceeding MATH ; from every other position the only move is to subtract MATH .

**S1 (Introduction), line 128 — `every`x2, `exactly`**

> The main outcome law can be tasted before any machinery arrives: for every MATH except MATH and every MATH , the P-positions of MATH are exactly MATH residue classes modulo MATH --- the bottoms of the game's fallback chains --- together with a finite exception set read off a single parameter, with no thresholds and no unverified zones.

**S1 (Introduction), line 135 — `every`**

> The Chain Lemma decomposes every fallback class into an independent chain whose P-positions alternate upward from a stuck bottom --- Grundy values MATH and MATH , nothing else, uniformly across the board's foreign territory.

**S1 (Introduction), line 139 — `exactly`**

> The MATH -duality lemma matches amounts to landings: an amount is useful from the square-mode class exactly when its residue modulo MATH avoids MATH and MATH , and the useful residues split into a hard set MATH and its shift, serving the class's two residues in complementary pairs.

**S1 (Introduction), line 144 — `every`**

> Its trichotomy is the paper's map: MATH for every healthy pair --- all MATH , MATH outside three exceptions --- while MATH at MATH and MATH at MATH .

**S1 (Introduction), line 154 — `exactly`**

> Behind the outcome argument sits a mechanism worth isolating, and Section~ REF states it for an arbitrary impartial game: if a set of positions has, off a finite bad prefix, external options realising exactly the Grundy values MATH and MATH , then its Grundy values are the internal game's values shifted by MATH , the periphery and the prefix invisible.

**S1 (Introduction), line 164 — `every`**

> Two corollaries calibrate how far outside the classical theory the family lives: no member is eventually periodic at the level of Grundy values, and each has bounded values if and only if MATH is bounded --- Golomb's Nim-dimension question, reproduced at every modulus.

**S1 (Introduction), line 195 — `exactly`**

> Section~ REF puts the machinery to work three times: MATH solved in full as the worked example; Foursquare --- the machine's first find, moves MATH with a square mode at MATH --- solved with its mechanism exposed and Kadam's Extension established; and a criterion determining exactly which enlargements of a mode's move set preserve a law.

**S1 (Introduction), line 206 — `every`**

> Every conjecture in this paper was machine-proposed, drawn from a census of roughly three thousand games; the instrument that proposed them constructs no proofs, and Section~ REF documents the pipeline, the verification regime, and the written protocol governing its use.

**S2 (Preliminaries), line 231 — `every`**

> A terminal position (no legal moves) is a -position; a position is an -position if and only if at least one legal move reaches a -position; a position is a -position if and only if every legal move reaches an -position, the terminal case satisfying this clause vacuously.

**S2 (Preliminaries), line 241 — `every`x2, `exactly`**

> If (i) every terminal position lies in MATH , (ii) no move from a position in MATH leads to a position in MATH , and (iii) from every position not in MATH some move leads to a position in MATH , then MATH is exactly the set of -positions.

**S2 (Preliminaries), line 265 — `every`**

> So every table is MATH plus mirrors, plus the MATH from MATH .

**S2 (Preliminaries), line 293 — `every`**

> The mod- MATH and mod- MATH rows are the diagnosis written out: $ (4) = \ 0, 1\ MATH (8) = \ 0, 1, 4\ $ both sit entirely inside the triple MATH , so their complements swallow every value any hard set will ever contain (Section~ REF ) --- the degeneracy of MATH and MATH is visible in these two rows before any game logic starts.

**S3 (Chain Lemma), line 307 — `every`**

> In MATH , for every position MATH with MATH : MATH

**S3 (Chain Lemma), line 314 — `exactly`**

> A rung is never MATH , so its only allowed move is the fallback MATH , legal exactly when MATH and landing on rung MATH ; rung MATH has no move at all, and no move ever leaves the progression.

**S3 (Chain Lemma), line 320 — `every`**

> Since Closure makes every option of a rung another rung, the chain computes its statuses as if the rest of the game had been deleted.

**S3 (Chain Lemma), line 328 — `exactly`**

> MATH is even exactly when MATH , so the P-positions of class MATH are precisely the MATH .

**S3 (Chain Lemma), line 338 — `every`**

> \] In particular every position outside class MATH has Grundy value MATH or MATH .

**S3 (Chain Lemma), line 343 — `exactly`**

> By the Closure and Independence steps of Lemma~ REF , class MATH is a path under the single move MATH , and rung MATH has exactly one option, rung MATH , for MATH , and none for MATH .

**S3 (Chain Lemma), line 349 — `exactly`**

> Translating as in Lemma~ REF , MATH is even exactly when MATH .

**S4 (Escape / s_min), line 360 — `every`**

> Lemma~ REF and Corollary~ REF settle every class except MATH .

**S4 (Escape / s_min), line 372 — `exactly`**

> The class MATH splits modulo MATH into exactly the two residues MATH and MATH , which we call the free and hard residues; when MATH these are MATH and MATH .

**S4 (Escape / s_min), line 392 — `every`**

> With this convention every statement below is uniform in MATH .

**S4 (Escape / s_min), line 412 — `every`x2**

> (iv) MATH for every MATH and every MATH .

**S4 (Escape / s_min), line 418 — `exactly`**

> Any MATH consecutive integers contain exactly one multiple of MATH , never none and never two.

**S4 (Escape / s_min), line 429 — `exactly`**

> Each window contains exactly one multiple of MATH , and two multiples of MATH that are distinct modulo MATH are congruent to MATH and to MATH in some order.

**S4 (Escape / s_min), line 454 — `exactly`**

> First, the partition (ii) says an amount can leave class MATH exactly when its residue modulo MATH is neither MATH nor MATH : the exclusions formerly listed one by one are the two-element complement of MATH .

**S4 (Escape / s_min), line 500 — `every`x2**

> For every MATH and every MATH , the interval MATH contains a perfect square, with a single exception: at MATH the interval MATH contains none.

**S4 (Escape / s_min), line 517 — `exactly`**

> Exactly one of the following holds:

**S4 (Escape / s_min), line 519 — `every`**

> (a) (healthy) MATH --- the case for every MATH with MATH and MATH ; moreover MATH , so the certifying square lies in the window MATH ;

**S4 (Escape / s_min), line 523 — `exactly`**

> (b) (exceptional) MATH --- exactly the pairs MATH , where MATH against MATH ;

**S4 (Escape / s_min), line 526 — `every`, `exactly`**

> (c) (degenerate) MATH --- exactly the moduli MATH , for every MATH .

**S4 (Escape / s_min), line 531 — `every`**

> Indeed, a square MATH has residue MATH (as MATH ), and every residue in MATH exceeds MATH when read in MATH --- its elements are MATH for MATH and MATH for MATH --- so MATH and squares up to MATH never certify.

**S4 (Escape / s_min), line 536 — `exactly`x2**

> A square MATH with MATH has residue MATH , which lies in MATH exactly when MATH is not a multiple of MATH ; the window contains exactly one multiple of MATH (any MATH consecutive integers do), namely MATH itself when MATH and MATH when MATH , and if MATH its residue is MATH .

**S4 (Escape / s_min), line 549 — `every`**

> By Lemma~ REF the window contains a square, so by the equivalence, (a) can fail only if every square in the window is the multiple MATH .

**S4 (Escape / s_min), line 559 — `exactly`**

> The window MATH is nonempty exactly when MATH , i.e.\ MATH ; MATH gives MATH , excluded, and MATH gives MATH with MATH --- the set MATH .

**S4 (Escape / s_min), line 561 — `every`**

> So (a) holds for every MATH , MATH with MATH .

**S4 (Escape / s_min), line 592 — `every`**

> Consequently no member of MATH has a legal square move divisible by MATH , and every internal option of a member of MATH lies in MATH and on the opposite residue modulo MATH .

**S4 (Escape / s_min), line 602 — `every`**

> For the consequence: a square divisible by MATH has size at least MATH , hence exceeds every member of MATH and is illegal from all of them.

**S4 (Escape / s_min), line 604 — `every`, `exactly`**

> An internal move --- a square MATH --- has residue MATH or MATH modulo MATH ; the residue- MATH case is exactly divisibility by MATH , just excluded, so within MATH every internal move has residue MATH , and by Lemma~ REF (iii) it exchanges the two residues of the class while landing on a smaller class member, which lies in MATH since MATH is an initial segment of the class.

**S4 (Escape / s_min), line 627 — `every`x2**

> (ii) Every member of MATH has Grundy value MATH , and every member of MATH has Grundy value MATH .

**S4 (Escape / s_min), line 630 — `every`**

> (iii) Every internal option of a member of MATH lies in MATH , on the opposite residue modulo MATH .

**S4 (Escape / s_min), line 642 — `every`**

> The regime values: for healthy MATH , MATH gives MATH ; for healthy MATH , every square up to MATH has residue at most MATH , outside MATH , so MATH , while MATH as in Lemma~ REF --- hence MATH , with MATH hard and MATH free; for MATH , MATH with MATH gives MATH , so MATH with the free--hard--free pattern MATH , MATH , MATH .

**S4 (Escape / s_min), line 665 — `every`x2**

> If MATH , then MATH , so the option set is nonempty; every external option is a bottom of value MATH , and every internal option is a member of MATH , of value MATH by induction.

**S4 (Escape / s_min), line 668 — `every`x2**

> If MATH with MATH , every external option is a top rung of value MATH , and every internal option is a member of MATH , of value MATH by induction; hence MATH .

**S5 (Diagonal Theorem), line 684 — `exactly`**

> The P-positions of MATH are exactly the elements of \[ S = \ \, n 0 : n b 2m for some b B \,\ Bad _h(m,r).

**S5 (Diagonal Theorem), line 687 — `every`**

> \] The law holds for every MATH , with no preperiod and no unverified zones.

**S5 (Diagonal Theorem), line 689 — `exactly`**

> The hypothesis on MATH enters exactly once, through the finiteness of MATH (Lemma~ REF and Proposition~ REF ).

**S5 (Diagonal Theorem), line 696 — `exactly`**

> A position outside class MATH is terminal exactly when it is the bottom rung of its chain, that is, one of the positions MATH themselves: these satisfy MATH , so the fallback is illegal, and they are not in squares mode.

**S5 (Diagonal Theorem), line 699 — `exactly`**

> A class- MATH position MATH has the legal square MATH , so the only class- MATH terminal is MATH , which is in class MATH exactly when MATH ; there it is the least member of the hard residue and, since MATH (Remark~ REF ), lies in MATH .

**S5 (Diagonal Theorem), line 704 — `every`**

> Every terminal position therefore lies in MATH .

**S5 (Diagonal Theorem), line 710 — `every`**

> From a member MATH of MATH : every square legal at MATH is smaller than MATH , hence has residue outside MATH by the minimality in Definition~ REF , hence, by the partition of Lemma~ REF (ii), has residue MATH , MATH , or in MATH .

**S5 (Diagonal Theorem), line 731 — `every`**

> Every position outside MATH has a move into MATH .

**S5 (Diagonal Theorem), line 733 — `exactly`**

> By Lemma~ REF , MATH is exactly the set of P-positions of MATH .

**S5 (Diagonal Theorem), line 776 — `every`, `exactly`**

> For odd MATH , $(m - 1)^2 = m^2 - 2m + 1 m^2 + 1 m + 1 2m MATH m^2 m MATH m + 1$ belongs to every hard set, landing the hard residue exactly on bottom MATH ( MATH when MATH ).

**S6 (Transfer Principle), line 794 — `every`**

> Two consequences follow in later sections: the Grundy values of every solved member of the diagonal family are a shift of Golomb's nim-sequence, and an arbitrary subtraction game can be embedded as a mode class of a mode-switching host.

**S6 (Transfer Principle), line 827 — `every`**

> (H1) (palette) every MATH has an external option of Grundy value MATH and an external option of Grundy value MATH ;

**S6 (Transfer Principle), line 830 — `every`x2**

> (H2) (ceiling) every external option of every MATH has Grundy value MATH or MATH ;

**S6 (Transfer Principle), line 833 — `every`x2**

> (H3) (prefix) every MATH has MATH , and every internal option of a member of MATH lies in MATH .

**S6 (Transfer Principle), line 836 — `every`**

> Then MATH for every MATH , and the function MATH on MATH satisfies \[ h(p) = mex \ \, h(q) : q an internal option of p with q Bad \,\ .

**S6 (Transfer Principle), line 845 — `every`**

> Let MATH and assume the conclusion at every member of MATH below MATH .

**S6 (Transfer Principle), line 851 — `every`**

> By (H2), every external option of MATH contributes a value in MATH and hence nothing to MATH .

**S6 (Transfer Principle), line 854 — `exactly`**

> An internal option MATH with MATH lies in MATH and is below MATH , so by the induction hypothesis MATH , and it contributes exactly that value.

**S6 (Transfer Principle), line 890 — `every`**

> The first prevents a member of MATH from masquerading as a good position: a single MATH with MATH would inject a phantom value into MATH at every good position having MATH as an option, and the identification of MATH with the internal Grundy function would fail there and everywhere above it.

**S6 (Transfer Principle), line 894 — `every`**

> The second clause is not needed for Theorem~ REF itself but for the step that follows every application of it --- the identification of the internal game on MATH with a translate of the internal game on MATH .

**S6 (Transfer Principle), line 913 — `exactly`**

> If MATH and MATH , the same two lines give MATH ; and if (H1) and (H2) are replaced by the requirement that the external options of a good position realise exactly the values MATH and never exceed them, and (H3) by MATH on MATH , then the conclusion becomes MATH on MATH with MATH satisfying the same internal recursion.

**S7 (Degenerate moduli), line 929 — `exactly`**

> Theorem~ REF excludes exactly two moduli, and this section proves the exclusion is not a limitation of the method but a fact about squares: at MATH and MATH there is no rescue to find, and the affected classes turn inward.

**S7 (Degenerate moduli), line 935 — `every`**

> For MATH and every MATH : MATH , while MATH excludes MATH , MATH , and MATH (Definition~ REF ).

**S7 (Degenerate moduli), line 936 — `every`**

> Hence no square move from a hard-residue position reaches a foreign bottom: every move stays inside class MATH or lands on an -position of a foreign chain.

**S7 (Degenerate moduli), line 944 — `every`x2**

> For MATH and every MATH : MATH --- read directly off the mod- MATH and mod- MATH rows of Table~ REF --- while every hard set MATH excludes MATH , MATH , and MATH (Definition~ REF ).

**S7 (Degenerate moduli), line 947 — `every`**

> Hence from any hard-residue position, every legal square move either stays inside class MATH (a square $ 0 MATH m MATH 2m MATH 0 MATH m$) or lands one below on the odd rung above a bottom (a square MATH ), an -position --- never on a -position of a foreign chain.

**S7 (Degenerate moduli), line 969 — `exactly`**

> The two degenerate moduli are exactly the two the parity-free engine cannot serve.

**S7 (Degenerate moduli), line 972 — `every`**

> At MATH the engine convicts every class from the outside: the failure window covers MATH , and the MATH interval MATH is square-free.

**S7 (Degenerate moduli), line 991 — `every`**

> Every MATH is odd, MATH , or a multiple of MATH ; we dispatch each kind from a hard-class position MATH .

**S7 (Degenerate moduli), line 997 — `every`**

> If MATH then MATH : at MATH this is MATH and the move stays in the class, while at MATH the landing MATH is the free residue ( MATH , or MATH when MATH ), every member of which is N because it subtracts MATH onto the foreign bottom directly beneath it --- P by Lemma~ REF , legal from the smallest free member.

**S7 (Degenerate moduli), line 1003 — `every`x2**

> In the index MATH the internal moves read: at MATH , every even MATH subtracts MATH , i.e.\ MATH ; at MATH , every MATH subtracts MATH , i.e.\ MATH .

**S7 (Degenerate moduli), line 1011 — `every`**

> The three-way sort is genuinely three-way only at MATH : modulo MATH the values MATH and MATH collapse into one residue, so at MATH parity alone decides --- every even square stays internal --- which is why MATH hosts Golomb's game whole while MATH , whose middle class defects to the free residue, keeps only the doubled cousin subtract- MATH .

**S7 (Degenerate moduli), line 1017 — `exactly`**

> At MATH the index game has the single internal-terminal MATH ; at MATH it has MATH and MATH (the smallest internal move needs MATH ) --- matching the terminal sets of subtract-a-square and subtract- MATH exactly.

**S7 (Degenerate moduli), line 1020 — `every`**

> For MATH these positions have real moves, but by (a) every one of them exits onto an N-position; for MATH the alignment is literal: MATH , so MATH is MATH , a moveless position --- Golomb's own terminal in the flesh.

**S7 (Degenerate moduli), line 1024 — `every`**

> The status of a position is determined by its options alone, and by (a) every exiting option is N; so a hard-class position is P iff all of its internal options are N, and N iff some internal option is P --- exits can neither supply a P-witness nor block one.

**S7 (Degenerate moduli), line 1028 — `exactly`**

> By induction on MATH , the map MATH therefore satisfies exactly the recursion of the subtraction game with the option sets of (a).

**S7 (Degenerate moduli), line 1032 — `every`**

> In subtract- MATH every move is even, so the parity of MATH is invariant, and on each parity class the move MATH reads MATH in the half-index MATH (legality MATH on both parities), with terminal MATH on each side: two interleaved, independent copies of Golomb's game, so MATH is P iff MATH .

**S7 (Degenerate moduli), line 1047 — `every`**

> The instrument had been filing Golomb's sequence under two aliases for the entire census --- while re-deriving that very sequence as a calibration classic before every session.

**S7 (Degenerate moduli), line 1061 — `every`**

> For MATH and every MATH , the set of P-positions of MATH is not eventually periodic.

**S7 (Degenerate moduli), line 1077 — `every`**

> The argument is folklore for any subtraction set containing a multiple of every integer; we include it to keep the paper self-contained.

**S7 (Degenerate moduli), line 1083 — `every`, `exactly`**

> Every legal square from MATH is at most MATH , because MATH overshoots MATH by exactly MATH ; and MATH , because MATH and MATH .

**S7 (Degenerate moduli), line 1085 — `every`**

> So every option of MATH lands at MATH , all N by supposition, making MATH itself a P-position at or beyond MATH --- contradicting the supposition.

**S7 (Degenerate moduli), line 1092 — `every`x2**

> Periodicity walks membership up MATH 's own progression: MATH , then MATH , and so on, every intermediate point lying at or above MATH , so every step is licensed.

**S7 (Degenerate moduli), line 1103 — `every`**

> For MATH and every MATH , the set of P-positions inside the confined class contains no two elements differing by a perfect square.

**S7 (Degenerate moduli), line 1112 — `exactly`**

> Density zero is then the Furstenberg--S\'ark\"ozy theorem REF , which says exactly that a set of integers avoiding square differences has density zero.

**S7 (Degenerate moduli), line 1120 — `every`**

> Every MATH in MATH is either in MATH or wins by one square move onto some MATH below it; a fixed MATH can serve at most MATH positions this way, one per square, plus itself.

**S7 (Degenerate moduli), line 1135 — `every`x2**

> For every MATH and every MATH , the P-set of MATH has asymptotic density MATH .

**S7 (Degenerate moduli), line 1143 — `exactly`**

> For MATH , MATH , Theorem~ REF lists the P-set as exactly MATH residue classes modulo MATH together with finitely many named positions, and MATH classes out of MATH carry density MATH .

**S8 (Grundy Transfer), line 1180 — `exactly`**

> Writing MATH , the amount is MATH , so in the class index the internal moves read MATH , legal exactly when MATH .

**S8 (Grundy Transfer), line 1193 — `exactly`**

> Deleting MATH from the internal game and re-basing each copy, the copy MATH loses an initial run of exactly MATH half-indices when MATH , and none when MATH .

**S8 (Grundy Transfer), line 1200 — `every`x2**

> Then MATH if and only if MATH for every MATH , if and only if MATH for every MATH , if and only if MATH .

**S8 (Grundy Transfer), line 1220 — `every`x3**

> MATH says every exponent is even, i.e.\ MATH is a square; MATH says every exponent is odd and the product of the odd-exponent primes is MATH , which forces every exponent to be MATH .

**S8 (Grundy Transfer), line 1226 — `exactly`**

> Such a MATH lies in MATH exactly when MATH , that is MATH , that is MATH .

**S8 (Grundy Transfer), line 1272 — `every`**

> For the second claim, MATH for every healthy MATH by Proposition~ REF (i), and MATH for each member of MATH .

**S8 (Grundy Transfer), line 1280 — `every`**

> Then for every class- MATH position MATH with MATH , \[ G(n) = 2 + \!

**S8 (Grundy Transfer), line 1290 — `every`**

> The induction of Theorem~ REF requires the option relation on MATH to be well-founded, which it is: every move of MATH subtracts a positive amount, so options are positions of strictly smaller value in a set of non-negative integers.

**S8 (Grundy Transfer), line 1301 — `exactly`**

> (H3) holds by Proposition~ REF (ii)--(iii), whose two clauses are exactly the two clauses of the hypothesis.

**S8 (Grundy Transfer), line 1321 — `every`x2**

> For every MATH , MATH , and every MATH , the Grundy sequence of MATH is not eventually periodic.

**S8 (Grundy Transfer), line 1337 — `every`x2**

> For every MATH , MATH , and every MATH , the Grundy sequence of MATH is bounded if and only if MATH is bounded; and if bounded, MATH .

**S8 (Grundy Transfer), line 1342 — `every`**

> Outside class MATH the values are MATH and MATH by Corollary~ REF ; inside class MATH they are MATH beyond a finite set by Theorem~ REF , and the argument of MATH ranges over all sufficiently large integers on the copy MATH , which is nonempty for every MATH since it contains MATH .

**S9 (Universal Embedding), line 1373 — `every`**

> The host MATH is the mode-switching game on MATH in which a position MATH may have subtracted any amount of the mode set MATH , and every other position may have subtracted only MATH ; play is normal.

**S9 (Universal Embedding), line 1388 — `every`**

> In MATH with either mode set, and for every class- MATH position MATH :

**S9 (Universal Embedding), line 1391 — `every`**

> (i) Every amount MATH is internal: the landing MATH lies in class MATH and on the same residue modulo MATH .

**S9 (Universal Embedding), line 1400 — `exactly`**

> (iv) The class index MATH defined by MATH , where MATH is the least member of the residue in question, transports the internal moves to MATH , legal exactly when MATH .

**S9 (Universal Embedding), line 1417 — `every`**

> Note that the two residues of class MATH do not communicate: by (i) every internal move preserves the residue modulo MATH , so the free half and the hard half of the class are separate boards.

**S9 (Universal Embedding), line 1419 — `exactly`**

> That is what makes the embedding clean; in the diagonal family the same disconnection occurs exactly when MATH is even, since internal moves preserve MATH modulo MATH (Proposition~ REF (i)) and the parity of MATH is the free--hard alternation (Proposition~ REF (i)).

**S9 (Universal Embedding), line 1429 — `exactly`**

> Then the P-positions of the host are exactly

**S9 (Universal Embedding), line 1439 — `every`**

> On the free residue, the move MATH is legal from the least free member onward (indeed always, since MATH ) and lands on a foreign bottom by Lemma~ REF (ii), a P-position; so every free member is N.

**S9 (Universal Embedding), line 1464 — `exactly`**

> At MATH the squares have residues in MATH modulo MATH , so the mode set of MATH acts on class MATH exactly as MATH does with MATH the squares: the amounts MATH are internal, the amounts MATH land as in Lemma~ REF (ii).

**S9 (Universal Embedding), line 1477 — `every`**

> (i) (Hard residue: exact.) For every MATH , MATH When MATH the hard residue has one further member, MATH , which is terminal and satisfies MATH .

**S9 (Universal Embedding), line 1482 — `every`**

> (ii) (Free residue: one-step prefix.) MATH , and for every MATH , MATH

**S9 (Universal Embedding), line 1486 — `every`**

> The embedding is thus exact on the progression MATH for every MATH and MATH , and exact on the free residue from its second member onward.

**S9 (Universal Embedding), line 1491 — `every`x2**

> By Lemma~ REF (i) every internal move preserves the residue modulo MATH , so the free and hard halves of class MATH are separate boards and Theorem~ REF may be applied to each; the option relation is well-founded since every move subtracts a positive amount.

**S9 (Universal Embedding), line 1527 — `exactly`**

> Theorem~ REF gives, after deleting the initial index MATH and re-basing at MATH , MATH for MATH --- that is, writing MATH with MATH , exactly the identity of (i).

**S9 (Universal Embedding), line 1538 — `every`**

> Both are absorbed as one-element MATH sets, and both disappear under cosmetic changes we do not make: the theorem's content is the progression based at MATH , where the embedding is exact with no prefix for every MATH and MATH --- the formal statement of the prefix- MATH observation recorded by the search instrument, now with its base point made explicit.

**S9 (Universal Embedding), line 1547 — `every`**

> For every nonempty MATH there is a mode-switching subtraction game whose Grundy function, restricted to an arithmetic progression and shifted by MATH , is that of MATH .

**S9 (Universal Embedding), line 1565 — `every`**

> Taking MATH in Theorem~ REF gives a mode-switching game whose Grundy sequence is MATH on the hard residue, for every MATH --- including MATH and MATH , where the diagonal family itself achieves only the outcome-level embedding of Section~ REF for want of the second palette witness.

**S10 (Misere play), line 1597 — `every`**

> A terminal position is therefore an N-position, and every other position is P if and only if all of its options are N.

**S10 (Misere play), line 1617 — `exactly`x2**

> Rung MATH has the single option rung MATH , so it is MATH exactly when rung MATH is MATH ; by induction rung MATH is MATH exactly when MATH is odd, which is to say MATH .

**S10 (Misere play), line 1639 — `every`x2**

> (M2) every external option of every MATH is MATH .

**S10 (Misere play), line 1641 — `every`**

> Then for MATH , MATH is MATH if and only if every internal option of MATH is MATH --- that is, the mis\`ere outcomes on MATH are the normal-play outcomes of the game played on MATH by internal moves alone.

**S10 (Misere play), line 1647 — `exactly`x2**

> By (M1) the terminal clause does not apply to MATH , so MATH is MATH exactly when all of its options are MATH ; by (M2) the external ones are MATH unconditionally, so this holds exactly when all internal options are MATH .

**S10 (Misere play), line 1650 — `every`**

> Reading " MATH " as the label of the internal game, the recursion is: a position of MATH is labelled P when every internal option is labelled N, and an internal-terminal position of MATH --- one with no internal option --- is labelled P vacuously.

**S10.1 (Misere 10.1), line 1672 — `exactly`**

> Under mis\`ere play the P-positions of MATH are exactly

**S10.1 (Misere 10.1), line 1692 — `every`**

> Every hard member is therefore MATH , with no size condition and no exception.

**S10.1 (Misere 10.1), line 1700 — `every`**

> By the definition of MATH no legal square of MATH has residue in MATH , so by Lemma~ REF (ii)--(iii) every legal square is either internal or of residue in MATH ; the latter carries the free residue onto a bottom, which is MATH by Lemma~ REF .

**S10.1 (Misere 10.1), line 1707 — `every`**

> Every option of MATH is therefore MATH , and MATH is MATH .

**S10.1 (Misere 10.1), line 1721 — `exactly`x2**

> For MATH , MATH , the P-positions of MATH outside the periodic law are, in normal play, exactly the hard members of MATH , and in mis\`ere play exactly the free members of MATH .

**S10.1 (Misere 10.1), line 1728 — `every`**

> For normal play, Proposition~ REF (ii) assigns Grundy value MATH to the hard members of MATH and MATH to the free members, so the former are P-positions and the latter are not; and by Theorem~ REF every class- MATH position at or above MATH has Grundy value at least MATH .

**S10.1 (Misere 10.1), line 1737 — `exactly`**

> In a healthy game with MATH , MATH is the single free position MATH , so normal play has no exceptional P-position at all and mis\`ere has exactly one.

**S10.2 (Misere 10.2), line 1766 — `every`**

> (i) every hard member of class MATH is MATH ;

**S10.2 (Misere 10.2), line 1781 — `every`**

> An odd square has residue MATH , which lies in MATH by Lemma~ REF (iv), so it carries the hard residue onto a top rung, MATH by Lemma~ REF ; and an odd square is legal at every MATH .

**S10.2 (Misere 10.2), line 1795 — `every`x2**

> Hence every external option of a member of MATH , and every option leaving MATH , is MATH , and Lemma~ REF applies: the mis\`ere outcomes on MATH are the normal-play outcomes of the internal game on MATH .

**S10.2 (Misere 10.2), line 1812 — `exactly`**

> (iii) Theorem~ REF states that the normal-play P-positions of class MATH are exactly MATH for MATH .

**S10.2 (Misere 10.2), line 1813 — `exactly`**

> By (ii) the mis\`ere MATH -positions are exactly MATH for MATH .

**S10.2 (Misere 10.2), line 1834 — `every`**

> For MATH and every MATH , the mis\`ere P-set of MATH is not eventually periodic; the confined free class contains no two elements differing by a perfect square, hence has asymptotic density zero, while retaining at least MATH members up to MATH ; and the mis\`ere P-set has asymptotic density MATH .

**S11 (Further solved games), line 1867 — `exactly`**

> The P-positions of MATH are exactly the $n 0, 1, 3, 4 10 $.

**S11 (Further solved games), line 1873 — `exactly`**

> A squares-mode position --- MATH --- always has the legal move MATH , since the smallest such position is MATH ; a fallback position has its only move MATH exactly when MATH .

**S11 (Further solved games), line 1879 — `every`**

> Every element of MATH is $ 0, 1, 3, 4 10 MATH 0, 1, 3, 4 5$: no candidate lies in class MATH , so a candidate's only move is the fallback MATH , whose landings occupy the residues MATH --- all outside MATH .

**S11 (Further solved games), line 1893 — `every`**

> Every position outside MATH has a move into MATH --- and the verification consumes only the two instances MATH and MATH ; no general fact about squares is invoked.

**S11 (Further solved games), line 1896 — `every`, `exactly`**

> By Lemma~ REF , MATH is exactly the set of P-positions of MATH : the law holds for every MATH , with no preperiod --- and the P-set consists of the bottom classes alone, for the reason recorded in Remark~ REF .

**S11 (Further solved games), line 1904 — `every`**

> Prediction first, then the rows: residue- MATH positions ( MATH ) should be rescued by any legal square MATH or MATH , residue- MATH positions ( MATH ) by any square MATH or $6 10 $, and every other square should be wasted.

**S11 (Further solved games), line 1924 — `every`x2**

> The check came back stronger than required: not only does the predicted rescue sit in every row, every wasted square is wasted for the predicted reason --- its residue misses the survivor set, and every wasted landing is MATH or MATH , both -residues.

**S11 (Further solved games), line 1933 — `every`**

> For every game with finite MATH the P-set is, by Theorem~ REF , the union of the bottom classes and MATH .

**S11 (Further solved games), line 1935 — `every`**

> When MATH is empty --- every healthy game with MATH --- the P-set is the bottom classes alone, which is the coincidence observed above for MATH ; at MATH and on MATH the set MATH contributes its single position; and at the degenerate moduli, where MATH , the class- MATH contribution is the infinite confined set of Section~ REF .

**S11 (Further solved games), line 1954 — `every`, `exactly`**

> Let MATH ; since MATH and its complement are unions of residue classes modulo MATH , every position lies in exactly one of the two.

**S11 (Further solved games), line 1958 — `every`**

> The positions MATH and MATH are standard-mode (both MATH ) and every allowed move MATH exceeds them, so both are terminal.

**S11 (Further solved games), line 1960 — `every`x2**

> Conversely, every standard-mode MATH has the legal move MATH , and every square-mode MATH has the legal move MATH , since square mode requires MATH and hence MATH .

**S11 (Further solved games), line 1962 — `exactly`**

> The terminal set is therefore exactly MATH , and both members lie in MATH .

**S11 (Further solved games), line 1964 — `every`**

> Every element of MATH is even, hence MATH , hence standard-mode, so its moves are among MATH .

**S11 (Further solved games), line 1985 — `every`**

> Every position outside MATH therefore has a move into MATH --- and the verification consumes only the two instances MATH and MATH ; no general fact about squares is invoked.

**S11 (Further solved games), line 1988 — `every`, `exactly`**

> By Lemma~ REF , MATH is exactly the set of P-positions of Foursquare: the law MATH holds for every MATH , with no preperiod.

**S11 (Further solved games), line 1994 — `every`**

> Every odd square is congruent to MATH or MATH modulo MATH : writing MATH , the product MATH is even, so $4m(m+1) 0 MATH 8 16 $.

**S11 (Further solved games), line 2009 — `exactly`**

> Proposition~ REF and Remark~ REF answer the same question for a mode-switching game, at the level of P-positions: the additions Foursquare tolerates are exactly the odd moves and the governor's clones MATH , and the parity-and-residue argument that certifies them does for mode-switching games the job that reversibility did classically.

**S11 (Further solved games), line 2017 — `every`**

> Let MATH be Foursquare with its standard-mode move set enlarged from MATH to every MATH or MATH with MATH , square mode unchanged.

**S11 (Further solved games), line 2019 — `exactly`**

> Then the P-positions of MATH are exactly MATH --- identical to Foursquare's.

**S11 (Further solved games), line 2028 — `every`x2, `exactly`**

> From a candidate position --- even, hence standard mode --- every legal move of MATH subtracts some MATH or MATH , and the closure argument of Theorem~ REF consumed exactly two facts about MATH , its parity and its residue modulo MATH , never its actual size, so it transfers verbatim to every member of the extended family: the MATH and MATH moves are odd and land on odd residues, none of which lie in the all-even candidate, while the MATH moves land on MATH , also outside --- no move from the candidate returns to it.

**S11 (Further solved games), line 2037 — `every`x2**

> In the other direction, the extended move set contains the original one and square mode is untouched, so every escape witness of the original proof --- the standard moves and the squares MATH and MATH --- remains a legal move of MATH with the same landing, and a move set that only grows cannot lose an escape: every position outside the candidate still has its move into it.

**S11 (Further solved games), line 2050 — `exactly`**

> The law survives if and only if no P-position has another P-position exactly MATH below it, with both positions in the enlarged mode.

**S11 (Further solved games), line 2055 — `every`**

> Adding moves can only affect closure, never escape: every old witness remains legal with the same landing, so condition (iii) of Lemma~ REF survives untouched, and condition (i) can only shrink the terminal set, which the hypothesis of no preperiod already places inside the candidate.

**S11 (Further solved games), line 2065 — `every`**

> We claim every position below MATH keeps its original status in the enlarged game, by strong induction.

**S11 (Further solved games), line 2066 — `every`**

> A position MATH with MATH has all of its old options outside MATH , hence N-positions by the induction hypothesis; its possible new option MATH --- present only when MATH is in the enlarged mode --- cannot lie in MATH , since that would contradict the minimality of MATH ; so every option of MATH is an N-position and MATH remains a P-position.

**S11 (Further solved games), line 2090 — `every`, `exactly`**

> In Foursquare every P-position is standard-mode, so the scoping is invisible and the criterion reduces to a residue condition: an added amount is harmless exactly when it is not congruent modulo MATH to a difference of two elements of MATH .

**S11 (Further solved games), line 2093 — `exactly`**

> Those differences are MATH , so the harmless amounts are exactly the odd ones and those MATH --- the governor's clones.

**S11 (Further solved games), line 2098 — `every`**

> A sweep over every added amount from MATH to MATH matches the criterion's prediction in every case, and the breaks land where the converse says they must, at MATH and MATH for the amounts MATH and MATH .

**S11 (Further solved games), line 2129 — `every`, `exactly`**

> Here is the number-theoretic heart at its true address: odd squares modulo MATH take exactly two values, MATH and MATH (Remark~ REF ), and the second is load-bearing precisely at residues MATH and MATH --- the square-mode residues, no others --- while modulo MATH every odd square is MATH and those residues would be stranded: the same poverty of squares modulo powers of two that confines MATH and MATH , one refinement up and just barely wealth enough.

**S11 (Further solved games), line 2144 — `every`x2, `exactly`**

> The mechanism classifies tampering as well: an enlargement of the standard set leaves the P-set fixed exactly when every added move is either odd, landing, from any candidate position, on the all-N odd world, or MATH , a clone of the governor --- verified: MATH , MATH , and MATH preserve the law, MATH , MATH , and MATH break it at MATH , and the maximal enlargement, every odd number plus the whole clone class, holds to MATH .

**S11 (Further solved games), line 2164 — `every`, `exactly`**

> Then the P-positions are exactly the even integers, and the Grundy sequence is the same for every odd MATH --- the fallback evaporates.

**S11 (Further solved games), line 2169 — `exactly`**

> An even position has at most one option, MATH , which is odd since MATH is odd and is legal exactly when MATH .

**S11 (Further solved games), line 2175 — `every`**

> Part (i): every even MATH has MATH .

**S11 (Further solved games), line 2182 — `every`**

> Part (ii): every odd MATH has MATH .

**S11 (Further solved games), line 2187 — `exactly`**

> The two parts induct together on MATH , each invoking the other only at strictly smaller positions, so the joint induction is legitimate and the P-positions --- the positions of Grundy value MATH --- are exactly the even integers.

**S11 (Further solved games), line 2197 — `every`x2**

> By induction the entire Grundy sequence is therefore identical for every odd fallback MATH : the parameter is invisible to the game, because the squares already supply, from every odd position, a move to an even one, and the fallback can only ever move between residues that Part (i) has already flattened.

**S12 (Discovery methodology), line 2212 — `every`**

> Every law survived six adversarial verification passes at depths MATH and MATH without a failure, and a deeper rescan of the MATH resistant games converted only MATH .

**S12 (Discovery methodology), line 2215 — `every`**

> Before and after every session the engine re-derives five classical laws --- the subtraction game MATH and Golomb's subtract-a-square among them --- so that drift anywhere in the stack would announce itself in the classics first.

**S12 (Discovery methodology), line 2248 — `every`**

> Corollary~ REF --- that MATH enters the class-index Grundy sequence only through MATH --- was derived before it was swept, and a sweep across eight moduli then returned the collapse exactly: at each modulus, every healthy game with MATH produced one and the same class-index sequence, and the three exceptional games at MATH produced theirs.

**S12 (Discovery methodology), line 2257 — `every`**

> And once, theory corrected a reading rather than confirming it: the embedding sweeps behind Section~ REF reported hard-side exactness for every index, which was true of an index based at the second member and false at the first --- the base-point clause of Theorem~ REF exists because the proof caught what a base-blind sweep could not.

**S13 (What is closed), line 2301 — `every`**

> Where the palette exists, the law is complete and threshold-free, and Corollary~ REF shows that even there the constraint is an outcome-level phenomenon only: every solved member of the family escapes the classical periodicity theory at the level of Grundy values.

**S* (Acknowledgments), line 2336 — `every`x2**

> The author directed that work, refereed and corrected every draft, verified every claim against independent computation, and takes sole responsibility for the correctness of what is stated here; individual results and remarks elsewhere in the paper come from the same dialogue, as do the results of Section~ REF .

**S* (Acknowledgments), line 2341 — `every`**

> The search instrument and every verification run are the author's own.


## Phase 2 — splits for the twenty longest sentences

Proposals only. Each reuses the existing words; where a split forces a
grammatical repair, it is marked **[repair]** and named, because those go
beyond "conjunctions and pronouns" and need your approval separately. The
commonest repair is turning a participle into a finite verb (*carrying* →
*carries*) or supplying a subject pronoun for a clause that had none.

---

**1. §11 line 2122 — 93 words → 3 sentences**

OLD: `And $3$ and $9$ are not decoys --- delete them and the law breaks at once, first at $n = 3$ --- for on the standard-mode odds, where squares are illegal, they are the sole rescuers: residue $3$'s only witness is $3$ (to bottom $0$), residue $7$'s is $3$ (to $4$), residue $11$'s is $9$ (to $2$), residue $15$'s is $9$ (to $6$) --- while the squares police only their legal home, the value $1$ carrying residues $\{1, 5\}$ to bottoms $0$ and $4$ and the value $9$ carrying $\{9, 13\}$ to the same two bottoms.`

PROPOSED:
`And $3$ and $9$ are not decoys: delete them and the law breaks at once, first at $n = 3$.`
`On the standard-mode odds, where squares are illegal, they are the sole rescuers: residue $3$'s only witness is $3$ (to bottom $0$), residue $7$'s is $3$ (to $4$), residue $11$'s is $9$ (to $2$), residue $15$'s is $9$ (to $6$).`
`The squares police only their legal home: the value $1$ carries residues $\{1, 5\}$ to bottoms $0$ and $4$, and the value $9$ carries $\{9, 13\}$ to the same two bottoms.`
**[repair]** *carrying* → *carries* twice; *for on* → *On*; *while* dropped at a sentence boundary.

---

**2. §11 line 2028 — 90 words → 3 sentences**

OLD: `From a candidate position --- even, hence standard mode --- every legal move of $F'$ subtracts some $s \equiv 3, 8,$ or $9 \pmod{16}$, and the closure argument of Theorem~\ref{thm:foursquare} consumed exactly two facts about $s$, its parity and its residue modulo $16$, never its actual size, so it transfers verbatim to every member of the extended family: the $s \equiv 3$ and $s \equiv 9$ moves are odd and land on odd residues, none of which lie in the all-even candidate, while the $s \equiv 8$ moves land on $\{8, 10, 12, 14\} \pmod{16}$, also outside --- no move from the candidate returns to it.`

PROPOSED:
`From a candidate position --- even, hence standard mode --- every legal move of $F'$ subtracts some $s \equiv 3, 8,$ or $9 \pmod{16}$.`
`The closure argument of Theorem~\ref{thm:foursquare} consumed exactly two facts about $s$, its parity and its residue modulo $16$, never its actual size, so it transfers verbatim to every member of the extended family.`
`The $s \equiv 3$ and $s \equiv 9$ moves are odd and land on odd residues, none of which lie in the all-even candidate, while the $s \equiv 8$ moves land on $\{8, 10, 12, 14\} \pmod{16}$, also outside: no move from the candidate returns to it.`
**[repair]** none; the two `and`s become sentence breaks and the colon moves.

---

**3. §1 line 214 — 89 words → 3 sentences.** The roadmap sentence: ten
semicolon-joined clauses.

OLD: one sentence, `Section~\ref{sec:prelim} fixes notation ... older than this paper.`

PROPOSED:
`Section~\ref{sec:prelim} fixes notation and the verification lemma; Sections~\ref{sec:chain} through~\ref{sec:main} build chains, the $s_{\min}$ apparatus, and the Diagonal Law.`
`Section~\ref{sec:transfer} isolates the Transfer Principle; Section~\ref{sec:disease} proves confinement at $m = 2$ and $4$; Sections~\ref{sec:grundy} and~\ref{sec:embed} carry the principle forward to the Grundy solution and backward to the universal embedding.`
`Section~\ref{sec:misere} settles mis\`ere play; Section~\ref{sec:examples} solves further games; Section~\ref{sec:method} opens the instrument; and Section~\ref{sec:open} closes what the census could not settle --- and locates the question that remains, older than this paper.`
**[repair]** none; two semicolons become full stops.

---

**4. §11 line 2115 — 85 words → 2 sentences**

PROPOSED:
`That world under one jump of $8$ is precisely the shape of the Chain Lemma (Lemma~\ref{lem:chain}) --- four chains by residue modulo $8$, with bottoms $0, 2, 4, 6$ too poor to afford the jump, and a jump of size $m$ minting a law of modulus $2m$.`
`So $8$ mints $16$, with P at the even rungs: $n \equiv 0, 2, 4, 6 \pmod{16}$, Theorem~\ref{thm:foursquare}, its four residues revealed as chain bottoms; and running the law modulo $8$ instead kills closure on the spot, $8 \to 0$ being a move from the candidate into itself.`
**[repair]** none; the second dash becomes a full stop and `so` opens the new sentence.

---

**5. §10.2 line 1814 — 79 words → 2 sentences**

PROPOSED:
`The index sets coincide because the two internal games are identical --- subtract-a-square at $m = 2$, subtract-$\{2i^2\}$ at $m = 4$ --- with index origin in each case at a position too small to afford any internal move, since $\max(f^*, h^*) < \sigma(m)$.`
`Both are evaluated by the \emph{normal-play} recursion: the hard side because play there is normal, the free side by Lemma~\ref{lem:misere-transfer}, whose conclusion is precisely that the mis\`ere outcomes of the confined class are the normal-play outcomes of its internal game.`
**[repair]** `and both are` → `Both are`.

---

**6. §13 line 2289 — 75 words → 2 sentences**

PROPOSED:
`The true growth rate of Golomb's P-set is wedged between two proven bounds --- the $\sqrt{n}$ floor (Corollary~\ref{cor:sparse}, second half) and the $o(n)$ ceiling that Furstenberg--S\'ark\"ozy places on any square-difference-free set (Corollary~\ref{cor:sparse}, first half).`
`Our instrument reads a count near $n^{0.7}$ across its whole range: a reading, not a theorem, and one that must stay instrument-tier forever unless a genuinely new bound arrives, since no finite prefix can certify an exponent.`
**[repair]** `and our instrument` → `Our instrument`.

---

**7. §11 line 2129 — 74 words → 2 sentences**

PROPOSED:
`Here is the number-theoretic heart at its true address: odd squares modulo $16$ take exactly two values, $1$ and $9$ (Remark~\ref{rem:odd-squares}), and the second is load-bearing precisely at residues $9$ and $13$ --- the square-mode residues, no others.`
`Modulo $8$ every odd square is $1$ and those residues would be stranded: the same poverty of squares modulo powers of two that confines $D(2,\cdot)$ and $D(4,\cdot)$, one refinement up and just barely wealth enough.`
**[repair]** `while modulo $8$` → `Modulo $8$`.

---

**8. §11 line 2144 — 72 words → 2 sentences**

PROPOSED:
`The mechanism classifies tampering as well: an enlargement of the standard set leaves the P-set fixed exactly when every added move is either odd, landing, from any candidate position, on the all-N odd world, or $\equiv 8 \pmod{16}$, a clone of the governor.`
`Verified: $1$, $5$, and $24$ preserve the law, $2$, $4$, and $16$ break it at $n = 2, 4, 16$, and the maximal enlargement, every odd number plus the whole clone class, holds to $2{,}000$.`
**[repair]** `--- verified:` → `Verified:` (capitalised).

---

**9. §11 line 2136 — 69 words → 2 sentences**

PROPOSED:
`So "why $\{3, 8, 9\}$" has its complete answer --- three moves, three jobs, zero waste: one governor $\equiv 8 \pmod{16}$ whose doubling is the modulus, plus a pair of odd rescuers whose residues cover all four standard-odd classes.`
`The number $9$'s double life upgrades rather than dissolves --- rescuer in both modes, carrying $\{11, 15\}$ as a move and $\{9, 13\}$ as a square, the entire upper odd world leaning on the value $9$.`
**[repair]** `and the number` → `The number`.

---

**10. §9 line 1581 — 68 words → 2 sentences.** Three parallel `that`-clauses.

PROPOSED:
`The construction uses only three properties of the host. The foreign classes are step-$m$ chains, so that the ceiling of Theorem~\ref{thm:transfer} is the alternation of Corollary~\ref{cor:chain-grundy}; the mode set contains two amounts whose residues lie on opposite sides of the partition of Lemma~\ref{lem:hduality}(ii), so that the palette is available; and the remaining amounts are $\equiv 0 \pmod{2m}$, so that they are internal.`
**[repair]** the colon becomes a full stop and the three `that`s are dropped — a deletion, but of a function word rather than an emphasis word, so flagged.

---

**11–20.** The remaining ten follow the same three shapes and are listed
compactly; full text on request.

| # | site | words | shape of the split |
|---|---|---:|---|
| 11 | §11 L2037 | 66 | break at `and a move set that only grows` → new sentence |
| 12 | §11 L2003 | 66 | break after `expansion sets`; Austin clause and Ho clause become two sentences |
| 13 | §7 L1150 | 66 | break at `an affine map`; the closing `--- two, not infinitely many ---` becomes its own sentence |
| 14 | §4 L604 | 66 | break at `so within $\mathrm{Bad}$`; the residue-$0$ exclusion stands alone |
| 15 | §11 L2150 | 63 | break at `--- and busy rather than idle:` → `It is busy rather than idle:` **[repair]** pronoun supplied |
| 16 | §12 L2237 | 61 | break after `derived exactly`; the two retrodictions become one sentence each |
| 17 | §11 L2080 | 61 | break at `--- even though`; the parenthetical objection becomes its own sentence |
| 18 | §4 L467 | 60 | break at `--- and since the residues`; the two consequences separate |
| 19 | abstract L81 | 60 | break at `--- so a classification theorem`; the consequence becomes its own sentence |
| 20 | §9 L1538 | 59 | break at `--- the formal statement`; the gloss becomes its own sentence |

## Phase 3 -- the 24 dash asides over eight words

For each: **PROMOTE** (the aside carries an independent assertion and should
become its own sentence) or **PARENTHESISE** (it glosses the noun beside it
and belongs in brackets). Both reuse existing words. A promotion that needs a
subject pronoun or a finite verb is marked **[repair]** -- eight of the nine
promotions do, since an aside rarely arrives with a subject.

Totals: **9 PROMOTE**, **15 PARENTHESISE**.

**1. S1 (Introduction), line 117 -- 11-word aside -- PARENTHESISE**

A two-item gloss on "completely"; brackets hold it without a stop.

> ... --- outcomes and Grundy values under normal play, outcomes under mis\`ere --- ...

**2. S1 (Introduction), line 195 -- 12-word aside -- PARENTHESISE**

Apposition naming Foursquare; a bracket is the standard device.

> ... --- the machine's first find, moves MATH with a square mode at MATH --- ...

**3. S4 (Escape / s_min), line 375 -- 10-word aside -- PARENTHESISE**

Apposition defining the foreign bottoms.

> ... --- the bottoms of the MATH chains classified by Lemma~ REF --- ...

**4. S4 (Escape / s_min), line 491 -- 9-word aside -- PROMOTE**

An independent claim about what Section 5 does with the witness. **[repair]** needs a subject pronoun or finite verb

> ... --- the escape that Section~ REF converts into the classification --- ...

**5. S4 (Escape / s_min), line 531 -- 10-word aside -- PARENTHESISE**

Spells out the set just named; belongs in brackets.

> ... --- its elements are MATH for MATH and MATH for MATH --- ...

**6. S7 (Degenerate moduli), line 944 -- 13-word aside -- PARENTHESISE**

A source pointer, not an assertion.

> ... --- read directly off the mod- MATH and mod- MATH rows of Table~ REF --- ...

**7. S7 (Degenerate moduli), line 1041 -- 9-word aside -- PARENTHESISE**

Apposition identifying the fingerprints with A030193.

> ... --- the opening P-positions of Golomb's game (OEIS REF A030193 ) --- ...

**8. S8 (Grundy Transfer), line 1325 -- 16-word aside -- PROMOTE**

A justification with its own subject and verb. **[repair]** needs a subject pronoun or finite verb

> ... --- MATH is the period of the copy structure in MATH , so any multiple of it does --- ...

**9. S9 (Universal Embedding), line 1506 -- 12-word aside -- PARENTHESISE**

Apposition naming the internal game.

> ... --- the subtraction game MATH on the index MATH , by Lemma~ REF (iv) --- ...

**10. S9 (Universal Embedding), line 1516 -- 10-word aside -- PARENTHESISE**

Restates the two landings; brackets suffice.

> ... --- MATH lands on a bottom, MATH on a top rung --- ...

**11. S10 (Misere play), line 1600 -- 30-word aside -- PROMOTE**

Two independent assertions about misere sums, each citable. **[repair]** needs a subject pronoun or finite verb

> ... --- mis\`ere outcomes of a disjunctive sum are not determined by the summands' outcomes REF , and the mis\`ere quotient of even a simple subtraction game may be large REF --- ...

**12. S11 (Further solved games), line 2003 -- 26-word aside -- PROMOTE**

Austin's theorem in full, with its own reason clause; a sentence. **[repair]** needs a subject pronoun or finite verb

> ... --- for each move MATH already present, the move MATH may be adjoined, since the reply MATH reverses it out and the period MATH absorbs the pair --- ...

**13. S11 (Further solved games), line 2037 -- 9-word aside -- PARENTHESISE**

Apposition listing the witnesses.

> ... --- the standard moves and the squares MATH and MATH --- ...

**14. S11 (Further solved games), line 2042 -- 9-word aside -- PARENTHESISE**

Restates the three conditions just verified.

> ... --- terminals inside, closed against return, reachable from everywhere outside --- ...

**15. S11 (Further solved games), line 2066 -- 9-word aside -- PARENTHESISE**

A condition on the new option; bracket it.

> ... --- present only when MATH is in the enlarged mode --- ...

**16. S11 (Further solved games), line 2080 -- 33-word aside -- PROMOTE**

A complete argument, colon and all; the longest aside in the paper.

> ... --- and provably so, no longer by sweep: by Corollary~ REF the class MATH of MATH contains no P-position at all, so the criterion's condition holds vacuously and Proposition~ REF returns the law unchanged --- ...

**17. S11 (Further solved games), line 2115 -- 27-word aside -- PROMOTE**

Three coordinated claims about the chain structure. **[repair]** needs a subject pronoun or finite verb

> ... --- four chains by residue modulo MATH , with bottoms MATH too poor to afford the jump, and a jump of size MATH minting a law of modulus MATH --- ...

**18. S11 (Further solved games), line 2122 -- 11-word aside -- PROMOTE**

An independent falsifying claim with its own verb. **[repair]** needs a subject pronoun or finite verb

> ... --- delete them and the law breaks at once, first at MATH --- ...

**19. S11 (Further solved games), line 2136 -- 38-word aside -- PROMOTE**

The accounting of the three moves; carries the paragraph's point. **[repair]** needs a subject pronoun or finite verb

> ... --- three moves, three jobs, zero waste: one governor MATH whose doubling is the modulus, plus a pair of odd rescuers whose residues cover all four standard-odd classes; and the number MATH 's double life upgrades rather than dissolves --- ...

**20. S12 (Discovery methodology), line 2215 -- 9-word aside -- PARENTHESISE**

Names two of the five classics.

> ... --- the subtraction game MATH and Golomb's subtract-a-square among them --- ...

**21. S12 (Discovery methodology), line 2231 -- 9-word aside -- PARENTHESISE**

Apposition describing the drafting error.

> ... --- a subtly different game verified faithfully across three documents --- ...

**22. S12 (Discovery methodology), line 2248 -- 10-word aside -- PARENTHESISE**

States what Corollary 8.3 says; apposition to its name.

> ... --- that MATH enters the class-index Grundy sequence only through MATH --- ...

**23. S13 (What is closed), line 2289 -- 24-word aside -- PROMOTE**

Names both bounds with their citations; a sentence of its own. **[repair]** needs a subject pronoun or finite verb

> ... --- the MATH floor (Corollary~ REF , second half) and the MATH ceiling that Furstenberg--S\'ark\"ozy places on any square-difference-free set (Corollary~ REF , first half) --- ...

**24. S* (Acknowledgments), line 2330 -- 30-word aside -- PARENTHESISE**

The itemised list of sections; brackets keep the main clause readable.

> ... --- the MATH apparatus of Sections~ REF and~ REF , and the transfer, Grundy, embedding and mis\`ere results of Sections~ REF and~ REF through~ REF , together with the abstract and introduction --- ...

