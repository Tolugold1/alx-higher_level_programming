#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        """Test if max int is greater than 1"""
        self.assertGreater(max_integer([2, 4, 1, 5]), 1)

    def test_max_equal(self):
        """Test if max int is equal to 9"""
        self.assertEqual(max_integer([8, 4, 2, 7, 4, 9]), 9)

    def test_max_less(self):
        """Test if 47 is less than max"""
        self.assertLess(47, max_integer([1, 4, 9, 8, 45, 66]))

    def test_not_equal(self):
        """Test if max int is not equal to 8"""
        self.assertNotEqual(max_integer([1, 4, 6, 3, 9]), 8)

    def test_is(self):
        """Test if max int is the same as 9"""
        self.assertIs(max_integer([1, 4, 2, 6, 9]), 9)



    def test_is_not(self):
        """testing for other datatype"""
        self.assertEqual(max_integer("Boys"), 'y')

    def test_tuple(self):
        """Test for tuple possibility"""
        self.assertEqual(max_integer((1, 3, 6, 7, 98)), 98)

    def test_none(self):
        """Test if nothing is passed"""
        self.assertEqual(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
