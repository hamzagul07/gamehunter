# Invariant-subtraction-game references (sourced)

Lookups performed 2026-09-01 for the bibliography batch. Every field below
was taken from publisher-registered metadata, and each entry records the
source it came from. Nothing here is a claim about any GameHunter
conjecture; these are bibliographic records plus a quotation of what each
paper says about itself.

Neither paper is cited in `paper/main.tex` at the time of writing. This
file is the sourcing record; the citing sentences are written separately.

## Method

Fields were obtained twice, independently:

1. Crossref REST API (`api.crossref.org/works`), searched by
   bibliographic query.
2. DOI content negotiation against `https://doi.org/<doi>` with
   `Accept: application/vnd.citationstyles.csl+json`, which returns the
   publisher's own CSL-JSON record.

Both routes returned identical volume, issue, page, year and DOI for both
papers. Abstracts are quoted from the arXiv preprint records, since
neither DOI record carries an abstract field.

## (a) Larsson, the star-operator paper

U.~Larsson, "The $\star$-operator and invariant subtraction games",
*Theoretical Computer Science* **422** (2012), 52--58.
DOI: 10.1016/j.tcs.2011.11.021

- **Requested fields, all confirmed:** volume **422**; year **2012**
  (issued March 2012); pages **52--58**; DOI **10.1016/j.tcs.2011.11.021**.
- Issue: none recorded (the volume is unnumbered by issue).
  ISSN 0304-3975. Publisher: Elsevier BV. Author: Urban Larsson, sole.
- **Source URLs:**
  - https://api.crossref.org/works?query.bibliographic=The+star-operator+and+invariant+subtraction+games+Larsson
  - https://doi.org/10.1016/j.tcs.2011.11.021 (CSL-JSON via content negotiation)
  - Preprint: https://arxiv.org/abs/1009.4220
- **Note on the title:** Crossref stores the title with the star as
  embedded MathML (`<mml:mo>&#8902;</mml:mo>`). The arXiv record renders it
  `The $\star$-operator and Invariant Subtraction Games`. A bibliography
  entry should set the symbol as `$\star$`.

**What the paper is about** (from the arXiv abstract, arXiv:1009.4220):
the paper studies invariant subtraction games -- impartial games in which
every allowed move is available from every position -- and defines a new
game $G^\star$ from an old one by taking the non-zero P-positions of $G$ as
the moves of $G^\star$. It gives a polynomial-time algorithm for infinitely
many P-positions of (Wythoff Nim)$^\star$, introduces the permutation games
and the ornament games, and proves that ($k$-pile Nim)$^{\star\star}$ is
$k$-pile Nim.

## (b) Larsson, Hegarty and Fraenkel, the Duchene-Rigo paper

U.~Larsson, P.~Hegarty and A.~S.~Fraenkel, "Invariant and dual subtraction
games resolving the Duch\^ene--Rigo conjecture", *Theoretical Computer
Science* **412** (2011), no.~8--10, 729--735.
DOI: 10.1016/j.tcs.2010.11.015

- **Requested fields, all confirmed:** volume **412**; year **2011**
  (issued March 2011); pages **729--735**; DOI
  **10.1016/j.tcs.2010.11.015**.
- Issue **8--10**. ISSN 0304-3975. Publisher: Elsevier BV.
  Authors: Urban Larsson; Peter Hegarty; Aviezri S. Fraenkel.
- **Source URLs:**
  - https://api.crossref.org/works?query.bibliographic=Invariant+and+dual+subtraction+games+resolving+the+Duchene-Rigo+conjecture
  - https://doi.org/10.1016/j.tcs.2010.11.015 (CSL-JSON via content negotiation)
  - Preprint: https://arxiv.org/abs/1005.4162
- **Note on the author name:** Crossref and the published title spell it
  "Duch\^ene--Rigo"; the arXiv title as filed reads "Duch\^e-Rigo", an
  apparent typo in the preprint metadata. The published spelling is the
  one to cite.

**What the paper is about** (from the arXiv abstract, arXiv:1005.4162):
the paper proves a conjecture of Duch\^ene and Rigo that every
complementary pair of homogeneous Beatty sequences is the solution of some
*invariant* impartial game, where invariance means every move is available
from anywhere on the board. It proves this for a wider class of
complementary sequence pairs by generalizing the notion of a subtraction
game: from a pair $(a_n)$, $(b_n)$ it builds a game $G$ with invariant
moves $\{\{a_n, b_n\}\}$, then the game $G^\star$ whose moves are the
non-zero P-positions of $G$, and gives sufficient conditions on the
initial pair for this duality to hold.
