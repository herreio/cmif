#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test creation of file in CMI format

Creator:          D. Herre
GitHub:       herreio/cmif

Created:        2020-05-03
Last Modified:  2020-05-03
"""

from cmif import build, local

test_dir = local.os.path.dirname(__file__)
test_out = local.os.path.join(test_dir, "output")

root = build.tei_root()

local.writer(root, file="cmif.xml", path=test_out)
