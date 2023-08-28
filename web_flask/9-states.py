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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def get_state(id):
    """Retrieves the list of all City objects of a State obj"""
    state_dict = storage.all(State)
    state_list = []
    for state in state_dict.values():
        if state.to_dict()["id"] == id:
            state_list.append(state.to_dict())

    city_dict = storage.all(City)
    city_list = []
    for city in city_dict.values():
        city_list.append(city.to_dict())

    return render_template(
            '9-states.html',
            state_list=state_list,
            city_list=city_list,
            id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
