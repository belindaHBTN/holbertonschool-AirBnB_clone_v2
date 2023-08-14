#!/usr/bin/python3
"""A script that starts a Flask web app with routes"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function called with / route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function called with /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Function called with /c/<text> route"""
    return "C" + " " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Function called with /python/ or /python/<text> route"""
    return "Python" + " " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Function called with /number/<int:n> route"""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
