#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

from mtgsdk.querybuilder import QueryBuilder


class Changelog(object):
    RESOURCE = 'changelogs'
    
    def __init__(self, response_dict={}):
        self.id = response_dict.get('id')
        self.version = response_dict.get('version')
        self.details = response_dict.get('details')
        self.release_date = response_dict.get('releaseDate')

    @staticmethod
    def all():
        return QueryBuilder(Changelog).all()
