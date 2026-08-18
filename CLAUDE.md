# GameHunter — project memory for Claude Code

GameHunter is an automated conjecture-hunting engine for impartial combinatorial
games (single Python file, `game_hunter.py`). It proposes invented games, computes
Sprague-Grundy values, detects structure, and outputs CONJECTURES. The human owner
proves them. Read README.md before making changes.

## Commands
- Trust check / regression test: `python game_hunter.py demo --offline`
- Search: `python game_hunter.py hunt --gens 25 --pop 40 --seed <k>`
- Inspect one game: `python game_hunter.py analyze --rule '<DSL JSON>' --N 20000`

## THE FIREWALL (never violate, never "improve away")
1. You may edit engineering code: DSL primitives, performance, CLI, detectors,
   v2 features. You may NOT add AI/LLM calls anywhere inside the verifier or
   detector paths — pattern detection stays 100% deterministic.
2. REGRESSION RULE: after ANY code edit, run the demo and confirm all five
   classics still detect correctly: {1,2,3} → period 4; powers of 2 → P ≡ 0
   (mod 3); proper divisors → P = odd n; base-10 digits → P ≡ 0 (mod 10);
   squares → chaotic (P-positions matching OEIS A030193). If any of these
   change, your edit broke a detector: fix or revert before anything else.
3. Never mark any conjecture as proved, confirmed, or verified. Never write
   proof claims, novelty claims, or edited results into reports, logs, or
   OEIS submissions. Conjecture wording stays exactly as the detectors emit it.
4. Never tune scores, thresholds, or detector tolerances to make results
   "look better." Threshold changes require a correctness justification in the
   commit message, and rule 2 still applies.
5. LLM-proposed game rules enter ONLY through `llm_propose()`, and every
   proposal passes `valid()` + the Grundy engine like any random mutation.
6. Proofs are the human's work. When asked, you may explain theory or critique
   a proof attempt in chat — but nothing you say is a verification.
7. The proofs/ directory contains human-authored mathematics only. Agents
   may create empty placeholder files there when asked, but must never
   write, edit, summarize, or "fix" mathematical content in that directory.
8. Every claim names its tier: executed (output pasted, execution site
   named), drafted (author named), or asserted --- and when the artifact
   does not exist, the only legal sentence is "there is nothing to paste."
   Receipts are checked hardest when they flatter.

## Engineering constraints
- Standard library only. Do not add dependencies without asking.
- Keep Python 3.9+ compatibility and the single-file structure for v1.
- Never delete `hunt_log.jsonl` or `report_*.json` — they are the research log.
