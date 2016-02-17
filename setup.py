#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import sys, os
from setuptools import setup, find_packages
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mtgsdk'))
from config import __version__, __pypi_packagename__, __github_username__, __github_reponame__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
    'vcrpy'
]

url='https://github.com/' + __github_username__ + '/' + __github_reponame__
download_url="{}/tarball/{}".format(url, __version__)

setup(
    name=__pypi_packagename__,
    version=__version__,
    description='Magic: The Gathering SDK for magicthegathering.io',
    long_description='''
Magic: The Gathering SDK is a python wrapper around the MTG API located at magicthegathering.io
''',
    keywords='mtg sdk magic gathering gatherer api rest',
    author='Andrew Backes',
    author_email='backes.andrew@gmail.com',
    url=url,
    download_url=download_url,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'mtgsdk=mtgsdk.cli:main',
        ],
    },
)
