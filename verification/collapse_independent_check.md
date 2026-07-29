# Independent Cross-Check: Odd-Fallback Collapse Theorem
This document is an AI re-derivation (Google Gemini, July 2026), produced
from the referee's full specification of the theorem, and verified
correct. It is retained as an independent cross-check of the
human-authored proof in proofs/collapse_theorem.md. It is NOT the
authoritative proof.
# The Odd-Fallback Collapse Theorem ($m = 2$ Family)

## 1. Introduction and Family Definition

Let $\mathcal{G}(a)$ denote the family of state-dependent subtraction games parameterized by an odd integer fallback $a \ge 1$, played on a non-negative integer state $n \in \mathbb{N}_0$ under normal play rules. The move set available from state $n$ is defined by:

* **Odd States ($n$ odd):** The active player may subtract any non-zero square $s = k^2 \le n$.
* **Even States ($n$ even):** The active player may subtract only the single fixed fallback value $s = a$ (provided $a \le n$).

In this document, we present the structural collapse of this family: for **every** odd fallback $a \ge 1$, the outcome strategy and Grundy sequence remain strictly invariant.

---

## 2. Lemma A (P-Position Invariance across Odd Fallbacks)

**Statement.** *For every odd integer $a \ge 1$, a state $n \ge 0$ in $\mathcal{G}(a)$ is a P-position if and only if $n$ is even. Equivalently, $n$ is an N-position if and only if $n$ is odd.*

**Proof (by Strong Induction on $n$).**

* **Base Case ($n = 0$):** $n = 0$ is even. The player facing state $0$ has no legal moves since no $a \ge 1$ satisfies $a \le 0$. Thus, $0$ is a **P-position**.
* **Inductive Step ($n \ge 1$):** Assume the lemma holds for all states $m < n$.

  * **Case 1 ($n$ is even):** Since $n$ is even, the active player is restricted to Standard Mode and may only subtract the odd fallback $a$. If $a > n$, no legal moves exist, so $n$ is a P-position. If $a \le n$, the reachable state $n - a$ is the difference of two even-parity/odd-parity integers (even minus odd), which is **odd**. By the strong induction hypothesis, every odd state $n - a < n$ is an N-position. Since all legal moves from $n$ lead exclusively to N-positions, $n$ is a **P-position**.

  * **Case 2 ($n$ is odd):** Since $n$ is odd, the active player enters Square Mode and may subtract any non-zero square $s = k^2 \le n$. Choosing $k = 1$ yields the legal move $s = 1^2 = 1$. The transition leads to state $n - 1$, which is **even** (odd minus odd). By the strong induction hypothesis, $n - 1 < n$ is a P-position. Since there exists a legal move to a P-position, $n$ is an **N-position**.

By strong induction, a state in $\mathcal{G}(a)$ is a P-position if and only if $n$ is even. $\blacksquare$

---

## 3. Lemma B (Grundy Sequence Collapse across Fallbacks)

**Statement.** *For all odd fallbacks $a, a' \ge 1$ and for all states $n \ge 0$, the Grundy values satisfy $G_a(n) = G_{a'}(n)$.*

**Induction Statement:** *For all $n \ge 0$, $G_a(n) = G_{a'}(n)$ holds for all odd fallbacks $a, a' \ge 1$.*

**Proof (by Strong Induction on $n$).**

* **Base Case ($n = 0$):** $G_a(0) = \text{mex}(\emptyset) = 0$ for all $a$. Thus, $G_a(0) = G_{a'}(0) = 0$.
* **Inductive Step ($n \ge 1$):** Assume $G_a(m) = G_{a'}(m)$ for all $m < n$ and all odd fallbacks.

  * **Case 1 ($n$ is even):**
    By Lemma A, any legal move from an even state $n$ under fallback $a$ transitions to an odd state $n - a$. By Lemma A, every odd state $m < n$ has $G_a(m) > 0$. Thus, the set of reachable Grundy values from $n$ contains only strictly positive integers.
    * If $a > n$, there are no legal moves, so $G_a(n) = \text{mex}(\emptyset) = 0$.
    * If $a \le n$, the only legal move is $n - a$. Since $n - a$ is an N-position, $G_a(n - a) \ge 1$. Thus:
      $$G_a(n) = \text{mex}(\{G_a(n - a)\}) = 0$$
    Therefore, for **any** odd fallback $a$, $G_a(n) = 0$ for all even $n$. Thus $G_a(n) = G_{a'}(n) = 0$.

  * **Case 2 ($n$ is odd):**
    From an odd state $n$, the legal moves are subtractions of squares $s = k^2 \le n$. Notice that the move set $\{k^2 \le n\}$ depends **only** on $n$ and is completely independent of the fallback parameter $a$. Furthermore, every transition $n \to n - k^2$ lands on a smaller state $m = n - k^2 < n$.

    By the induction hypothesis, $G_a(m) = G_{a'}(m)$ for all $m < n$. Therefore:
    $$G_a(n) = \text{mex}\left(\{G_a(n - k^2) \mid 1 \le k^2 \le n\}\right) = \text{mex}\left(\{G_{a'}(n - k^2) \mid 1 \le k^2 \le n\}\right) = G_{a'}(n)$$

By strong induction, $G_a(n) = G_{a'}(n)$ for all $n \ge 0$ and all odd fallbacks $a, a'$. $\blacksquare$

---

## 4. The Quarantine Mechanism

The independence of $\mathcal{G}(a)$ from its fallback parameter $a$ relies on a **quarantine argument**:

1. **Even Position Suppression:** At even states, the single move to $n - a$ produces a singleton set of non-zero Grundy values. The minimum excluded ordinal ($\text{mex}$) of any set containing only non-zero values is always $0$. Thus, the specific value of $a$ is quarantined—it can never change $G(n) = 0$ for even $n$.
2. **Odd Position Autonomy:** Because even positions are permanently quarantined at $G = 0$, odd positions interact with even positions only via square subtractions ($n - k^2$). Since odd squares subtract to even positions ($G=0$) and even squares subtract to odd positions ($G > 0$), the odd states form a self-contained game whose evaluation is entirely unaffected by $a$.
