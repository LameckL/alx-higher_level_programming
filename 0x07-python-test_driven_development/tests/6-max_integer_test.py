#!/usr/bin/python3
"""this is a unit test for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this cass is a tect casefor max_integer function"""

    def test_regular(self):
        """func test with regular intergers returning maximum result"""
        lst = [1, 2, 3, 4, 5]
        result = max_integer(lst)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """func test with a list of integers and non-integers,
        it should give a TypeError exception"""
        lst = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, lst)

    def test_empty(self):
        """func test with empty list, returnin none"""
        lst = []
        result = max_integer(lst)
        self.assertEqual(result, None)

    def test_negative(self):
        """test func with a list of negative values, return the maximum"""
        lst = [-2, -6, -1]
        result = max_integer(lst)
        self.assertEqual(result, -1)

    def test_float(self):
        """test func with a list mixture integers and floats, returning max"""
        lst = [3, 4.5, 2]
        result = max_integer(lst)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """func test with a parameter, raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """fun test with one integer list, returning the value of the integer"""
        lst = [45]
        result = max_integer(lst)
        self.assertEqual(result, 45)

    def test_identical(self):
        """func test with a list of identical values, returning that value"""
        lst = [8, 8, 8, 8, 8]
        result = max_integer(lst)
        self.assertEqual(result, 8)

    def test_strings(self):
        """func test with a list of strings, return the first string"""
        lst = ["hi", "hello"]
        result = max_integer(lst)
        self.assertEqual(result, "hi")

    def test_none(self):
        """func test with a none as parameter, raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
