'''
RMS: Recipe Management System

DB will be sqlite, for convenience.

The app will be executable, with data files.
'''

from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = './recipes.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('init_table.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def init_data():
    with app.app_context():
        db = get_db()
        with app.open_resource('init_data.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/db_connect')
def db_connect():
    try:
        cur = get_db().cursor()
    except Exception as e:
        raise e
    else:
        print(cur)
        return 'connected'


@app.route('/init_database')
def init_database():
    try:
        init_db()
    except Exception as e:
        raise e
    else:
        return 'database initiated'


@app.route('/populate')
def populate():
    try:
        init_data()
    except Exception as e:
        raise e
    else:
        return 'db populated.'


if __name__ == '__main__':
    app.run(use_reloader=False, port=8003, host='0.0.0.0')