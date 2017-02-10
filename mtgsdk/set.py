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


class Set(object):
    RESOURCE = 'sets'

    def __init__(self, response_dict={}):
        self.code = response_dict.get('code')
        self.name = response_dict.get('name')
        self.type = response_dict.get('type')
        self.border = response_dict.get('border')
        self.mkm_id = response_dict.get('mkm_id')
        self.mkm_name = response_dict.get('mkm_name')
        self.release_date = response_dict.get('releaseDate')
        self.gatherer_code = response_dict.get('gathererCode')
        self.magic_cards_info_code = response_dict.get('magicCardsInfoCode')
        self.booster = response_dict.get('booster')
        self.old_code = response_dict.get('oldCode')
        self.block = response_dict.get('block')
        self.online_only = response_dict.get('onlineOnly')

    @staticmethod
    def find(id):
        return QueryBuilder(Set).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Set).all()
        
    @staticmethod
    def generate_booster(code):
        url = "{}/{}/{}/booster".format(__endpoint__, Set.RESOURCE, code)
        return QueryBuilder(Set).find_many(url, Card, Card.RESOURCE)
