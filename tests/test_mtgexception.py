#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import unittest
from mtgsdk import MtgException

class TestMtgException(unittest.TestCase):
    def test_constructor_sets_description(self):
        description = "An error has occurred"
        exception = MtgException(description)
        
        self.assertEqual(description, exception.__str__())