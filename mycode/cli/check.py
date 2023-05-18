#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from .. import __version__

def _check_version(context, param, value):
    if not value or context.resilient_parsing:
        return
    current = __version__
    latest = "Unknown"
    print(f"You are currently using v{current} the latest is v{latest}")
    context.exit()
