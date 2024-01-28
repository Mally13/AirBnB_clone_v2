#!/usr/bin/python3
from flask import Flask
"""Hello Flask"""


app = Flask(__name__)
@app.route("/")
def hello_world():
	"""Displays the hello world message"""
	return "<p>Hello, World!</p>"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
