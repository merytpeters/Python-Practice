#!/usr/bin/env python3
"""Learning flask, Trying Webpages"""
from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route("/")
def homepage():
    return "Hello, welcome to the main page <h1>HELLO<h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("homepage"))


if __name__ == "__main__":
    app.run()
