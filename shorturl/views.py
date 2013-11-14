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
from django.http import HttpResponseRedirect
from shorturl.dbapi import get_path_for_key


def expand(request, key):
    """
    Expands the short url into actual url and redirects the request.
    """
    path = get_path_for_key(key)
    if path:
        return HttpResponseRedirect(path)
    else:
        return HttpResponseRedirect("/404")
