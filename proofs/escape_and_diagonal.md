# Escape and the Diagonal

**The games D(m, r), solved for every m ≥ 3 except m = 4, with the two diseased moduli explained.**

*Status: human-authored; referee-accepted July 30, 2026 (mathematics refereed across the Escape and parity-audit vivas; structural pass on this assembly). Examination records: verification/escape_viva.md and verification/diagonal_viva.md.*

**The game.** D(m, r) is played on the non-negative integers. From a position n ≡ r (mod m) — *squares mode* — a move subtracts any square k² with k ≥ 1 and k² ≤ n. From any other position — *fallback mode* — the only move subtracts m, available when n ≥ m. Normal play: a position with no legal move is P; a position is N iff some move reaches a P. Throughout, Q(2m) denotes the set of squares modulo 2m.

---

## Part I — The engine: squares modulo 10

| k | k² | k² mod 10 |
|---|----|-----------|
| 1 | 1 | 1 |
| 2 | 4 | 4 |
| 3 | 9 | 9 |
| 4 | 16 | 6 |
| 5 | 25 | 5 |
| 6 | 36 | 6 |
| 7 | 49 | 9 |
| 8 | 64 | 4 |
| 9 | 81 | 1 |
| 10 | 100 | 0 |

Collecting the distinct values: **Q = {0, 1, 4, 5, 6, 9}**. The complement — the values a square can never take mod 10 — is {2, 3, 7, 8}.

Why k = 10 is enough, one line and part of the proof: (k + 10)² = k² + 20k + 100, and both 20k and 100 are multiples of 10, so (k + 10)² ≡ k² (mod 10) — every k past 10 replays one of these ten rows, so the table above is the whole story forever.

Mirror check, kept as the standing tool for every later table: (10 − k)² = 100 − 20k + k² ≡ k² (mod 10) for the same reason. The table must mirror around the middle, and it does: row 6 matches row 4 (both 6), row 7 matches row 3 (both 9), row 8 matches row 2 (both 4), row 9 matches row 1 (both 1). Footnote kept honest: row 10 mirrors "row 0," so the lone 0 enters at that end — k = 1..5 catches {1, 4, 5, 6, 9} and k = 10 supplies the 0. A broken mirror means an arithmetic slip.

---

## Part II — The Escape Theorem for D(5, 2)

**II.1 Statement.** There is an explicit threshold N₀, computed in II.6 below, such that every position n ≡ 2 (mod 5) with n ≥ N₀ has at least one legal square move — some k with k² ≤ n — whose landing n − k² is a P-position of a fallback chain. Consequently every such n is an N-position.

**II.2 The target window.** By the Chain Lemma, the fallback classes 0, 1, 3, 4 (mod 5) have their P-positions exactly at n ≡ 0, 1, 3, 4 (mod 10); call that set T = {0, 1, 3, 4} (mod 10). A landing in T is genuinely P: a number ≡ 0, 1, 3, or 4 (mod 10) is ≡ 0, 1, 3, or 4 (mod 5), so it lives in a fallback chain where the lemma has jurisdiction, and its residue mod 10 matching the chain bottom's means it sits an even number of rungs up — precisely the lemma's P-rungs.

**II.3 The split.** Write n = 5q + 2: if q = 2t then n = 10t + 2, and if q = 2t + 1 then n = 10t + 7, so a class-2 position is ≡ 2 or 7 (mod 10) — that is, r or r + m — and the proof forks on the parity of q exactly the way the chain proof forked on the parity of j.

**II.4 Coverage line one.** For n ≡ 2 (mod 10): the differences 2 − T are {2−0, 2−1, 2−3, 2−4} ≡ {2, 1, 9, 8} (mod 10), and intersecting with Q = {0, 1, 4, 5, 6, 9} leaves {1, 9}; take the smallest, s = 1, so subtracting 1² gives n − 1 ≡ 1 (mod 10) ∈ T.

**II.5 Coverage line two.** For n ≡ 7 (mod 10): the differences 7 − T are {7, 6, 4, 3} (mod 10), intersecting with Q leaves {4, 6}; take s = 4, so subtracting 2² gives n − 4 ≡ 3 (mod 10) ∈ T. Both keystones came with a spare — 9 = 3² also rescues residue 2, and 16 = 4² also rescues residue 7. The corridor is wider than it needs to be.

**II.6 Legality and the threshold.** The rescue squares are the concrete numbers 1 and 4. For the residue-2 class, whose members are 2, 12, 22, …, legality demands 1 ≤ n, which already holds at the smallest member. For the residue-7 class, members 7, 17, 27, …, legality demands 4 ≤ n, which holds at 7. So both rescues are legal for every member of their class, and the threshold collapses: **N₀ = 2**, the smallest class-2 position in existence. Below N₀ there are no class-2 positions at all, so the hand-check zone is empty — verdict: vacuous. Checking the workbook rows anyway, as ordered: 2 − 1 = 1 (P) ✓, 7 − 4 = 3 (P) ✓, 12 − 1 = 11 (P) ✓, 17 − 4 = 13 (P) ✓, 22 − 1 = 21 (P) ✓, 27 − 4 = 23 (P) ✓. Every row is rescued-anyway, rebels: none. Worth recording why it collapsed: the rescue squares 1 and 4 happen to be smaller than the smallest members of their classes. Nothing guarantees that luck at other moduli, which is exactly why the theorem was written with N₀ as a named unknown.

**II.7 Assembly.** The Chain Lemma classifies the four fallback classes everywhere: P exactly at n ≡ 0, 1, 3, 4 (mod 10), N at 5, 6, 8, 9. The Escape Theorem classifies class 2 everywhere, since N₀ = 2 means "past the threshold" is all of it: residues 2 and 7 (mod 10) are all N. Union the two and every residue mod 10 is accounted for, with no unexplained positions beneath any threshold.

> **Theorem (D(5,2), solved).** A position n is P if and only if n ≡ 0, 1, 3, or 4 (mod 10).

One coincidence too pretty not to flag: the P-set of the whole game *is* the target window T — the landing pads and the answer turned out to be the same four residues. [Resolved: Part IV, Remark 2.]

**II.8 Scope and the forward hook.** The proof secretly depended on squares mod 10 being *rich*: Q fills six of the ten residues, enough that both difference lists {2, 1, 9, 8} and {7, 6, 4, 3} caught at least one member — had Q missed either list entirely, one residue of class 2 would have had no escape and the whole corridor would have collapsed. Generalizing to D(m, r) therefore means asking whether that richness survives at other moduli — whether squares mod 2m keep intersecting the difference sets ρ − T for both ρ ∈ {r, r + m} — and since quadratic residues thin out and organize themselves as the modulus grows, that question, not the game logic, is the real content of what follows.

**II.9 Verification against the workbook.** Prediction first, then the rows: residue-2 positions (2, 12, 22) should be rescued by any legal square ≡ 1 or 9 (mod 10), residue-7 positions (7, 17) by any square ≡ 4 or 6 (mod 10), and every other square should be wasted.

- n = 2: only move 2−1 = 1 (P). Predicted rescue 1² present ✓, nothing else in the row to waste.
- n = 7: 7−1 = 6 (N), 7−4 = 3 (P). Rescue 2² present ✓; the 1² is wasted exactly as the congruence says (1 ∉ {4, 6} mod 10, landing ≡ 6).
- n = 12: 12−1 = 11 (P), 12−4 = 8 (N), 12−9 = 3 (P). Primary rescue 1² ✓, and the spare 9 = 3² makes its first appearance in the first row big enough to afford it.
- n = 17: 17−1 = 16 (N), 17−4 = 13 (P), 17−9 = 8 (N), 17−16 = 1 (P). Primary 2² ✓ and spare 4² ✓.
- n = 22: 22−1 = 21 (P), 22−4 = 18 (N), 22−9 = 13 (P), 22−16 = 6 (N). Primary 1² ✓, spare 3² ✓.

The check came back stronger than required: not only does the predicted rescue sit in every row, every wasted square is wasted for the predicted reason — its residue misses the survivor set, and every wasted landing is ≡ 6 or 8 (mod 10), both N-residues. The congruence machinery reproduces the workbook letter-for-letter, and the 200,000 mechanical sweep stands as the bulk consistency evidence behind it.

---

## Part III — The engines at every modulus: Q(2m) with complements

The mirror tool, proved once in general: (2m − k)² = 4m² − 4mk + k² ≡ k² (mod 2m), since 4m² = 2m·2m and 4mk = 2k·2m. So every table is k = 1..m plus mirrors, plus the 0 from k = 2m. Two side facts fell out of the mirrors and are used below: for odd m, m² − m = m(m − 1) has the even factor m − 1, so m² ≡ m (mod 2m); for even m, m² = (m/2)·2m ≡ 0 (mod 2m).

| mod | Q(2m) | complement |
|---|---|---|
| 4 | {0, 1} | {2, 3} |
| 6 | {0, 1, 3, 4} | {2, 5} |
| 8 | {0, 1, 4} | {2, 3, 5, 6, 7} |
| 10 | {0, 1, 4, 5, 6, 9} | {2, 3, 7, 8} |
| 12 | {0, 1, 4, 9} | {2, 3, 5, 6, 7, 8, 10, 11} |
| 14 | {0, 1, 2, 4, 7, 8, 9, 11} | {3, 5, 6, 10, 12, 13} |
| 18 | {0, 1, 4, 7, 9, 10, 13, 16} | {2, 3, 5, 6, 8, 11, 12, 14, 15, 17} |
| 22 | {0, 1, 3, 4, 5, 9, 11, 12, 14, 15, 16, 20} | {2, 6, 7, 8, 10, 13, 17, 18, 19, 21} |

The mod-4 and mod-8 rows are the indictment written out: Q(4) = {0, 1} and Q(8) = {0, 1, 4} both sit entirely inside the triple {0, 1, m}, so their complements swallow every value any hard set will ever contain (Part IV) — the disease of m = 2 and m = 4 is visible in these two rows before any game logic starts. One eyebrow kept raised on purpose: the thinnest *odd* table is mod 18, thinned because 9 is itself a square and the rows k = 3 and k = 9 collide there — m = 9's anomaly is foreshadowed in its own table.

---

## Part IV — The general theorem

> **Theorem (Diagonal Law).** Let m ≥ 3 with m ≠ 4, and let 0 ≤ r ≤ m − 1. Define the exception set
>
> **E = {(9, 4), (9, 5), (9, 6)}.**
>
> In D(m, r), a position n is P **if and only if**
> n ≡ b (mod 2m) for some foreign bottom b ∈ {0, 1, …, m−1} \ {r}, **or** n = 0, **or** (m, r) ∈ E and n = m + r.
>
> The law holds for both parities of m, with no thresholds and no unverified zones.

**IV.1 Setup.** By the Chain Lemma (general form, as accepted): fallback moves preserve class mod m, so each class c ≠ r is a single self-contained chain c, c + m, c + 2m, … with terminal bottom c — no square moves (c ≢ r) and no affordable fallback (c < m) — and P/N alternate upward from the stuck bottom: P exactly at n ≡ c (mod 2m). The window T(m, r) is the set of foreign bottoms mod 2m. Class r splits mod 2m into the **free residue** (r when r ≥ 1, else m) and the **hard residue** (r + m when r ≥ 1, else 0). The free escape is immediate: 1² lands the free residue on the bottom directly beneath it (r − 1, or m − 1 when r = 0), and is legal from the smallest free member. For the hard residue, a square value s (mod 2m) lands in the window iff s ∈ H(m, r) = {r+1, …, m−1} ∪ {m+1, …, m+r} for r ≥ 1, or {m+1, …, 2m−1} for r = 0. Constitutional uselessness, for every m and r: 0, 1, m ∉ H(m, r) — a square ≡ 0 or m (mod 2m) is ≡ 0 (mod m) and stays inside class r, and subtracting ≡ 1 from the hard residue lands one below it in the top half, an odd rung, N.

**IV.2 Clearing Lemma** *(formerly the Zone Lemma — the parity audit showed it is not a patch on the odd-m witness but the escape engine itself, parity-free).* Suppose some square s ≠ m lies in the integer interval (r, m + r] when r ≥ 1, or in (m, 2m) when r = 0. Then the entire hard class is N by the single move −s. Legality: s ≤ m + r, the smallest hard member (for r = 0: s < 2m, and the smallest positive hard member is 2m), so the move is affordable to every member from the first. Landing: n − s ≡ m + r − s (mod 2m) is a foreign bottom — in (r, m) when r < s < m, in [0, r) when m < s ≤ m + r; for r = 0, the landing 2m − s lies in (0, m). Combined with the free escape, class r is all N — except possibly n = 0, handled in IV.6.

**IV.3 The interval always contains a square (m ≥ 3) — repaired and parity-free.** For r ≥ 1: if (r, m + r] contained no square, consecutive squares would straddle it, c² ≤ r and (c + 1)² > m + r, so 2c + 1 > m, hence c ≥ m/2 for any m, hence c² ≥ m²/4 > m − 1 ≥ r, since m²/4 − (m − 1) = (m − 2)²/4 > 0 for m ≥ 3 — contradicting c² ≤ r. The inequality degenerates at exactly one modulus, m = 2, where (m − 2)² = 0 and the interval can indeed be empty ((1, 3] in D(2, 1) contains no square). Erratum, folded in: for r = 0 the interval reads (m, 2m), which contains a square for every m ≥ 3 **except m = 4** — (4, 8) = {5, 6, 7} is square-free, and it is the lone counterexample, since the same consecutive-squares squeeze forces emptiness only for m ≤ 5, and m = 3 has its 4, m = 5 its 9.

**IV.4 The failure window.** With a square always present, the Clearing Lemma's hypothesis can fail for r ≥ 1 only if the *unique* square in (r, m + r] is m itself: m = b² with (b − 1)² ≤ r (no smaller square intrudes) and (b + 1)² > m + r, i.e. r ≤ 2b. The window (b − 1)² ≤ r ≤ 2b is nonempty iff (b − 1)² ≤ 2b iff b ≤ 3. Among m ≥ 3 that leaves exactly m = 4 (b = 2, r ∈ {1, 2, 3}) and m = 9 (b = 3, r ∈ {4, 5, 6}). With the r = 0 erratum, every class of m = 4 is condemned from the outside — no clearing square exists for any r — while m = 9 is healthy at every r except 4, 5, 6. Squarehood of m alone is harmless: at m = 25 (b = 5) the neighboring square 36 sits only 2b + 1 = 11 above m, deep inside a 25-wide window, so it invades (r, m + r] for every r; a square m isolates itself only when the modulus is small enough (b ≤ 3) for square-gaps to outrun m.

**IV.5 The rebels.** At (9, r) with r ∈ {4, 5, 6}, the smallest hard member n₀ = m + r ∈ {13, 14, 15} can afford only the squares k² ≤ r and 9. A square k² ≤ r lands on m + (r − k²), the odd rung directly above bottom r − k² — N. The square 9 lands on r itself, the smallest free member — N, since it escapes by 1². Every move lands on N, so **n₀ is P.** In-game receipts: in D(9,4), 13 → 12, 9, 4, all N; in D(9,5), 14 → 13, 10, 5, all N; in D(9,6), 15 → 14, 11, 6, all N. Above the rebel the class closes uniformly: the members 27 + r (31, 32, 33) are cleared by 25 ≡ 7 (mod 18), which lies in all three hard sets, landing on bottoms 6, 7, 8; the members 45 + r (49, 50, 51) by 49 ≡ 13, landing on bottoms 0, 1, 2; and from 63 + r ≥ 64 = (m − 1)² onward, the witness 64 ≡ 10 = m + 1 lands on bottom r − 1 forever. So each exceptional game carries exactly one extra P-position, and the exception set is precisely the E displayed in the box.

**IV.6 Corruption audits.** The n = 0 clause: when r = 0, zero is claimed by squares mode and is the unique squares-mode position that can afford no square (k ≥ 1 forces k² ≥ 1 > 0), so it is terminal, hence P — while the unamended law would file residue 0 as N. It corrupts nobody: fallback chains never visit class 0; the positions that can drop to 0 are n = k² ≡ 0 (mod m), class-0 members the theorem already declares N; and the classes above escape without it — spot receipts: 10 − 9 = 1 (P) in D(5,0), 14 − 9 = 5 (P) in D(7,0). For r ≥ 1 the clause is absorbed, since 0 is itself a foreign bottom; it earns its keep exactly at r = 0. The rebels, one sentence in the same mirror: a rebel corrupts nobody either — fallback chains never enter class r, and the only positions with a move onto m + r are class-r members above it (a square step back into class r forces k² ≡ 0 mod 9, i.e. 3 | k), which the theorem already declares N, so the rebel's P-ness merely hands them one more witness for what they already were.

**IV.7 Remarks.** *(1) The odd-m witness identity, the original route.* For odd m, (m − 1)² = m² − 2m + 1 ≡ m² + 1 ≡ **m + 1 (mod 2m)**, using m² ≡ m from Part III; and m + 1 belongs to every hard set, landing the hard residue exactly on bottom r − 1 (m − 1 when r = 0). So the pair (1², (m − 1)²) is a universal witness pair for all odd m at once — at the price of the threshold n ≥ (m − 1)². The Clearing Lemma supersedes it: a square below m + r does the same job with legality free, for both parities, with no threshold. The identity remains the cleanest line in this file and the historical door to everything above. *(2) The D(5,2) coincidence, resolved.* For any escaped game the P-set equals its window by construction: P-set = (chain P's) ∪ (class-r P's) = T ∪ ∅ = T. The equality fails exactly where escape does — the three exceptional games have P-set = T ∪ {m + r}, and the diseased games' P-sets properly contain their windows.

---

## Part V — Confinement and retrodiction

**V.1 Confinement Lemma.** For m ∈ {2, 4} and every r: Q(2m) ⊆ {0, 1, m} — read directly off the mod-4 and mod-8 rows of Part III — while every hard set H(m, r) excludes 0, 1, and m (IV.1). Hence from any hard-residue position, every legal square move either stays inside class r (a square ≡ 0 or m mod 2m is ≡ 0 mod m) or lands one below on the odd rung above a bottom (a square ≡ 1), an N-position — never on a P-position of a foreign chain. *Proof:* only-options enumeration over Q(2m), the mirror image of the Independence section — there, fallback moves cannot leave a chain; here, square moves cannot leave the class except onto N. *Consequence:* the hard class's P/N structure is decided by a self-contained internal recursion, and its very first member already defies the chain law: 3 is P in D(2,1) and 5 is P in D(4,1), where escape, if it existed, would force N. Calibration, as accepted at the viva: for m = 2 and m = 4 we prove confinement — no square door into the window, so the class turns inward. We do **not** prove that these confined classes obey no eventual law of their own: "no period and no modulus up to 200 fits" is a reading from the search instrument, not a theorem, and their aperiodicity remains open.

**V.2 Double condemnation.** The two diseased moduli are exactly the two the parity-free engine cannot serve. At m = 2 the engine is silent: the always-a-square inequality degenerates ((m − 2)² = 0) and the clearing interval (1, 3] is genuinely square-free. At m = 4 the engine convicts every class from the outside: the failure window covers r ∈ {1, 2, 3}, and the r = 0 interval (4, 8) is square-free. Outside view and inside view agree because both are reading the same two table rows: Q(2m) ⊆ {0, 1, m}.

**V.3 Retrodiction I — the fingerprints.** During the Chain Lemma verification sweeps — recorded weeks before any escape machinery existed — the ledger logged unexplained P-positions 3, 11, 23 in D(2,1) and 5, 13, 37 in D(4,1), anomalies with no mechanism attached. The Confinement Lemma now computes those games' hard residues as 3 (mod 4) and 5 (mod 8), and all six fingerprints satisfy their congruence without exception. The theory did not accommodate old data; it specified coordinates for where lawlessness is possible, and data recorded before the theory existed turns out to have been sitting on those coordinates the entire time.

**V.4 Retrodiction II — the D(9,4) receipt.** Primary source, quoted verbatim from DIAGONAL_WORKBOOK.md and the raw JSON behind it:

```
| D(9,4) | mod 18 | P ≡ 0,1,2,3,5,6,7,8 | preperiod 14 | period 18 | swept 200,000 |
{"game":[9,4],"preperiod":14,"period":18,"p_res":[0,1,2,3,5,6,7,8],"pre_P":[0,1,2,3,5,6,7,8,13]}
```

This line was recorded before the rebel mechanism existed, and the mechanism now derives every number on it with zero freedom. The rebel 13 is the lone off-residue P, named in the pre_P field. Any eventually-periodic fit beginning at or before 13 would propagate 13's P-ness by the period, which the sweep refutes (31 is N); so every correct fit begins at 14, and the minimal preperiod is exactly rebel + 1 = 14. The period is 2m = 18, and the P-residues are the foreign bottoms {0, …, 8} \ {4} = {0, 1, 2, 3, 5, 6, 7, 8}. Provenance note, owed and recorded: an earlier session claimed from memory that every diagonal cell's preperiod was ≤ 1 and built a certificate on that claim; the file said otherwise all along, the claim and the certificate are struck, and this line enters the paper as the primary-source receipt that replaced them.

---

## Part VI — Scope

**Solved:** every m ≥ 3 except m = 4 — all r, both parities — under the boxed law: the chains by the Chain Lemma, class r by the Clearing Lemma plus the free escape, the n = 0 clause at r = 0, and the three rebels of E; no fences, no thresholds, no machine dependence, and no even-m gap — the even case was never open, only misfiled while the Clearing Lemma wore the wrong name.

**Explained:** m = 2 and m = 4, where the Confinement Lemma proves escape impossible and hands the recorded lawlessness to the self-contained internal games — with the double condemnation of V.2 recording that the outside engine fails at exactly those two moduli and nowhere else.

**Open:** only the aperiodicity of the two confined classes; "lawless to 200,000, no modulus to 200" remains an instrument statement, not a theorem. The mod-16 and mod-20 stackings, once necessities for an even-m theorem, are demoted to cross-checks of a theorem already proved.
