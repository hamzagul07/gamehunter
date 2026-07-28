# GameHunter shortlist

Generated 2026-07-28 by an operations run of `game_hunter.py`. Nothing in this
file is proved. The engine emitted every CONJECTURE line below; they are
reproduced verbatim.

## How this shortlist was produced

- Engine: `game_hunter.py`, Python 3.9.6, OEIS lookups online.
- Trust check: `python3 game_hunter.py demo` reproduced all five classic
  detections, with subtract-a-square P-positions matching **A030193**.
- Hunts: `python3 game_hunter.py hunt --gens 25 --pop 40 --seed k` for
  k = 1,2,3,4,5. Five reports, 40 finalist records total.
- Filter: tier in {HIDDEN_MOD_STRUCTURE, DIGIT_STRUCTURED, ARITHMETIC_PERIODIC}
  AND `oeis_p_positions` status `not_found`. 17 records passed; 15 remain
  after deduplication by `game_hash`. Sorted by score descending.
- Deep verify: `python3 game_hunter.py analyze --rule '<DSL>' --N 20000` for
  every entry. "Survived at N=20000" means the CONJECTURE line emitted at
  N=20000 is character-identical to the one emitted during the hunt.

Observed tier distribution across all 40 finalist records:
HIDDEN_MOD_STRUCTURE 39, PERIODIC 1. No DIGIT_STRUCTURED or
ARITHMETIC_PERIODIC records occurred in these five hunts.

## Read this before spending proof effort

1. **The score ranking is nearly flat.** Entry 1 scores 11.26; entries 2-15
   are all tied at exactly 11.14. Their relative order below is an artifact of
   file iteration order, not a quality signal. Treat entries 2-15 as unordered.
2. **`not_found` is a statement about a 24-term prefix, not about novelty.**
   `oeis_lookup` sends the first 24 P-positions verbatim (`OEIS_TERMS = 24`).
   Several entries below have an irregular head followed by a clean tail --
   e.g. entry 1's P-positions begin `1, 2, 7, 9, 11, 13, ...`. That literal
   prefix is absent from OEIS even though the conjectured eventual law
   (`n = 1 (mod 2)`) is the same law A005408 describes. `not_found` here means
   "this exact prefix is not indexed", nothing stronger.
3. **Four entries restate the same modular law as the known proper-divisor
   game.** Entries 1, 2, 5 and 7 all conjecture P-positions `n = 1 (mod 2)`,
   which is the law the classic `["divisors"]` game already satisfies. The
   rules and Grundy sequences differ (distinct `game_hash`), and the thresholds
   differ, but the conclusion is not new mathematics on its face.
4. Survival at N=20000 is evidence, not proof. Data can lie past the horizon.

---

## 1. (proper divisors of n + 2)

- **DSL**: `["shift", 2, ["divisors"]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n + 2)
- **Score**: 11.26
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `901ec3fa1008`  (surfaced by seed(s) [3, 4])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 6, the P-positions are exactly n ≡ 1 (mod 2).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["shift", 2, ["divisors"]]' --N 20000
```

## 2. (proper divisors of n ∪ {7})

- **DSL**: `["union", ["divisors"], ["const", [7]]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n ∪ {7})
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `2828e2dc064b`  (surfaced by seed(s) [2, 3])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 8, the P-positions are exactly n ≡ 1 (mod 2).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["union", ["divisors"], ["const", [7]]]' --N 20000
```

## 3. (proper divisors of n ∪ {2,7,8})

- **DSL**: `["union", ["divisors"], ["const", [2, 7, 8]]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n ∪ {2,7,8})
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `166c19be7d8a`  (surfaced by seed(s) [2])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 8, the P-positions are exactly n ≡ 1 (mod 3).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["union", ["divisors"], ["const", [2, 7, 8]]]' --N 20000
```

## 4. (proper divisors of n ∪ {2,5,7,8})

- **DSL**: `["union", ["divisors"], ["const", [2, 5, 7, 8]]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n ∪ {2,5,7,8})
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `42773f8c2500`  (surfaced by seed(s) [2])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 8, the P-positions are exactly n ≡ 1 (mod 3).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["union", ["divisors"], ["const", [2, 5, 7, 8]]]' --N 20000
```

## 5. (proper divisors of n \ ⌈n/2⌉ only)

- **DSL**: `["diff", ["divisors"], ["halve"]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n \ ⌈n/2⌉ only)
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `dc983c7d822a`  (surfaced by seed(s) [3])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 6, the P-positions are exactly n ≡ 1 (mod 2).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["diff", ["divisors"], ["halve"]]' --N 20000
```

## 6. (proper divisors of n ∪ {1,8,9})

- **DSL**: `["union", ["divisors"], ["const", [1, 8, 9]]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n ∪ {1,8,9})
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `b3f28c48a4b6`  (surfaced by seed(s) [3])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 34, the P-positions are exactly n ≡ 1, 3, 7, 13 (mod 16).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["union", ["divisors"], ["const", [1, 8, 9]]]' --N 20000
```

## 7. ((proper divisors of n + 1) + 3)

- **DSL**: `["shift", 3, ["shift", 1, ["divisors"]]]`
- **Rule (human-readable)**: subtract s ∈ ((proper divisors of n + 1) + 3)
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `a844e79c5e78`  (surfaced by seed(s) [3])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 10, the P-positions are exactly n ≡ 1 (mod 2).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["shift", 3, ["shift", 1, ["divisors"]]]' --N 20000
```

## 8. (proper divisors of n ∪ {1..2})

- **DSL**: `["union", ["divisors"], ["range", 1, 2]]`
- **Rule (human-readable)**: subtract s ∈ (proper divisors of n ∪ {1..2})
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `e3d3d70469d9`  (surfaced by seed(s) [3])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 5, the P-positions are exactly n ≡ 1 (mod 3).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["union", ["divisors"], ["range", 1, 2]]' --N 20000
```

## 9. [if n≡1 (mod 4): squares ≤ n else: {3,8,9}]

- **DSL**: `["ifmod", 4, 1, ["squares"], ["const", [3, 8, 9]]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡1 (mod 4): squares ≤ n else: {3,8,9}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `d30d67788cc1`  (surfaced by seed(s) [4])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 1, the P-positions are exactly n ≡ 0, 2, 4, 6 (mod 16).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 4, 1, ["squares"], ["const", [3, 8, 9]]]' --N 20000
```

## 10. [if n≡1 (mod 2): nonzero base-12 digits of n else: {1,6,9}]

- **DSL**: `["ifmod", 2, 1, ["digits", 12], ["const", [1, 6, 9]]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡1 (mod 2): nonzero base-12 digits of n else: {1,6,9}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `1c15640ab121`  (surfaced by seed(s) [5])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 1, the P-positions are exactly n ≡ 0, 2, 4 (mod 12).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 2, 1, ["digits", 12], ["const", [1, 6, 9]]]' --N 20000
```

## 11. [if n≡1 (mod 5): squares ≤ n else: {2..2}]

- **DSL**: `["ifmod", 5, 1, ["squares"], ["range", 2, 2]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡1 (mod 5): squares ≤ n else: {2..2}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `ca7c05450a3c`  (surfaced by seed(s) [5])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 15, the P-positions are exactly n ≡ 2, 3 (mod 5).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 5, 1, ["squares"], ["range", 2, 2]]' --N 20000
```

## 12. [if n≡2 (mod 5): squares ≤ n else: {2..2}]

- **DSL**: `["ifmod", 5, 2, ["squares"], ["range", 2, 2]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡2 (mod 5): squares ≤ n else: {2..2}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `85e7e856a4f5`  (surfaced by seed(s) [5])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 16, the P-positions are exactly n ≡ 3, 4 (mod 5).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 5, 2, ["squares"], ["range", 2, 2]]' --N 20000
```

## 13. [if n≡2 (mod 5): squares ≤ n else: {1..3}]

- **DSL**: `["ifmod", 5, 2, ["squares"], ["range", 1, 3]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡2 (mod 5): squares ≤ n else: {1..3}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `ef3508a472d8`  (surfaced by seed(s) [5])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 25, the P-positions are exactly n ≡ 3 (mod 5).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 5, 2, ["squares"], ["range", 1, 3]]' --N 20000
```

## 14. [if n≡1 (mod 3): squares ≤ n else: {3..6}]

- **DSL**: `["ifmod", 3, 1, ["squares"], ["range", 3, 6]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡1 (mod 3): squares ≤ n else: {3..6}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `be46689174c6`  (surfaced by seed(s) [5])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 9, the P-positions are exactly n ≡ 0, 8 (mod 9).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 3, 1, ["squares"], ["range", 3, 6]]' --N 20000
```

## 15. [if n≡1 (mod 5): squares ≤ n else: {1..2}]

- **DSL**: `["ifmod", 5, 1, ["squares"], ["range", 1, 2]]`
- **Rule (human-readable)**: subtract s ∈ [if n≡1 (mod 5): squares ≤ n else: {1..2}]
- **Score**: 11.14
- **Tier**: HIDDEN_MOD_STRUCTURE
- **game_hash**: `bcb693c540b9`  (surfaced by seed(s) [5])
- **OEIS status, P-positions**: `not_found`
- **OEIS status, Grundy sequence**: `not_found`
- **Survived at N=20000**: yes

Conjecture, copied verbatim from the `analyze --N 20000` output:

```
CONJECTURE: for n ≥ 15, the P-positions are exactly n ≡ 0, 3, 7 (mod 10).
```

Reproduce with:

```bash
python3 game_hunter.py analyze --rule '["ifmod", 5, 1, ["squares"], ["range", 1, 2]]' --N 20000
```

---

Every entry also emitted the same boilerplate follow-up line, reproduced once
here rather than fifteen times:

```
Proof strategy: induction on n. Show (i) every move from a claimed P-position lands on a claimed N-position, and (ii) from every claimed N-position some move lands on a claimed P-position.
```

All items above are unproven conjectures pending human verification.
