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
# coding: utf-8

# DJANGO IMPORTS
try:
    from django.conf.urls import url, patterns
except ImportError:
    # for Django version less then 1.4
    from django.conf.urls.defaults import url, patterns
from shorturl.views import expand
urlpatterns = patterns(
    '',
    url(r'^(?P<key>[a-zA-Z0-9]{6})$', expand, name="expand"))
