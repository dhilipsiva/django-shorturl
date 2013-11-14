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
There is just one simple table here.
The KeyPath table which has a key an a path.
"""

from django.db import models


class KeyPath(models.Model):
    key = models.CharField('Key', max_length=10)
    path = models.CharField('Path', max_length=255)

    def as_dict(self):
        """
        Return a python dictionary representation of a KeyPath model
        """
        return {
            'key': self.key,
            'path': self.path
        }
