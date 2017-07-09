#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

from mtgsdk.querybuilder import QueryBuilder


class Card(object):
    RESOURCE = 'cards'

    def __init__(self, response_dict={}):
        self.name = response_dict.get('name')
        self.layout = response_dict.get('layout')
        self.mana_cost = response_dict.get('manaCost')
        self.cmc = response_dict.get('cmc')
        self.colors = response_dict.get('colors')
        self.color_identity = response_dict.get('colorIdentity')
        self.names = response_dict.get('names')
        self.type = response_dict.get('type')
        self.supertypes = response_dict.get('supertypes')
        self.subtypes = response_dict.get('subtypes')
        self.types = response_dict.get('types')
        self.rarity = response_dict.get('rarity')
        self.text = response_dict.get('text')
        self.flavor = response_dict.get('flavor')
        self.artist = response_dict.get('artist')
        self.number = response_dict.get('number')
        self.power = response_dict.get('power')
        self.toughness = response_dict.get('toughness')
        self.loyalty = response_dict.get('loyalty')
        self.multiverse_id = response_dict.get('multiverseid')
        self.variations = response_dict.get('variations')
        self.watermark = response_dict.get('watermark')
        self.border = response_dict.get('border')
        self.timeshifted = response_dict.get('timeshifted')
        self.hand = response_dict.get('hand')
        self.life = response_dict.get('life')
        self.release_date = response_dict.get('releaseDate')
        self.starter = response_dict.get('starter')
        self.printings = response_dict.get('printings')
        self.original_text = response_dict.get('originalText')
        self.original_type = response_dict.get('originalType')
        self.source = response_dict.get('source')
        self.image_url = response_dict.get('imageUrl')
        self.set = response_dict.get('set')
        self.set_name = response_dict.get('setName')
        self.id = response_dict.get('id')
        self.legalities = response_dict.get('legalities')
        self.rulings = response_dict.get('rulings')
        self.foreign_names = response_dict.get('foreignNames')

    @staticmethod
    def find(id):
        return QueryBuilder(Card).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(Card).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(Card).all()
