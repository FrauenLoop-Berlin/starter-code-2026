from flask import Flask, render_template
import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'instance', 'coffee.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.execute('SELECT id, name, price, description FROM menu')
    menu = cur.fetchall()
    conn.close()
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/shop')
def shop():
    conn = get_db_connection()
    cur = conn.execute('SELECT id, name, price, description FROM menu')
    menu = cur.fetchall()
    conn.close()
    return render_template('shop.html', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
