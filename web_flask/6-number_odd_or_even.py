#!/usr/bin/python3
"""Hello Flask"""
from flask import Flask
from flask import render_template


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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_world_4(text="is cool"):
    """Displays the message Python with parameter text"""
    text = text.replace('_', " ")
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def hello_world_5(n):
    """Displays the message if a parameter is a number"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_world_6(n):
    """Displays an html page"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_world_7(n):
    """Displays an html page"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
