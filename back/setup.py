#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="taiga-contrib-access-token-auth",
    version="0.3",
    description="The Taiga plugin for Access Token authentication",
    long_description="",
    keywords="taiga, access token, auth, plugin",
    author="untitledds",
    author_email="untitledds@gmail.com",
    url="https://github.com/untitledds/taiga-contrib-access-token-auth",
    license="AGPL",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "django > 3, < 4",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
)