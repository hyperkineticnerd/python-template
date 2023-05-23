from flask import current_app
from .. import __apiroot__

@current_app.route(__apiroot__+"/firewall")
def add_port_forward():
    pass
