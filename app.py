import os

from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def callback():
    if request.method == "GET":
        return "Hello Heroku"