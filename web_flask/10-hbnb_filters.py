#!/usr/bin/python3
"""A script that starts a Flask web app with routes"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """display a HTML page"""
    state_list = storage.all(State)
    city_list = storage.all(City)
    amenity_list = storage.all(Amenity)

    return render_template("10-hbnb_filters.html", city_list=city_list,
                           state_list=state_list, amenity_list=amenity_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
