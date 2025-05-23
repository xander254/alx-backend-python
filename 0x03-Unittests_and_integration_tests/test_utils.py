#!/usr/bin/env python3
"""
Test Utils
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestNestedMap(unittest.TestCase):
    """
    Class to test the nested access map
    """
    @parameterized.expand([({"a": 1}, ("a",), 1),])
    def test_access_nested_map(self, nested_map, path, expected) -> None:
        """
        Test the nested map access
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
