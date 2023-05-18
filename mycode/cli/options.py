#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import requests

_common_options = [
    click.argument("directory", type=str),
    click.option("--authenticate", is_flag=True, default=None),
    click.option("--config", type=str, default=None),
    click.option("--disable-module", multiple=True, default=None, type=str),
    click.option("--exclude-id", default=None, multiple=True),
    click.option("--exclude-id-file", default=None, multiple=True),
    click.option("--file-scheme", default=None, type=str),
    click.option("--filename-restriction-scheme", type=click.Choice(("linux", "windows")), default=None),
    click.option("--folder-scheme", default=None, type=str),
    click.option("--ignore-user", type=str, multiple=True, default=None),
    click.option("--include-id-file", multiple=True, default=None),
    click.option("--log", type=str, default=None),
    click.option("--opts", type=str, default=None),
    click.option("--saved", is_flag=True, default=None),
    click.option("--search", default=None, type=str),
    click.option("--submitted", is_flag=True, default=None),
    click.option("--subscribed", is_flag=True, default=None),
    click.option("--time-format", type=str, default=None),
    click.option("--upvoted", is_flag=True, default=None),
    click.option("-L", "--limit", default=None, type=int),
    click.option("-l", "--link", multiple=True, default=None, type=str),
    click.option("-m", "--multireddit", multiple=True, default=None, type=str),
    click.option(
        "-S", "--sort", type=click.Choice(("hot", "top", "new", "controversial", "rising", "relevance")), default=None
    ),
    click.option("-s", "--subreddit", multiple=True, default=None, type=str),
    click.option("-t", "--time", type=click.Choice(("all", "hour", "day", "week", "month", "year")), default=None),
    click.option("-u", "--user", type=str, multiple=True, default=None),
    click.option("-v", "--verbose", default=None, count=True),
]

_downloader_options = [
    click.option("--make-hard-links", is_flag=True, default=None),
    click.option("--max-wait-time", type=int, default=None),
    click.option("--no-dupes", is_flag=True, default=None),
    click.option("--search-existing", is_flag=True, default=None),
    click.option("--skip", default=None, multiple=True),
    click.option("--skip-domain", default=None, multiple=True),
    click.option("--skip-subreddit", default=None, multiple=True),
    click.option("--min-score", type=int, default=None),
    click.option("--max-score", type=int, default=None),
    click.option("--min-score-ratio", type=float, default=None),
    click.option("--max-score-ratio", type=float, default=None),
]

_archiver_options = [
    click.option("--all-comments", is_flag=True, default=None),
    click.option("--comment-context", is_flag=True, default=None),
    click.option("-f", "--format", type=click.Choice(("xml", "json", "yaml")), default=None),
]

def _add_options(opts: list):
    def wrap(func):
        for opt in opts:
            func = opt(func)
        return func

    return wrap
