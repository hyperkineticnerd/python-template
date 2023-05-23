from . import __apiroot__
from flask import current_app

@current_app.route(__apiroot__ + "/hello")
def hello_world():
    return "Hello, World!"
