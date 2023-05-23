from . import __apiroot__
from flask import current_app

@current_app.route(__apiroot__)
def index():
    return "<Root>"
