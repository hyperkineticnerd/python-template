#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
__apiroot__ = "/v1/api"
__all__ = ["hello", "index", "home", "app"]

@app.route("/")
def redirect():
    return app.redirect(__apiroot__ + "/home")

with app.app_context():
    from . import hello
    from . import index
    from . import home
