#!/usr/bin/env python3
"""Pivot tables over the merged laws, restricted to singleton fallbacks F={a}.

Reads laws_merged.json. Keeps only records whose fallback branch is ["const",[a]]
with a in 1..9. For each branch order emits two grids, rows m=2..8, columns
a=1..9:

  table A -- cell = the distinct law moduli across all r for that (m, a)
  table B -- cell = the distinct residue-set sizes across all r for that (m, a)

A cell with no law in any r is a dash.

Reads only; modifies nothing. No OEIS calls.

Firewall: PIVOT_SINGLETON.md carries the grids and their definitions and nothing
else -- no commentary, no proposed relationship between (m, r, a) and the moduli
or residue-set sizes, and no reworded conjecture. Pattern-finding in these grids
is the human's task.
"""

import json

SRC = "laws_merged.json"
OUT = "PIVOT_SINGLETON.md"

MS = list(range(2, 9))
AS = list(range(1, 10))
ORDERS = ["squares / F", "F / squares"]


def singleton_a(F):
    """Return a if F is ["const",[a]] with a in 1..9, else None."""
    if isinstance(F, list) and len(F) == 2 and F[0] == "const":
        vals = F[1]
        if isinstance(vals, list) and len(vals) == 1 and vals[0] in AS:
            return vals[0]
    return None


def fmt(values):
    return "{" + ", ".join(str(v) for v in sorted(values)) + "}" if values else "–"


def grid(cells, key):
    """cells[(order,m,a)] -> list of records; key picks the value per record."""
    L = []
    L.append("| m \\ a | " + " | ".join(str(a) for a in AS) + " |")
    L.append("|---:|" + "|".join(["---"] * len(AS)) + "|")
    for m in MS:
        row = [f"| **{m}** "]
        for a in AS:
            recs = cells.get((m, a), [])
            row.append("| " + (fmt({key(z) for z in recs}) if recs else "–") + " ")
        L.append("".join(row) + "|")
    return L


def main():
    src = json.load(open(SRC))
    laws = src["laws"]

    kept = 0
    by_order = {o: {} for o in ORDERS}
    for z in laws:
        a = singleton_a(z["F"])
        if a is None or z["m"] not in MS or z["branch_order"] not in ORDERS:
            continue
        by_order[z["branch_order"]].setdefault((z["m"], a), []).append(z)
        kept += 1

    L = []
    w = L.append
    w("# Singleton-fallback pivot tables")
    w("")
    w(f"Source: `{SRC}` ({src['total']} laws; "
      f"{src['by_provenance'].get('census', 0)} provenance `census`, "
      f"{src['by_provenance'].get('rescan', 0)} provenance `rescan`).")
    w("")
    w(f"Restricted to records whose fallback branch is `[\"const\",[a]]` with")
    w(f"a in 1..9: **{kept}** of {src['total']} laws.")
    w("")
    w("Rows are m, columns are a. Each cell pools every r in 0..m-1 for that")
    w("(m, a) and lists the distinct values found. A dash means no law in any r.")
    w("`branch order` reads *then-branch / else-branch*, so `squares / F` applies")
    w("the squares move set when n ≡ r (mod m).")
    w("")
    w("Every value below is detector output at a finite range. Nothing here is")
    w("proved; all underlying laws are unproven conjectures pending human")
    w("verification.")
    w("")

    for order in ORDERS:
        cells = by_order[order]
        w(f"## Branch order `{order}`")
        w("")
        w("### Table A — distinct emergent moduli")
        w("")
        L.extend(grid(cells, lambda z: z["law"]["modulus"]))
        w("")
        w("### Table B — distinct residue-set sizes")
        w("")
        L.extend(grid(cells, lambda z: len(z["law"]["residues"])))
        w("")

    with open(OUT, "w") as fh:
        fh.write("\n".join(L).rstrip() + "\n")

    for order in ORDERS:
        filled = sum(1 for m in MS for a in AS if by_order[order].get((m, a)))
        print(f"{order:<13} cells with a law: {filled}/{len(MS) * len(AS)}  "
              f"records: {sum(len(v) for v in by_order[order].values())}")
    print(f"kept {kept} of {src['total']} laws (singleton F only)")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
