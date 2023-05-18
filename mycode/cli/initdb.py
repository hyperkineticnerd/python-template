#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

@click.command()
def initdb():
    click.echo('Initialized the database')