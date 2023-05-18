#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

@click.command()
def dropdb():
    click.echo('Dropped the database')
