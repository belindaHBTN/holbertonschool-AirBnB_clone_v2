#!/usr/bin/python3
"""A script that starts a Flask web app with routes"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Retrieves the list of all State objects"""
    state_dict = storage.all(State)
    state_list = []
    for state in state_dict.values():
        state_list.append(state.to_dict())
    return render_template('7-states_list.html', state_list=state_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
