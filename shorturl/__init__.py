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

from shorturl.dbapi import create_key_path, get_key_path, delete_key_path
from shorturl.conf import SU_SHORT_DOMAIN


def shorten_path(path):
    """
    Shorten the given path if.
    """
    return create_key_path(path)


def get_short_path(path):
    """
    Get the Key path for the given key
    """
    return get_key_path(path=path)


def delete_path(path):
    """
    Delete the give path from shortening
    """
    return delete_key_path(path)


def get_short_url(path):
    """docstring for get_short_url"""
    kp = get_key_path(path=path)
    if kp:
        return SU_SHORT_DOMAIN + kp.as_dict()['key']
    else:
        return None
