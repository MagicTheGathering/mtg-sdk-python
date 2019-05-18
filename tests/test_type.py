#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from mtgsdk import Type

class TestType(unittest.TestCase):
    def test_all_returns_types(self):
        with vcr.use_cassette('fixtures/types.yaml'):
            types = Type.all()

            #API returns some erroneous values, but this line is correct
            #Remove temporary line and uncomment this line when API is updated
            #self.assertEqual(["Artifact","Card","Conspiracy","Creature","Emblem","Enchantment","Host","Instant","Land","Phenomenon","Plane","Planeswalker","Scheme","Sorcery","Summon","Tribal","Vanguard","You'll"], types)
            self.assertEqual(["Artifact","Card","Conspiracy","Creature","Emblem","Enchantment","Hero","instant","Instant","Land","Phenomenon","Plane","Planeswalker","Scheme","Sorcery","Summon","Tribal","Vanguard","You’ll"], types)
