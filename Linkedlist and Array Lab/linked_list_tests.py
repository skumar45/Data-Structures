import unittest
from typing import *
from dataclasses import dataclass
from linked_list import *

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

    def test_empty_list(self):
        self.assertEqual(empty_list([]), [])

    def test_add_to_front(self):
        self.assertEqual(add_to_front((Pair(4, Pair(9, None))), 3), (Pair(3, Pair(4, Pair(9, None)))))

    def test_add(self):
        test = (Pair(1, Pair(2, None)))
        self.assertEqual(add((Pair(3, Pair(9, None))), 1, 4), (Pair(3, Pair(4, Pair(9, None)))))
        self.assertRaises(IndexError, add, test, 4, 4)

    def test_length(self):
        self.assertEqual(length(Pair(3, Pair(7, Pair(5, None)))), 3)
        self.assertEqual(length(Pair(4, Pair(87, None))), 2)

    def test_get(self):
        self.assertEqual(get((Pair(8, Pair(3, None))), 1), 3)
        self.assertEqual(get(Pair(3, Pair(7, Pair(5, None))), 0), 3)
        test_3 = Pair(3, None)
        self.assertRaises(IndexError, add, test_3, 4, 3)


    def test_set(self):
        list_1 = Pair(8, Pair(3, None))
        list_test = Pair(8, Pair(5, None))
        list_2 = Pair(4, Pair(0, Pair(2, None)))
        list_test_2 = Pair(8, Pair(0, (Pair(2, None))))
        test_3 = Pair(3, None)
        self.assertEqual(set(list_1, 1, 5), list_test)
        self.assertEqual(set(list_2, 0, 8), list_test_2)
        self.assertRaises(IndexError, add, test_3, 4, 4)

    def test_remove(self):
        list_1 = Pair(4, Pair(3, Pair(2, None)))
        test_1 = (Pair(4, Pair(2, None)))
        list_2 = Pair(3, Pair(9, None))
        test_2 = Pair(9, None)
        test_3 = Pair(3, None)
        self.assertEqual(remove(list_1, 1), (3, test_1))
        self.assertEqual(remove(list_2, 0), (3, test_2))
        self.assertRaises(IndexError, add, test_3, 4, 4)
