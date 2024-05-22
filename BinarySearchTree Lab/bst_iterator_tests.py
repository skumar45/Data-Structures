import unittest
from bst import *


class BSTIteratorTests(unittest.TestCase):

    def test_prefix_iterator(self):
        tree1 = BinarySearchTree(lambda x, y: x <= y, Node(4, Node(2, None, None), Node(6, None, None)))
        expected1 = [4, 2, 6]
        self.assertEqual(list(prefix_iterator(tree1)), expected1)
        tree2 = BinarySearchTree(lambda x, y: x <= y, Node(10, Node(5, None, None), Node(15, None, None)))
        expected2 = [10, 5, 15]
        self.assertEqual(list(prefix_iterator(tree2)), expected2)

    def test_infix_iterator(self):
        tree1 = BinarySearchTree(lambda x, y: x <= y, Node(4, Node(2, None, None), Node(6, None, None)))
        expected1 = [2, 4, 6]
        self.assertEqual(list(infix_iterator(tree1)), expected1)
        tree2 = BinarySearchTree(lambda x, y: x <= y, Node(10, Node(5, None, None), Node(15, None, None)))
        expected2 = [5, 10, 15]
        self.assertEqual(list(infix_iterator(tree2)), expected2)

    def test_postfix_iterator(self):
        tree1 = BinarySearchTree(lambda x, y: x <= y, Node(4, Node(2, None, None), Node(6, None, None)))
        expected1 = [2, 6, 4]
        self.assertEqual(list(postfix_iterator(tree1)), expected1)
        tree2 = BinarySearchTree(lambda x, y: x <= y, Node(10, Node(5, None, None), Node(15, None, None)))
        expected2 = [5, 15, 10]
        self.assertEqual(list(postfix_iterator(tree2)), expected2)
