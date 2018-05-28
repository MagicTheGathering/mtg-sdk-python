#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

from mtgsdk.querybuilder import QueryBuilder
from mtgsdk.config import __endpoint__
from mtgsdk.card import Card
from string import ascii_uppercase, ascii_lowercase


class Set(object):
    RESOURCE = 'sets'

    """Usual attributes :
    block, booster, border, code, gatherer_code, magic_cards_info_code, mkm_id,
    mkm_name, name, old_code, online_only, release_date, type.
    See online docs for details."""

    # some keys in the response_dict are of the form fooBarBaz ;
    # we want them as foo_
    trans = str.maketrans({u:"_"+l for u,l in zip(ascii_uppercase, ascii_lowercase)})

    def __new__(cls, response_dict=dict()) :
        obj = object.__new__(__class__)
        obj.__dict__ = {k.translate(__class__.trans):v for k,v in response_dict.items()}
        return obj

    @staticmethod
    def find(id):
        return QueryBuilder(__class__).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(__class__).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(__class__).all()

    @staticmethod
    def generate_booster(code):
        url = "{}/{}/{}/booster".format(__endpoint__, Set.RESOURCE, code)
        return QueryBuilder(Set).find_many(url, Card, Card.RESOURCE)
