import unittest
from typing import *
from linked_list import *


class TestCases(unittest.TestCase):

    def test_object_iterator(self):
        initial = (Pair(4, Pair(87, None)))
        expected = Iterator(Pair(4, Pair(87, None)))
        self.assertEqual(object_iterator(initial), expected)

    def test_has_next(self):
        iterator = Iterator(Pair(3, Pair(9, None)))
        self.assertEqual(has_next(iterator), True)
        iterator_2 = Iterator(Pair(None, None))
        self.assertEqual(has_next(iterator_2), False)

    def test_get_next(self):
        test = Iterator(Pair(4, Pair(0, Pair(2, None))))
        test_2 = Iterator(Pair(None, Pair(0, Pair(2, None))))
        test_3 = Iterator(Pair(None, None))
        self.assertEqual(get_next(test), 4)
        self.assertEqual(get_next(test_2), 0)
        self.assertRaises(StopIteration, get_next, test_3)
