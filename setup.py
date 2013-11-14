#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='django-shorturl',
    version='0.1',
    description='A very simple URL Shortener Django app',
    author='dhilipsiva',
    author_email='dhilipsiva@gmail.com',
    url='http://github.com/dhilipsiva/django-shorturl/',
    long_description=open('README.md', 'r').read(),
    packages=[
        'shorturl',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'
    ],
)
