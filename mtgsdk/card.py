#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

from mtgsdk.querybuilder import QueryBuilder


class Card(dict):
    RESOURCE = 'cards'

    """Usual attributes :
    artist, border, cmc, color_identity, colors, flavor, foreign_names, hand,
    id, image_url, layout, legalities, life, loyalty, mana_cost, multiverse_id,
    name, names, number, original_text, original_type, power, printings, rarity,
    release_date, rulings, set, set_name, source, starter, subtypes, supertypes,
    text, timeshifted, toughness, type, types, variations, watermark.
    See online docs for details."""

    def __new__(cls, response_dict=dict()) :
            return dict.__new__(__class__, response_dict)

    @staticmethod
    def find(id):
        return QueryBuilder(__class__).find(id)

    @staticmethod
    def where(**kwargs):
        return QueryBuilder(__class__).where(**kwargs)

    @staticmethod
    def all():
        return QueryBuilder(__class__).all()
