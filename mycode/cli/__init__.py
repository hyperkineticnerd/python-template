#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .cli import cli
from .initdb import initdb
from .dropdb import dropdb

cli.add_command(initdb)
cli.add_command(dropdb)
