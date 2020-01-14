#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """
        Check function max_integer([..])
    """
    def test_correct_list(self):
        self.assertEqual(max_integer([1, 2, 4, 6]), 6)
        self.assertEqual(max_integer([54, 344, 788, 2]), 788)
        self.assertEqual(max_integer([2, 4, -7, 5]), 5)
        self.assertEqual(max_integer([-3, 4.7, 9, 23]), 23)
        self.assertEqual(max_integer([]), None)

    def test_strings(self):
        with self.assertRaises(TypeError):
            max_integer([3, "l", 4, 9])
        with self.assertRaises(TypeError):
            max_integer(["sol", 5, 6, 7])
        with self.assertRaises(TypeError):
            max_integer([6, 78, "hi", 70, "arg"])
        with self.assertRaises(TypeError):
            max_integer([4], "helloo", [3, 8])
        with self.assertRaises(TypeError):
            max_integer(84, [5, 6], "h", 8)
        with self.assertRaises(TypeError):
            max_integer(3.8, 5, [3, 7], "9")

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(3, 5)
        with self.assertRaises(TypeError):
            max_integer("hi", 5)
        with self.assertRaises(TypeError):
            max_integer("hola", "hello")
        with self.assertRaises(TypeError):
            max_integer([4, 5], [3, 8])
        with self.assertRaises(TypeError):
            max_integer([4, 5], 90)
        with self.assertRaises(TypeError):
            max_integer(3, [78], 8)
        with self.assertRaises(TypeError):
            max_integer(4, [83, 9])
        with self.assertRaises(TypeError):
            (max_integer[8, [89], 9])
        with self.assertRaises(TypeError):
            max_integer[8, [89], 9]
