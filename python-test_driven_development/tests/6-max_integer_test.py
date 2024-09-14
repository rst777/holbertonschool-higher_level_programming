#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_numbers(self):
        """Test with mixed integer and float numbers"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_string_list(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_empty_string(self):
        """Test with an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("string"), "t")

if __name__ == '__main__':
    unittest.main()
