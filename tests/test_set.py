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

class TestCard(unittest.TestCase):
    def test_find_returns_set(self):
        with vcr.use_cassette('fixtures/ktk.yaml'):
            set = Set.find('ktk')
            
            self.assertEqual('KTK', set.code)
            self.assertEqual('Khans of Tarkir', set.name)
            self.assertEqual('expansion', set.type)
            self.assertEqual('black', set.border)
            self.assertTrue('common' in set.booster)
            self.assertEqual('2014-09-26', set.release_date)
            self.assertEqual('ktk', set.magic_cards_info_code)
            
    def test_generate_booster_returns_cards(self):
        with vcr.use_cassette('fixtures/booster.yaml'):
            cards = Set.generate_booster('ktk')
            
            self.assertEqual(15, len(cards))
            self.assertEqual('KTK', cards[0].set)