#!/usr/bin/python3
""" Script to start a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def shutdown(exception):
    """ Close the storage after each request """
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """ Display a list of all states """
    all_states = storage.all(State)
    return render_template('9-states.html', all_states=all_states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """ Display the cities of a given state """
    all_states = storage.all(State)
    state = all_states.get(state_id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    """ Main """
    app.run(host='0.0.0.0', port=5000)
