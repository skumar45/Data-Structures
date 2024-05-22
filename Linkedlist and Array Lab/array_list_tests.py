import unittest
import numpy as nd
from typing import *
from dataclasses import dataclass
from array_list import *


class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)


if __name__ == '__main__':
    unittest.main()


class Tests(unittest.TestCase):

    def test_empty_lst(self):
        ta = np.array([])
        self.assertEqual(list(empty_list()), list(ta))

    def test_add_to_front(self):
        actual = np.array([9, 1, 2, 3])
        self.assertEqual(list(add_to_front([1, 2, 3], 9)), list(actual))

    def test_add(self):
        actual_1 = np.array([1, 4, 2, 3])
        self.assertEqual(list(add([1, 2, 3], 1, 4)), list(actual_1))
        self.assertRaises(IndexError, add, [1, 2, 3], 4, 4)

    def test_length(self):
        ta_1 = np.array([1, 2, 3, 4])
        ta_2 = np.array([3, 2, 5])
        self.assertEqual(length(ta_1), 4)
        self.assertEqual(length(ta_2), 3)

    def test_get(self):
        ta_1 = np.array([1, 2, 3])
        ta_2 = np.array([5, 9, 35])
        self.assertEqual(get(ta_1, 1), 2)
        self.assertEqual(get(ta_2, 0), 5)
        self.assertRaises(IndexError, get, [1, 2, 3], 4)

    def test_set(self):
        actual_1 = np.array([1, 4, 3])
        actual_2 = np.array([4, 20, 9])
        self.assertEqual(list(set([1, 2, 3], 1, 4)), list(actual_1))
        self.assertEqual(list(set([5, 20, 9], 0, 4)), list(actual_2))
        self.assertRaises(IndexError, set, [1, 2, 3], 4, 5)

    def test_remove(self):
        ta_1 = np.array([2, 3])
        ta_2 = np.array([4, 8, 5])
        actual_1 = [1, list(ta_1)]
        actual_2 = [7, list(ta_2)]
        self.assertEqual(list(remove([1, 2, 3], 0)), actual_1)
        self.assertEqual(list(remove([4, 7, 8, 5], 1)), actual_2)
        self.assertRaises(IndexError, remove, [1, 2, 3], 4)
