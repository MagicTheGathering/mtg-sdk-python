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
            
            self.assertEqual(["Artifact","Conspiracy","Creature","Enchantment","Instant","Land","Phenomenon","Plane","Planeswalker","Scheme","Sorcery","Tribal","Vanguard"], types)