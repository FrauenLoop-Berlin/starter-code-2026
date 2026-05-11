"""Pre-session install check — run this before class to verify everything works.

Usage:   python check_setup.py
"""
import os
import sys

CHECK = '✅'
FAIL  = '❌'
WARN  = '⚠️ '

ok = True

def check(label, condition, hint=''):
    global ok
    if condition:
        print(f'  {CHECK} {label}')
    else:
        ok = False
        print(f'  {FAIL} {label}')
        if hint:
            print(f'       → {hint}')


print('\nFrauenLoop Python session — environment check')
print('=' * 50)

# 1. Python version
print('\nPython')
version_ok = sys.version_info >= (3, 9)
check(
    f'Python {sys.version.split()[0]}',
    version_ok,
    'Need Python 3.9 or newer. See https://www.python.org/downloads/',
)

# 2. Required libraries
print('\nLibraries')

try:
    import pandas as pd
    check(f'pandas {pd.__version__}', True)
except ImportError:
    check('pandas', False, 'Run:  pip install pandas')

try:
    import sqlite3
    check(f'sqlite3 {sqlite3.sqlite_version} (stdlib)', True)
except ImportError:
    check('sqlite3', False, 'Should come with Python — reinstall Python')

try:
    import jupyter      # noqa: F401
    check('jupyter', True)
except ImportError:
    check('jupyter', False, 'Run:  pip install jupyter')

# 3. Files in this folder
print('\nFiles')
here = os.path.dirname(os.path.abspath(__file__))

files_needed = [
    '01_python_fundamentals.ipynb',
    '02_pandas_cleaning.ipynb',
    '03_etl_kpis.ipynb',
    'dirty_sales.csv',
    'init_orders.py',
]
for f in files_needed:
    check(f, os.path.exists(os.path.join(here, f)))

# 4. The Part 3 database
print('\nDatabase (Part 3)')
db_path = os.path.join(here, 'cafe_data.db')
if os.path.exists(db_path):
    check('cafe_data.db', True)
    # Smoke-test the data
    try:
        import sqlite3
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM orders')
        n = cur.fetchone()[0]
        conn.close()
        check(f'orders table has {n} rows', n > 0,
              "Re-run:  python init_orders.py")
    except Exception as e:
        check('orders table', False, f'Error: {e}. Re-run: python init_orders.py')
else:
    check('cafe_data.db', False, 'Run:  python init_orders.py')

# 5. Final verdict
print('\n' + '=' * 50)
if ok:
    print(f'{CHECK} You are ready for the session. See you on Monday!')
    sys.exit(0)
else:
    print(f'{FAIL} Fix the items above before class. Ask in Slack if stuck.')
    sys.exit(1)
