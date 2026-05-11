# Python for Data Analysis — Session Materials

Hands-on materials for the FrauenLoop session on Python, pandas, and Python↔SQL integration.

## What's in here

**For students (top level)**

| File | Used in | Time | Topic |
|---|---|---|---|
| [check_setup.py](check_setup.py) | Pre-class | — | Verify Python, pandas, jupyter, and DB are ready |
| [01_python_fundamentals.ipynb](01_python_fundamentals.ipynb) | Part 1 | 10 min | Order calculation with loops conditionals |
| [dirty_sales.csv](dirty_sales.csv) | Part 2 | — | Messy sales data for cleaning exercise |
| [02_pandas_cleaning.ipynb](02_pandas_cleaning.ipynb) | Part 2 | 15 min | Clean the dirty CSV using pandas |
| [init_orders.py](init_orders.py) | Part 3 setup | — | Builds `cafe_data.db` (menu + orders + customers) |
| [03_etl_kpis.ipynb](03_etl_kpis.ipynb) | Part 3 | 25 min | Extract from SQLite, transform in pandas, load to CSV |

**SOS (`solutions/`)** - Check solution folder when you are super frustrated or to see if your solution looks different

- [solutions/01_python_fundamentals_SOLUTION.ipynb](solutions/01_python_fundamentals_SOLUTION.ipynb)
- [solutions/02_pandas_cleaning_SOLUTION.ipynb](solutions/02_pandas_cleaning_SOLUTION.ipynb)
- [solutions/03_etl_kpis_SOLUTION.ipynb](solutions/03_etl_kpis_SOLUTION.ipynb)

## Setup

From the repo root:

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install pandas jupyter
```

Build the Part 3 database:

```bash
cd python-session
python init_orders.py
```

Verify everything works:

```bash
python check_setup.py
```

You should see all green ✅ checks.

Open the notebooks with:

```bash
jupyter notebook            # or: jupyter lab
```

(VS Code also opens `.ipynb` files natively — pick your kernel after first cell run.)


## What students should already know

From earlier sessions: SQL SELECT / JOIN / GROUP BY / CASE, what a KPI is, the ETL diagram, the Data Science Lifecycle. Today bridges those concepts to Python code.

