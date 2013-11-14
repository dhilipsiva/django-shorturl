#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 dhilipsiva <dhilipsiva@gmail.com>
#
# http://dhilipsiva.github.io/django-shorturl/
#
# Distributed under terms of the MIT license.

"""

"""
from __future__ import unicode_literals

__author__ = 'dhilipsiva'
__version__ = (0, 1, 0)

from shorturl.dbapi import create_key_path


def shorten_path(path):
    """
    Shorten the given path if.
    """
    return create_key_path(path)
