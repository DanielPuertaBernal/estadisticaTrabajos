# estadisticaTrabajos

Coursework for **Estadística III** — Ingeniería de Sistemas, Universidad Católica de Oriente.

## Current work

**Taller 07 — Estadística descriptiva y análisis exploratorio de datos (EDA)**
See [`07 - Taller estadistica descriptiva y EDA.md`](07%20-%20Taller%20estadistica%20descriptiva%20y%20EDA.md)
for the full brief. Dataset: `data/07 - canciones.csv` (2000 rows x 17 columns,
global hit songs 2000-2019).

## Environment

Dependencies are managed with [uv](https://docs.astral.sh/uv/); the virtual
environment lives in `.venv` (Python 3.12, not committed).

```bash
uv sync                 # recreate .venv from pyproject.toml + uv.lock
uv run jupyter lab      # notebook workflow (deliverable is .ipynb)
```

If `uv` is not on PATH: `export PATH="$HOME/.local/bin:$PATH"`.

In VS Code, select the interpreter at `.venv/bin/python`.

Stack: pandas, numpy, matplotlib, seaborn, jupyterlab, openpyxl.

## Dataset notes

Findings from the initial inspection of `data/07 - canciones.csv`:

- The brief describes an `explicit` column that **is not present** in either the
  `.csv` or the `.xlsx`. Exercises 5 and 7 depend on it.
- Genres are multi-valued and separated by `"; "`, not by commas as the brief states.
- No null values, but 59 fully duplicated rows.
- `key` and `mode` are integers encoding categories, not quantities.
