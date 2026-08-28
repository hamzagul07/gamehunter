# GameHunter v1

An automated conjecture-hunting engine for impartial combinatorial games.
It invents new games, computes their Sprague-Grundy values, detects hidden
structure, filters out already-known mathematics via OEIS, and hands you
ranked, precisely-stated **conjectures** — which become **discoveries** only
when *you* prove them.

Zero dependencies. Python 3.9+. Runs on any laptop.

## 1. Architecture (FunSearch-style, student scale)

```
 PROPOSER            VERIFIER              DETECTORS               FILTER        SELECTOR
 random mutation --> Grundy engine  -->  periodicity          --> OEIS      --> interestingness
 of DSL rules        (Sprague-Grundy)    arithmetic-periodic      novelty       score drives
 (+ optional LLM)    deterministic       mod-m P-position law     lookup        evolution
                                         digit-sum law
                                              |
                                              v
                                   auto-drafted CONJECTURES  ---->  YOU: the proof
```

The design borrows one idea from each ancestor: systematic candidate spaces
with numerical validation before human proof (Ramanujan Machine, Technion,
Nature 2021); the proposer/verifier split where a deterministic evaluator
guards against hallucination (FunSearch, DeepMind, Nature 2023); evolutionary
selection over candidates (AlphaEvolve, 2025). The domain — a searchable
rule-space of *invented* impartial games — is the original contribution.

## 2. Quickstart

```bash
# Step 1: watch the detectors rediscover five known theorems (trust check)
python3 game_hunter.py demo

# Step 2: hunt for new games (about 1-2 minutes; every run is logged)
python3 game_hunter.py hunt --gens 25 --pop 40 --seed 1

# Step 3: deep-dive any rule you like
python3 game_hunter.py analyze --rule '["ifmod",2,0,["fib"],["powers",2]]' --N 20000
```

With internet, OEIS lookups run automatically on finalists (cached in
`oeis_cache.json`, one polite request per second). Offline, add `--offline`.

Run many seeds. Different seeds explore different regions of rule-space.
Every hunt appends to `hunt_log.jsonl` and writes a full `report_*.json` —
this is your research log; never delete it.

## 3. Reading a report

- **tier** — PERIODIC / ARITHMETIC_PERIODIC / HIDDEN_MOD_STRUCTURE /
  DIGIT_STRUCTURED are theorem material. CHAOTIC may hide deeper structure.
  DULL is trash.
- **P-positions** — positions where the player to move *loses* (G(n)=0).
- **CONJECTURE lines** — precise statements the data supports at this range.
  They are *not* theorems. Data can lie past the horizon; only proof can't.
- **oeis_*: not_found** — novelty candidate. **found A-number** — known
  mathematics; still useful as a sanity check, but not a discovery.
- **note: identical to known classic** — the engine caught itself
  rediscovering textbook material and penalized it.

## 4. The honest protocol (non-negotiable)

**Scope note (added August 2026).** The rules in this file govern automated
agents operating in this repository: they propose, compute, verify and
referee, and they never write mathematics into `proofs/`. That constraint
has held and still holds. These rules are not, and never were, a claim
about how the paper's mathematics was drafted. A substantial part of the
theory added during the August 2026 extension was drafted in dialogue with
an AI system under the author's direction and refereeing; this is disclosed
in the paper's acknowledgments and recorded in full in the August 2026
addendum to `PROJECT_REPORT.md`.

1. The machine outputs candidates. **You** own conjectures only after
   verifying by hand at small n, and theorems only after writing a proof.
2. Re-verify every finalist at a much larger range (`--N 20000` or more)
   before investing proof effort. Patterns that die at large n saved you
   months; log them as negative results.
3. Get every proof checked by a stronger mathematician (teacher, professor,
   Art of Problem Solving forums) before claiming anything publicly.
4. OEIS etiquette: entries are refereed by human editors. Submit only
   sequences you have verified by hand, understood, and can describe well —
   a handful of curated, high-quality entries, never bulk machine output.
   Read their contribution guidelines first. Spamming OEIS would burn your
   reputation and disrespect a resource mathematicians depend on.
5. In any paper or application, describe the methodology exactly as it is,
   including where an AI system drafted mathematics, if it did. As of
   August 2026 the accurate description is: "I built an automated search
   system; it proposed the candidates and verified them mechanically; some
   proofs are mine, and much of the later theory was drafted in dialogue
   with an AI system, refereed, corrected and verified by me." That
   sentence is strong only for as long as it is true. When the facts
   change, change the sentence first.

## 5. Wiring your LLM as a second proposer

Implement `llm_propose()` in `game_hunter.py`. Suggested prompt to your AI:

> Here are the DSL primitives: [paste §1 of game_hunter.py DSL comment].
> Here are the current top games and their scores: [paste hall-of-fame
> reports]. Propose 10 new rules as JSON arrays that might show clean
> P-position structure while differing from all games above. Output only a
> JSON list of rules, nothing else.

**The firewall rule:** every LLM proposal passes through the same
`valid()` + Grundy engine + detectors as a random mutation. The LLM never
scores, never verifies, never "confirms" a pattern, and never writes proofs
into your results. Proposer creativity, verifier authority — that separation
is the entire reason systems like this produce trustworthy output.

## 6. Roadmap (v2 ideas, roughly in order of payoff)

- **Two-pile and move-history games** — extend the DSL with a second state
  variable; Grundy engine generalizes directly. This is where genuinely
  unexplored territory gets vast.
- **Automatic-sequence detection + Walnut** — infer a finite automaton for
  the P-position set (L* learning), then use the Walnut theorem-prover
  (Shallit's school) to *machine-prove* base-k characterizations. A
  conjecture pipeline that ends in a machine-checked proof is elite.
- **Berlekamp–Massey over GF(2)** on the win/loss sequence to catch linear
  structure the current detectors miss.
- **Misère play** (last player to move *loses*) — one-line change in the
  engine, famously wilder theory.
- **OpenEvolve integration** — swap the random mutator for the open-source
  AlphaEvolve-style population search once v1 results justify the effort.
- Parallel evaluation (multiprocessing) for N in the millions.

## 7. First-week battle plan

- Day 1 — run `demo`, read every line, replay the {1,2,3} and powers-of-2
  proofs on paper until the induction pattern feels obvious.
- Days 2–3 — hunts with 10+ different seeds; collect every
  HIDDEN_MOD_STRUCTURE and DIGIT_STRUCTURED finalist into a shortlist.
- Day 4 — re-verify the shortlist at `--N 20000`+; run OEIS checks online;
  kill everything known or broken.
- Day 5 — pick the single cleanest survivor and attempt the induction proof
  by hand. Small, complete, and proved beats big and conjectural.
- Weekend — write up the first proof in LaTeX, take it to a teacher or
  forum for checking, and log everything.
