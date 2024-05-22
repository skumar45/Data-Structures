import unittest
import numpy as nd
from typing import *
from dataclasses import dataclass


# empty_list ps: function takes no arguments and returns an empty list

def empty_list() -> List:
    return list()


# add_to_front ps: function takes a list and an element and returns a list where the new element is
# first and the remaining elements follow it

def add_to_front(l: list[int], element: int):
    l.insert(0, element)
    new_l = l
    return new_l


# add ps: takes a list, integer, another value and places value at index

def add(l: list[int], index: int, value: int):
    if (index > 0) and (index < len(l)):
        l.insert(index, value)
        new_l = l
        return new_l
    else:
        return 'Index Error'


# length ps: function takes a list and returns the number of elements in the list
def length(l: list[int]):
    return len(l)


# get ps: function takes list and integer and return value at index position
def get(l: list[int], index: int):
    if (index > 0) and (index < len(l)):
        return l[index]
    else:
        return 'Index Error'


# set ps: function takes a list, integer, and another value and replaces element at index position in the given value
def set(l: list[int], index: int, value: int):
    if (index > 0) and (index < len(l)):
        del l[index]
        l.insert(index, value)
        return l
    else:
        return 'Index Error'


# remove ps: function takes a list and integer index and removes element at index position
def remove(l: list[int], index: int):
    if (index > 0) and (index < len(l)):
        removed_element = l.pop(index)
        return removed_element, l
    else:
        return 'Index Error'


# Test Cases
class Tests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(empty_list([]), [])

    def test_add_to_front(self):
        self.assertEqual(add_to_front([2, 3, 4], 1), [1, 2, 3, 4])
        self.assertEqual(add_to_front([4, 5, 6], 8), [8, 4, 5, 6])

    def test_add(self):
        self.assertEqual(add([1, 2, 3], 1, 5), [1, 5, 2, 3])
        self.assertEqual(add([3, 6, 8], 2, 9), [3, 6, 9, 8])
        self.assertEqual(add([1, 2, 3], 4, 3), 'Index Error')

    def test_length(self):
        self.assertEqual(length([1, 2, 3, 4]), 4)
        self.assertEqual(length([3, 2, 5]), 3)

    def test_get(self):
        self.assertEqual(get([2, 5, 3], 2), 3)
        self.assertEqual(get([3, 6, 8, 4], 1), 6)
        self.assertEqual(get([9, 0, 3, 8], 5), 'Index Error')

    def test_set(self):
        self.assertEqual(set([9, 4, 8], 1, 3), [9, 3, 8])
        self.assertEqual(set([3, 5], 0, 2), [2, 5])
        self.assertEqual(set([0, 4, 9], 4, 9), 'Index Error')

    def test_remove(self):
        self.assertEqual(remove([8, 2, 9], 1), (2, [8, 9]))
        self.assertEqual(remove([9, 4, 5, 2], 2), (5, [9, 4, 2]))
        self.assertEqual(remove([0, 1], 4), 'Index Error')
