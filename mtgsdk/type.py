#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

from mtgsdk.querybuilder import QueryBuilder


class Type(object):
    RESOURCE = 'types'

    @staticmethod
    def all():
        return QueryBuilder(Type).array()
