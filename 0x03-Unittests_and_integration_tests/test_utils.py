#!/usr/bin/env python3
"""
Task 0's module
"""
import unittest
from parameterized import parameterized
import utils

access_nested_map = utils.access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Nested Map testing class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, result):
        """test1"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand(
        [
            ({}, ("a",), 1),
            ({"a": 1}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, result):
        """test for exceptions"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), result)
