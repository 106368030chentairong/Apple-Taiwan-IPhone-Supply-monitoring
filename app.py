import os

from flask import Flask, abort, request
from lib.iphone_check import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def callback():
    if request.method == "GET":
        return "Hello Heroku"
