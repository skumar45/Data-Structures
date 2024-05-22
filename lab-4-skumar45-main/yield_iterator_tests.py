from typing import *
from linked_list import *
import unittest

ll = Pair(1, Pair(2, Pair(3, None)))
for value in yield_iterator(ll):
    print(value)


class TestCases(unittest.TestCase):

    def test_yield_iterator(self):
        ll = Pair(1, Pair(2, Pair(3, None)))
        ll_2 = Pair(5, Pair(6, Pair(9, None)))
        ll_3 = Pair(None, None)
        self.assertEqual(list(yield_iterator(ll)), [1, 2, 3])
        self.assertEqual(list(yield_iterator(ll_2)), [5, 6, 9])
        self.assertEqual(list(yield_iterator(ll_3)), [None])
