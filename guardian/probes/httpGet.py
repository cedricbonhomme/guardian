#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests  # type: ignore[import-untyped]


def execute(param):
    r = requests.get(param)
    return r.status_code
