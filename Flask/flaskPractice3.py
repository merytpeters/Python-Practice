#!/usr/bin/env python3
"""Learning flask, Trying Webpages"""
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/<name>")
def homepage(name):
    return render_template("ted.html", content=name, r=2)


if __name__ == "__main__":
    app.run()
