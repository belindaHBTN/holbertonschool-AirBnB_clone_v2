#!/usr/bin/python3
"""A script that starts a Flask web app with routes"""
from flask import Flask
from markupsafe import escape


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
