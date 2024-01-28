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


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)