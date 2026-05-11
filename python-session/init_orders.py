"""Build cafe_data.db for the Python↔SQL session.

Creates three tables — menu, customers, orders — with seed data that's
rich enough to compute KPIs (top seller, revenue by category, avg basket).
"""
import os
import random
import sqlite3
from datetime import date, timedelta

random.seed(42)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'cafe_data.db')

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.executescript("""
CREATE TABLE menu (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    price       REAL NOT NULL,
    category    TEXT NOT NULL
);

CREATE TABLE customers (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    signup_date TEXT NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    menu_id     INTEGER NOT NULL,
    quantity    INTEGER NOT NULL,
    order_date  TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (menu_id)     REFERENCES menu(id)
);
""")

menu_items = [
    (1, 'Espresso',         2.50, 'Coffee'),
    (2, 'Cappuccino',       3.50, 'Coffee'),
    (3, 'Latte',             3.75, 'Coffee'),
    (4, 'Flat White',        3.75, 'Coffee'),
    (5, 'Blueberry Muffin',  2.00, 'Bakery'),
    (6, 'Croissant',         2.50, 'Bakery'),
    (7, 'Chocolate Cookie',  1.75, 'Bakery'),
    (8, 'Green Tea',         2.75, 'Tea'),
]
cur.executemany('INSERT INTO menu VALUES (?, ?, ?, ?)', menu_items)

customers = [
    (1,  'Anna',     '2026-01-15'),
    (2,  'Beatriz',  '2026-02-03'),
    (3,  'Chiara',   '2026-02-20'),
    (4,  'Dilek',    '2026-03-01'),
    (5,  'Elena',    '2026-03-10'),
    (6,  'Fatima',   '2026-03-18'),
    (7,  'Greta',    '2026-03-25'),
    (8,  'Hana',     '2026-04-02'),
    (9,  'Iris',     '2026-04-08'),
    (10, 'Jana',     '2026-04-15'),
]
cur.executemany('INSERT INTO customers VALUES (?, ?, ?)', customers)

start = date(2026, 4, 1)
orders = []
order_id = 1
for day_offset in range(30):
    day = start + timedelta(days=day_offset)
    # 2-5 orders per day
    for _ in range(random.randint(2, 5)):
        customer_id = random.randint(1, 10)
        menu_id = random.choices(
            [1, 2, 3, 4, 5, 6, 7, 8],
            weights=[3, 4, 5, 2, 3, 2, 2, 1],   # latte/cappuccino most popular
        )[0]
        quantity = random.choices([1, 2, 3], weights=[6, 3, 1])[0]
        orders.append((order_id, customer_id, menu_id, quantity, day.isoformat()))
        order_id += 1

cur.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?)', orders)
conn.commit()
conn.close()

print(f'Built {DB_PATH}')
print(f'  menu:      {len(menu_items)} rows')
print(f'  customers: {len(customers)} rows')
print(f'  orders:    {len(orders)} rows')
