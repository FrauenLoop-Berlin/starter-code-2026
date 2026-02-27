import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
instance_dir = os.path.join(BASE_DIR, 'instance')
os.makedirs(instance_dir, exist_ok=True)
db_path = os.path.join(instance_dir, 'coffee.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()
# Recreate the menu table with an image column (idempotent)
cur.execute('DROP TABLE IF EXISTS menu')
cur.execute(
    '''
    CREATE TABLE menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image TEXT
    )
    '''
)

# Insert sample rows with image filenames (stored under static/img/)
sample = [
    ('Espresso', 2.5, 'Strong and bold single shot', 'espresso.svg'),
    ('Cappuccino', 3.5, 'Espresso with steamed milk and foam', 'cappuccino.svg'),
    ('Latte', 3.75, 'Smooth espresso with steamed milk', 'latte.svg'),
    ('Blueberry Muffin', 2.0, 'Fresh baked muffin', 'muffin.svg'),
]
cur.executemany('INSERT INTO menu (name, price, description, image) VALUES (?, ?, ?, ?)', sample)
conn.commit()
conn.close()

print(f'Initialized database at {db_path}')
