#! /usr/bin/env Python2

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return("Hello world!")
