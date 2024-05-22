import unittest

from bst import *


class TestCases(unittest.TestCase):

    def test_comes_before(self):
        self.assertEqual(comes_before(3, 6), True)
        self.assertEqual(comes_before('b', 'a'), False)

    def test_is_empty(self):
        self.assertEqual(is_empty(Node(None, None, None)), True)
        self.assertEqual(is_empty(Node(5, Node(2, None, None), None)), False)

    def test_insert(self):
        expected = Node(5, Node(2, None, None), Node(6, None, None))
        initial = Node(5, Node(2, None, None), None)
        self.assertEqual(insert(initial, 6), expected)

    def test_lookup(self):
        tree = Node(9, Node(6, None, None), None)
        self.assertEqual(lookup(tree, 6), True)
        self.assertEqual(lookup(tree, 5), False)

    def test_delete(self):
        initial_1 = Node(7, Node(6, Node(5, None, None), None), Node(8, None, None))
        expected_1 = Node(7, Node(5, None, None), Node(8, None, None))
        initial_2 = Node(9, Node(3, Node(1, None, None), None), None)
        expected_2 = Node(3, Node(1, None, None), None)

        self.assertEqual(delete(initial_1, 6), expected_1)
        self.assertEqual(delete(initial_2, 9), expected_2)
    def test_delete2(self):
        bst = Node(30, Node(25, 10, 50), Node(75, Node(60, None, 63), 90))
        bst = delete(bst, 30)
        self.assertEqual(bst.c, 60)
        self.assertEqual(bst.l.c, 25)
        self.assertEqual(bst.r.l, 63)