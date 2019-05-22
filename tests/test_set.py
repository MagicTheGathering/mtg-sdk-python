#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from mtgsdk import Set

class TestSet(unittest.TestCase):
    def test_find_returns_set(self):
        with vcr.use_cassette('fixtures/ktk.yaml'):
            set = Set.find('ktk')

            self.assertEqual('KTK', set.code)
            self.assertEqual('Khans of Tarkir', set.name)
            self.assertEqual('expansion', set.type)
            #NOTE: The API doesn't seem to be providing "border" at this time
            #self.assertEqual('black', set.border)
            self.assertTrue('common' in set.booster)
            self.assertEqual('2014-09-26', set.release_date)
            #NOTE: The API doesn't seem to be providing "magic_cards_info_code at this time
            #self.assertEqual('ktk', set.magic_cards_info_code)

    def test_generate_booster_returns_cards(self):
        with vcr.use_cassette('fixtures/booster.yaml'):
            cards = Set.generate_booster('ktk')

            #NOTE: API booster size seems incorrect, returns 14 cards instead of expected 15
            self.assertEqual(14, len(cards))

            self.assertEqual('KTK', cards[0].set)

    def test_where_filters_on_name(self):
        with vcr.use_cassette('fixtures/filtered_sets.yaml'):
            sets = Set.where(name='khans of tarkir promos').all()
            
            self.assertEqual(1, len(sets))
            self.assertEqual('PKTK', sets[0].code)
            
    def test_all_returns_all_sets(self):
        with vcr.use_cassette('fixtures/all_sets.yaml'):
            sets = Set.all()

            self.assertGreater(len(sets), 190)
