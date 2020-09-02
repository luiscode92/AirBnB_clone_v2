#!/usr/binin/python3
"""
start a flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ print hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print hbnb"""
    return 'HBNB'


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
