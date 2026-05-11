# 3. Python for Data Analysis

All materials for this session live in the [`python-session/`](python-session/) folder. Start with its [README](python-session/README.md).

## 3.0 Before class — verify your setup

Install Python (3.9+), pandas, and Jupyter, then run the setup check so we don't lose time debugging installs in class:

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install pandas jupyter
cd python-session
python init_orders.py
python check_setup.py
```

You should see all green ✅ checks. If anything fails, post in Slack before class — we'll help you fix it.

**Goal:** Have a working Python + pandas + Jupyter setup so you can start coding the moment class begins.

## 3.1 Python fundamentals — Café Cozy order calculator

Open `python-session/01_python_fundamentals.ipynb` and complete the TODO cells. You'll build a checkout function that sums an order, applies a discount, and decides on a free-muffin promo.

**Goal:** Be comfortable with Python variables, lists of dictionaries, `for` loops, and `if`/`else`.

## 3.2 Data cleaning with pandas

Open `python-session/02_pandas_cleaning.ipynb`. Clean a messy real-looking sales export — handle missing values, duplicates, inconsistent strings, German decimal commas, mixed date formats.

**Goal:** Be able to inspect a new dataset with pandas and fix the common quality issues from last week's *Data Cleaning Cycle* slide.

## 3.3 Connect Python to SQL — build an ETL pipeline

Open `python-session/03_etl_kpis.ipynb`. Connect Python to a SQLite database, write a SQL JOIN to extract data, compute three business KPIs in pandas, save the results to CSV.

**Goal:** Build the same Extract → Transform → Load pipeline you saw in Session 1, end-to-end in Python.

## 3.4 (Stretch) Pick one stretch goal

Each notebook has bonus tasks at the bottom. Pick one that interests you. Examples: who is the most loyal customer? Plot a daily revenue trend. Write your KPI table back into the SQLite database.

**Goal:** Practice combining what you learned without step-by-step guidance.
