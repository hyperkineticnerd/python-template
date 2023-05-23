from . import __apiroot__
from flask import current_app

@current_app.route(__apiroot__ + "/home")
def home():
    return "Welcome Home!"
