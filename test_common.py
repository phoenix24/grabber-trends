#!/usr/bin/env python
"""
unit-tests for the common data fetch methods.
"""

import unittest
from mock import Mock, patch

class TestFlipkartInventory(unittest.TestCase):
        
    def test_get_items(self):
        self.assertEquals(1, len(self.inventory.get_items()))

    def test_get_item_color(self):
        actual = self.inventory.get_item_color(self.inventory.get_items()[0])
        expected = self.item[ self.attr.color ]
        self.assertEquals(expected, actual)

