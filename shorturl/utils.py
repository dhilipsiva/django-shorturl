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
Some utility functions
"""
# http://stackoverflow.com/q/2257441/1235072

import string
import random


def key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
