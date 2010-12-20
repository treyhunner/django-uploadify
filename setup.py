#!/usr/bin/env python

#This project forked from http://github.com/tstone/django-uploadify
#which lacked a setup.py file.

from distutils.core import setup

setup(name='django-uploadify',
        description='Django integration of Uploadify jQuery plugin.',
        author='Glenn Siegman',
        author_email='gsiegman@gsiegman.com',
        url='http://github.com/gsiegman/django-uploadify',
        packages=['uploadify', 'uploadify.templatetags'],
        package_data={'uploadify': ['templates/uploadify/*.html']}
)
