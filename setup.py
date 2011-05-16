#!/usr/bin/env python

#This project forked from http://github.com/gsiegman/django-uploadify

from distutils.core import setup

setup(name='django-uploadify',
        description='Django integration of Uploadify jQuery plugin.',
        author='Vlad Frolov',
        author_email='frolvlad@gmail.com',
        url='http://github.com/frol/django-uploadify',
        packages=['uploadify', 'uploadify.templatetags'],
        package_data={'uploadify': ['templates/uploadify/*.html']}
)
