# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='simplereport',
    version="1.0",
    description="A Django app that allows addition of sql reports",
    author="Joseph Rose",
    author_email="josephdrose@gmail.com",
    url="https://github.com/josephdrose/django-simplereport",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Django>=1.4"],
)
