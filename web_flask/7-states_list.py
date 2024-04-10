#!/usr/bin/python3
""" flask for states"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def shutdown(exception):
    """close the storage after each requests"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a list of states"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == '__main__':
    """ Main """
    app.run(host='0.0.0.0', port=5000)
