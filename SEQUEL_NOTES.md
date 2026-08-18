# Sequel notes — literature scans

Scans run 2026-08-18. Titles and links only; no conclusions are drawn here and
nothing below has been read past its abstract unless a quotation says
otherwise. Nothing in this file is a result of this project.

## Scope note on "Theorem C"

The instruction attached to these scans was that nothing prints from Theorem C
until they return. There is no Theorem C in this repository: `grep` over every
`.md`, `.py` and `.tex` file finds no occurrence of the string, and the paper's
numbered results run Theorem 5.1 (Diagonal Law), Theorem 7.4 (Foursquare) and
Proposition 7.6 (Kadam's Extension). So there is nothing gated on these scans
here; if Theorem C lives in a draft outside this repo, that draft is where the
hold applies.

## (1) Undecidability of eventual periodicity, computably-presented sets

- Decidability and Undecidability Results for LIA-Definable Impartial
  Combinatorial Games — Feng, Fang, Luo, Guan (Sun Yat-sen Univ. / Jinan
  Univ.), arXiv:2606.25276, June 24 2026 —
  https://arxiv.org/abs/2606.25276
- Subtraction games in more than one dimension — arXiv:2307.12458 —
  https://arxiv.org/pdf/2307.12458
- Impartial games emulating one-dimensional cellular automata and
  undecidability — arXiv:1201.1039 — https://arxiv.org/pdf/1201.1039
- A brief conversation about subtraction games — Larsson and Saha, appendix by
  Suetsugu, arXiv:2405.20054 — https://arxiv.org/pdf/2405.20054
- Superpolynomial period lengths of the winning positions in the subtraction
  game — arXiv:2312.02426 — https://arxiv.org/pdf/2312.02426
- On aperiodic subtraction games with bounded Nim sequence — Fox,
  arXiv:1407.2823 — https://arxiv.org/pdf/1407.2823
- Subtraction Games: Range and Strict Periodicity — BYU thesis —
  https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=7735&context=etd

Open caveat for the sequel: none of the above was found to state the exact
question asked — undecidability of eventual periodicity for a *computably
presented infinite* subtraction set on one heap. The nearest located results
are about higher dimensions, cellular-automaton emulation, and LIA-definable
games. Whether the one-heap computably-presented question is settled in the
literature is not resolved by this scan.

## (2) Universality / embedding for subtraction games

- Universal Embedding Theorems in Combinatorial Game Theory — Reitmeir,
  bachelor's thesis, Univ. Innsbruck —
  https://www.uibk.ac.at/mathematik/algebra/media/teaching/bachelorarbeit-reitmeir.pdf
- Embedding processes in combinatorial game theory —
  https://core.ac.uk/download/pdf/81140765.pdf
- Playing Games with Algorithms: Algorithmic Combinatorial Game Theory —
  Demaine and Hearn —
  https://www.researchgate.net/publication/1866875_Playing_Games_with_Algorithms_Algorithmic_Combinatorial_Game_Theory
- Impartial Games with Activeness — arXiv:2511.20984 —
  https://arxiv.org/abs/2511.20984

## (3) Invariant expansion / duality near Larsson–Hegarty–Fraenkel

- U. Larsson, P. Hegarty, A. S. Fraenkel, "Invariant and dual subtraction games
  resolving the Duchêne–Rigo conjecture", *Theoret. Comput. Sci.* **412**
  (2011), no. 8–10, 729–735. Preprint arXiv:1005.4162 —
  https://arxiv.org/abs/1005.4162 ;
  https://www.sciencedirect.com/science/article/pii/S0304397510006262
- U. Larsson, "The ⋆-operator and invariant subtraction games", *Theoret.
  Comput. Sci.* —
  https://www.sciencedirect.com/science/article/pii/S0304397511009406
- Deciding game invariance —
  https://www.researchgate.net/publication/265015348_Deciding_game_invariance
- Take-Away Games on Beatty's Theorem and the Notion of p-Invariance —
  https://www.academia.edu/29332038/Take_Away_Games_on_Beattys_Theorem_and_the_Notion_of_p_Invariance
- The Misère ⋆-operator — Dufour, slides —
  https://www.calstatela.edu/sites/default/files/star_operator_shortv2.pdf

Relevance flag for the sequel, recorded as a question and not an answer: the
⋆-operator line of work concerns which move sets can be enlarged without
moving the P-positions, which is the same shape of question as Kadam's
Extension. Whether the mode-switching setting is covered by, or outside, those
criteria is not determined by this scan.
