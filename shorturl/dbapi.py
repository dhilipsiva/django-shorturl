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
from shorturl.models import KeyPath
from shorturl.utils import key_generator


def get_key_path(*args, **kwargs):
    """
    Get Key path for given variables
    """
    try:
        kp = KeyPath.objects.get(*args, **kwargs)
        return kp.as_dict()
    except Exception:
        return None


def _get_unique_key():
    """
    Get an unique key for shortening
    """
    key = key_generator()
    kp = get_key_path(key=key)
    if kp:
        return _get_unique_key()
    else:
        return key


def create_key_path(path):
    """
    Create a KeyPath for for the given path if it doesnt already exsist.
    """
    """
    If the path already exsists, return it KeyPath
    """
    kp = get_key_path(path=path)
    if kp:
        return kp
    key = _get_unique_key()
    kp = KeyPath(key=key, path=path)
    kp.save()
    return kp.as_dict()
