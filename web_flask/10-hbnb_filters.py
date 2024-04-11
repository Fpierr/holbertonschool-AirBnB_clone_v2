#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Display HBNB filters """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext                                                                                                                               def shutdown(exception):                                                                                                                                   """ Close the storage after each request """
    storage.close() 


if __name__ == '__main__':
    """ Main """
    app.run(host='0.0.0.0', port=5000)
