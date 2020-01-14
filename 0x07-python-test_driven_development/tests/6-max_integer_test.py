#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_correct_list(self):
        self.assertEqual(max_integer([1, 2, 4, 6]), 6)
        self.assertEqual(max_integer([54, 344, 788, 2]), 788)
        self.assertEqual(max_integer([2, 4, -7, 5]), 5)

    def test_strings(self):
        with self.assertRaises(TypeError):
            max_integer([3, "l", 4, 9])
        with self.assertRaises(TypeError):
            max_integer(["sol", 5, 6, 7])
        with self.assertRaises(TypeError):
            max_integer([6, 78, "hi", 70, "arg"])

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(3, 5)

