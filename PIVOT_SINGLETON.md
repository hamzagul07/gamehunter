# Singleton-fallback pivot tables

Source: `laws_merged.json` (395 laws; 389 provenance `census`, 6 provenance `rescan`).

Restricted to records whose fallback branch is `["const",[a]]` with
a in 1..9: **270** of 395 laws.

Rows are m, columns are a. Each cell pools every r in 0..m-1 for that
(m, a) and lists the distinct values found. A dash means no law in any r.
`branch order` reads *then-branch / else-branch*, so `squares / F` applies
the squares move set when n ≡ r (mod m).

Every value below is detector output at a finite range. Nothing here is
proved; all underlying laws are unproven conjectures pending human
verification.

## Branch order `squares / F`

### Table A — distinct emergent moduli

| m \ a | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---|---|---|---|---|---|---|---|---|
| **2** | {2} | – | {2} | – | {2} | – | {2} | {16} | {2} |
| **3** | – | {3} | {6} | – | {3} | – | – | {3} | {18} |
| **4** | {2} | {4} | {2} | – | {2} | {12} | {2} | {16} | {2} |
| **5** | {5} | {5} | {5} | {5} | {10} | {5} | {5} | {5} | {5} |
| **6** | {2} | {12} | {2, 6} | – | {2} | {12} | {2} | {48} | {18} |
| **7** | {7} | {7} | {7} | {7} | {7} | {7} | {14} | {7} | {7} |
| **8** | {2} | {4} | {2} | {8} | {2} | {12} | {2} | {16} | – |

### Table B — distinct residue-set sizes

| m \ a | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---|---|---|---|---|---|---|---|---|
| **2** | {1} | – | {1} | – | {1} | – | {1} | {4} | {1} |
| **3** | – | {1} | {2} | – | {1} | – | – | {1} | {6} |
| **4** | {1} | {2} | {1} | – | {1} | {6} | {1} | {6} | {1} |
| **5** | {2} | {2} | {2} | {2} | {4} | {2} | {2} | {2} | {2} |
| **6** | {1} | {5} | {1, 3} | – | {1} | {5} | {1} | {20} | {9} |
| **7** | {3} | {3} | {3} | {3} | {3} | {3} | {6} | {3} | {3} |
| **8** | {1} | {2} | {1} | {4} | {1} | {6} | {1} | {7} | – |

## Branch order `F / squares`

### Table A — distinct emergent moduli

| m \ a | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---|---|---|---|---|---|---|---|---|
| **2** | {2} | – | {2} | – | {2} | – | {2} | {16} | {2} |
| **3** | – | – | – | – | – | – | – | – | – |
| **4** | – | – | – | – | – | – | – | – | – |
| **5** | – | – | – | – | – | – | – | – | – |
| **6** | – | – | – | – | – | – | – | – | – |
| **7** | – | – | – | – | – | – | – | – | – |
| **8** | – | – | – | – | – | – | – | – | – |

### Table B — distinct residue-set sizes

| m \ a | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---|---|---|---|---|---|---|---|---|
| **2** | {1} | – | {1} | – | {1} | – | {1} | {4} | {1} |
| **3** | – | – | – | – | – | – | – | – | – |
| **4** | – | – | – | – | – | – | – | – | – |
| **5** | – | – | – | – | – | – | – | – | – |
| **6** | – | – | – | – | – | – | – | – | – |
| **7** | – | – | – | – | – | – | – | – | – |
| **8** | – | – | – | – | – | – | – | – | – |
