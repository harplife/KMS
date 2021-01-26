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
    return db


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


if __name__ == '__main__':
    app.run(use_reloader=False, port=8003, host='0.0.0.0')