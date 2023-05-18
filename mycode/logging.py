#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger()

def silence_module_loggers():
    logging.getLogger("praw").setLevel(logging.CRITICAL)
    logging.getLogger("prawcore").setLevel(logging.CRITICAL)
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)
