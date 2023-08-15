#!/usr/bin/python3
"""A script that starts a Flask web app with routes"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Function called with /states_list route"""
    state_dict = storage.all("State")
    state_list = []
    for state in state_dict.values():
        state_list.append(state)
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def fetch_data():
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
