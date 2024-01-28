#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Displays the message Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world_2():
    """Displays the message HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world_3(text):
    """Displays the message C with parameter text"""
    normal_text = text.replace('_', " ")
    return f'C {normal_text}'


@app.route("/python/<text>", strict_slashes=False)
def hello_world_4(text="is cool"):
    """Displays the message Python with parameter text"""
    text = text.replace('_', " ")
    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
