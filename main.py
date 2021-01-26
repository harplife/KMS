'''
RMS: Recipe Management System

DB will be sqlite, for convenience.

The app will be executable, with data files.
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(use_reloader=False, port=8003, host='0.0.0.0')