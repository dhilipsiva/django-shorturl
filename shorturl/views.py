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
from shorturl.dbapi import get_key_path
from shorturl.conf import SU_REDIRECT_DOMAIN


def expand(request, key):
    """
    Expands the short url into actual url and redirects the request.
    """
    kp = get_key_path(key=key)
    if kp:
        return HttpResponseRedirect(SU_REDIRECT_DOMAIN + kp.path)
    else:
        return HttpResponseRedirect(SU_REDIRECT_DOMAIN + "/404")
