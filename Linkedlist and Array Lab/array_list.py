import unittest
import numpy as nd
from typing import List
from dataclasses import dataclass
import numpy as np
import self as self
from numpy import ndarray

from lists import *


@dataclass
class LstData:
    array: np.ndarray[int]
    length: int

    def __iter__(self):
        return iter(self.array)

    def insert(self, param, element):
        pass


# empty_list ps: function takes no arguments and returns an empty list
def empty_list() -> LstData:
    return LstData(array=np.array([]), length=0)


# add_to_front ps: function takes a list and an element and returns a list where the new element is first and the
# remaining elements follow it

def add_to_front(arr: np.ndarray[int], element: int) -> LstData:
    new_arr = arr
    new_arr.insert(0, element)
    return LstData(array=new_arr, length=len(new_arr))


# add ps: takes a list, integer, another value and places value at index

def add(arr: np.ndarray[int], index: int, value: int):
    if (index >= 0) and (index <= len(arr)):
        new_arr = arr
        new_arr.insert(index, value)
        return LstData(array=new_arr, length=len(new_arr))
    else:
        raise IndexError("Index out of range")


# length ps: function takes a list and returns the number of elements in the list
def length(arr: np.ndarray[int]) -> int:
    new_arr = LstData(array=arr, length=len(arr))
    return new_arr.length


# get ps: function takes a list and an integer and returns the value at the index pos
def get(arr: np.ndarray[int], index: int) -> int:
    if (index >= 0) and (index <= len(arr)):
        return arr[index]
    else:
        raise IndexError("Index out of range")


# set ps: function takes a list, int index, and a value and replaces element at index pos with
# the given value
def set(arr: np.ndarray[int], index: int, value: int):
    if (index >= 0) and (index <= len(arr)):
        del arr[index]
        new_arr = arr
        new_arr.insert(index, value)
        return LstData(array=new_arr, length=len(new_arr))
    else:
        raise IndexError("Index out of range")


# remove ps: function takes a list and an int index and removes element at index pos
# this function returns a 2-tuple of the removed element and the resulting list

def remove(arr: np.ndarray[int], index: int) -> tuple:
    if (index >= 0) and (index <= len(arr)):
        val = arr[index]
        del arr[index]
        return val, arr
    else:
        raise IndexError("Index out of range")


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
