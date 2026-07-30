# Characterization and Proof of the Foursquare Subtraction Game

## 1. Game Definition and Rules

The **Foursquare Subtraction Game** is an impartial game played on a non-negative integer state $n \in \mathbb{N}_0$ under normal play rules (a player with no legal moves loses). The set of legal moves available from state $n$ is defined by:

1. **Square Mode ($n \equiv 1 \pmod 4$):** The active player may subtract any non-zero square $s = k^2$ such that $1 \le s \le n$.
2. **Standard Mode ($n \not\equiv 1 \pmod 4$):** The active player may subtract any element $s \in \{3, 8, 9\}$ such that $1 \le s \le n$.

---

## 2. Main Theorem

**Theorem 1.** *A state $n \ge 0$ in the Foursquare Subtraction Game is a P-position (previous-player winning) if and only if:*
$$n \equiv 0, 2, 4, \text{ or } 6 \pmod{16}$$
*Otherwise, $n$ is an N-position (next-player winning).*

*Partition Exhaustiveness:* The set of residues modulo 16 is exhaustively partitioned into claimed P-positions $\mathcal{P} = \{0, 2, 4, 6\} \pmod{16}$ and claimed N-positions $\mathcal{N} = \{1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15\} \pmod{16}$, such that $\mathcal{P} \cup \mathcal{N} = \mathbb{Z} / 16\mathbb{Z}$ and $\mathcal{P} \cap \mathcal{N} = \emptyset$.

---

## 3. Supporting Lemmas

### Lemma 1 (Orientation Lemma)
*Every state $n \equiv 0, 2, 4, \text{ or } 6 \pmod{16}$ is even. Consequently, $n \not\equiv 1 \pmod 4$.*

**Proof.** For any $r \in \{0, 2, 4, 6\}$, $n = 16q + r \equiv r \equiv 0 \pmod 2$. Since $n$ is even, $n \bmod 4 \in \{0, 2\}$, which implies $n \not\equiv 1 \pmod 4$. Thus, Square Mode never applies at any claimed P-position, and for $n \ge 9$, the full move set $\{3, 8, 9\}$ is strictly available. $\square$

### Lemma 2 (Odd Squares Modulo 16 Lemma)
*For any odd integer $k \in \mathbb{Z}$, $k^2 \equiv 1 \text{ or } 9 \pmod{16}$.*

**Proof.** Express any odd integer as $k = 2m + 1$ for some $m \in \mathbb{Z}$. Squaring yields:
$$k^2 = (2m + 1)^2 = 4m^2 + 4m + 1 = 4m(m + 1) + 1$$
Because $m(m + 1)$ is the product of two consecutive integers, it is always even. Let $m(m + 1) = 2j$ for $j \in \mathbb{Z}$. Substituting gives:
$$k^2 = 4(2j) + 1 = 8j + 1$$
If $j$ is even ($j = 2l$), $k^2 = 16l + 1 \equiv 1 \pmod{16}$. If $j$ is odd ($j = 2l + 1$), $k^2 = 16l + 9 \equiv 9 \pmod{16}$. Thus, every odd square is congruent to $1$ or $9 \pmod{16}$. $\square$

---

## 4. Formal Proof of Main Theorem

**Proof (by Strong Induction on $n$).**

### Base Cases ($0 \le n \le 8$)
Direct manual calculation of legal move bounds and reachable states confirms:

* $n = 0$: Standard mode, no moves $\le 0$. **P-position**.
* $n = 1$: Square mode, move $s = 1^2 \to 0$ (P). **N-position**.
* $n = 2$: Standard mode, no moves $\le 2$. **P-position**.
* $n = 3$: Standard mode, move $s = 3 \to 0$ (P). **N-position**.
* $n = 4$: Standard mode, move $s = 3 \to 1$ (N). All legal moves go to N. **P-position**.
* $n = 5$: Square mode, moves $s = 1^2 \to 4$ (P), $s = 2^2 \to 1$ (N). **N-position**.
* $n = 6$: Standard mode, move $s = 3 \to 3$ (N). **P-position**.
* $n = 7$: Standard mode, move $s = 3 \to 4$ (P). **N-position**.
* $n = 8$: Standard mode, move $s = 8 \to 0$ (P). **N-position**.

### Inductive Step ($n \ge 9$)
Assume the theorem holds for all states $m < n$.

#### Part 1: Closure (Claimed P-positions)
Let $n \equiv r \pmod{16}$ with $r \in \{0, 2, 4, 6\}$. By Lemma 1, $n \not\equiv 1 \pmod 4$. For all $n \ge 9$, all of $\{3, 8, 9\}$ are legal moves since $s \le n$. We compute $r - s \pmod{16}$ across all 12 combinations:

* $r = 0 \implies 0 - 3 \equiv 13, \quad 0 - 8 \equiv 8, \quad 0 - 9 \equiv 7 \pmod{16}$
* $r = 2 \implies 2 - 3 \equiv 15, \quad 2 - 8 \equiv 10, \quad 2 - 9 \equiv 9 \pmod{16}$
* $r = 4 \implies 4 - 3 \equiv 1, \quad 4 - 8 \equiv 12, \quad 4 - 9 \equiv 11 \pmod{16}$
* $r = 6 \implies 6 - 3 \equiv 3, \quad 6 - 8 \equiv 14, \quad 6 - 9 \equiv 13 \pmod{16}$

None of the resulting residues belong to $\{0, 2, 4, 6\} \pmod{16}$. By the strong induction hypothesis, every reachable state $n - s < n$ is an N-position. Hence, $n$ is a **P-position**.

#### Part 2: Escape (Claimed N-positions)
Let $n \equiv r \pmod{16}$ with $r \in \mathcal{N}$. We display a legal move $s$ such that $n - s \in \mathcal{P}$:

1. **Non-Square Residues ($r \in \{3, 7, 8, 10, 11, 12, 14, 15\}$):**
   * $r = 3$: $s = 3 \implies 3 - 3 \equiv 0 \in \mathcal{P}$
   * $r = 7$: $s = 3 \implies 7 - 3 \equiv 4 \in \mathcal{P}$
   * $r = 8$: $s = 8 \implies 8 - 8 \equiv 0 \in \mathcal{P}$
   * $r = 10$: $s = 8 \implies 10 - 8 \equiv 2 \in \mathcal{P}$
   * $r = 11$: $s = 9 \implies 11 - 9 \equiv 2 \in \mathcal{P}$
   * $r = 12$: $s = 8 \implies 12 - 8 \equiv 4 \in \mathcal{P}$
   * $r = 14$: $s = 8 \implies 14 - 8 \equiv 6 \in \mathcal{P}$
   * $r = 15$: $s = 9 \implies 15 - 9 \equiv 6 \in \mathcal{P}$

   Since $n \ge 9$, $s \le n$ is satisfied in all cases.

2. **Square-Mode Residues ($r \in \{1, 5, 9, 13\}$):**
   By Lemma 2, odd squares satisfy $k^2 \equiv 1 \text{ or } 9 \pmod{16}$. Using $s = 1^2 = 1$ or $s = 3^2 = 9$:
   * $r = 1$: $s = 1 \implies 1 - 1 \equiv 0 \in \mathcal{P}$
   * $r = 5$: $s = 1 \implies 5 - 1 \equiv 4 \in \mathcal{P}$
   * $r = 9$: $s = 9 \implies 9 - 9 \equiv 0 \in \mathcal{P}$
   * $r = 13$: $s = 9 \implies 13 - 9 \equiv 4 \in \mathcal{P}$

   For $r \in \{1, 5\}$, $s = 1 \le n$ holds for $n \ge 1$. For $r \in \{9, 13\}$, $s = 9 \le n$ holds for $n \ge 9$.

By strong induction, every state $n \in \mathcal{N}$ can transition to a P-position $n - s < n$. Thus, $n$ is an **N-position**. $\blacksquare$

---

## 5. Closing Remark

*No-Preperiod Remark:* The periodicity of P-positions ($\text{period} = 16$) holds strictly and purely from $n = 0$ onward, exhibiting no initial non-periodic transient phase (preperiod = 0).
