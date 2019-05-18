#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import vcr
import unittest
from mtgsdk import Supertype

class TestSupertype(unittest.TestCase):
    def test_all_returns_supertypes(self):
        with vcr.use_cassette('fixtures/supertypes.yaml'):
            supertypes = Supertype.all()
            
            #API currently misplaces Host among Supertypes instead of regular types, remove Host when API is updated
            self.assertEqual(["Basic","Host","Legendary","Ongoing","Snow","World"], supertypes)
