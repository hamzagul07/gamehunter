# Density-corollary references (sourced)

Lookups performed 2026-08-18. Every entry records where the field came from.
Nothing here is a proof claim about any GameHunter conjecture; these are
bibliographic records and quotations of what the cited sources state.

## 1. A030193 — subtract-a-square losing positions

- **Source URL:** https://oeis.org/A030193 (fields read via the OEIS JSON API,
  `https://oeis.org/search?fmt=json&q=id:A030193`)
- **Name:** "Let S = squares; a(0)=0; a(n) = smallest m such that m - a(i) is
  not in S for any i < n."
- **Offset:** 0
- **First 12 terms:** 0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 34, 39
- **Confirms the requested identification.** OEIS comment by Mikhail Dvorkin,
  Jan 27 2008: "Consider the following game: two players make moves in turn,
  initially the number on the board is n, each move consists of subtracting a
  perfect square from the number on the board, the player who faces 0 loses.
  This sequence is the set of losing positions in this game."
- **Cross-check:** all 49 terms of the OEIS b-data agree with the engine's
  P-positions for `["squares"]` computed to n = 400.

## 2. Grundy-value sequence of subtract-a-square

- **Candidate A014586: CONFIRMED, not corrected.**
- **Source URL:** https://oeis.org/A014586 (via the same JSON API)
- **Name:** "Nim-Grundy function for Take-a-Square (or Subtract-a-Square)
  game."
- **Offset:** 0
- **First 12 terms:** 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1
- **Cross-check:** all 99 terms of the OEIS data agree exactly with the
  engine's `grundy_sequence(["squares"], 400)` read from n = 0. No mismatch.
- **Note on offset:** A014586 is indexed from n = 0, while `analyze_rule`
  submits `G[1:]`. The match is therefore on a shifted window; the engine's
  own demo reports the same A-number.

## 3. Density-corollary bibliography

### Furstenberg 1977
H. Furstenberg, "Ergodic behavior of diagonal measures and a theorem of
Szemerédi on arithmetic progressions", *Journal d'Analyse Mathématique* **31**
(1977), 204–256. DOI: 10.1007/BF02813304

- **Source URL:** https://link.springer.com/article/10.1007/BF02813304

### Sárközy 1978
A. Sárközy, "On difference sets of sequences of integers I", *Acta Mathematica
Academiae Scientiarum Hungaricae* **31** (1978), no. 1, 125–149.
DOI: 10.1007/BF01896079

- **Source URL:** https://doi.org/10.1007/BF01896079 (recorded in A030193's
  link list)
- Companion papers listed on the same OEIS page, recorded for completeness:
  "On the difference sets of sequences of integers II", *Ann. Univ. Sci.
  Budapest. Eötvös Sect. Math.* **21** (1978), 45–53; "On difference sets of
  sequences of integers III", *Acta Math. Acad. Sci. Hungar.* **31** (1978),
  no. 3, 355–386, DOI: 10.1007/BF01901984.

### Ruzsa 1984
I. Z. Ruzsa, "Difference sets without squares", *Periodica Mathematica
Hungarica* **15** (1984), no. 3, 205–209. DOI: 10.1007/BF02454169

- **Source URL:** https://doi.org/10.1007/BF02454169 (recorded in A030193's
  link list)

### Eppstein 2018
D. Eppstein, "Faster Evaluation of Subtraction Games", in *Proceedings of the
9th International Conference on Fun with Algorithms (FUN 2018)*, edited by
H. Ito, S. Leonardi, L. Pagli and G. Prencipe, Leibniz International
Proceedings in Informatics (LIPIcs) **100**, Schloss Dagstuhl –
Leibniz-Zentrum für Informatik, 2018, Article 20, pp. 20:1–20:12.
ISBN 978-3-95977-067-5. DOI: 10.4230/LIPIcs.FUN.2018.20. Preprint
arXiv:1804.06515 [cs.DS], 18 April 2018.

- **Source URLs:** https://arxiv.org/abs/1804.06515 and
  https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2018.20

**Square-difference-free / Furstenberg–Sárközy connection: confirmed stated.**
The arXiv abstract page for 1804.06515 discusses square-difference-free sets in
connection with the Furstenberg–Sárközy theorem and treats subtract-a-square as
a case study whose winning positions form a maximal square-difference-free set.
The same connection is stated in Eppstein's own OEIS comment on A030193
(Nov 20 2016), quoted here in full:

> This sequence was investigated by Golomb (1966), who proved that it is
> infinite. More strongly (as Ruzsa 1984 notes) the number of values up to any
> given n is at least proportional to sqrt(n). No two numbers in this sequence
> differ by a square, and this sequence can be defined as the lexicographically
> first (greedy) sequence with no square differences. It follows from the
> Furstenberg-Sárközy theorem (e.g., see Sárközy 1978) that its natural density
> is zero.

### Also recorded from the same OEIS link list
- S. W. Golomb, "A mathematical investigation of games of 'take-away'",
  *J. Combinatorial Theory* **1** (1966), 443–458.
  DOI: 10.1016/S0021-9800(66)80016-9
- B. Green and M. Sawhney, "Improved bounds for the Furstenberg-Sárközy
  theorem", arXiv:2411.17448 [math.NT], 2024.
