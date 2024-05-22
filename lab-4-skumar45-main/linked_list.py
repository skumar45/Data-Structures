import unittest
from typing import *

import numpy as nd
from typing import *
from dataclasses import dataclass

# IntList Data Definition
AnyList: TypeAlias = Union['Pair', None]


@dataclass(frozen=True)
class Pair:
    first: int
    rest: AnyList


@dataclass(frozen=True)
class Iterator:
    llist: AnyList


# function takes a linked list and returns an iterator object
def object_iterator(ll: AnyList) -> Iterator:
    return Iterator(ll)


# function takes iterator object and returns True if there is another value to return from the iterated list
def has_next(i: Iterator) -> bool:
    if i.llist.first is None and i.llist.rest is None:
        return False
    else:
        return True


# function takes iterator object and returns the next value in the iteration sequence: if there are no remaining values,
# a stop-iteration exception should be raised.
def get_next(i: Iterator) -> any:
    if i.llist.first is not None:
        return i.llist.first
    while i.llist.first is None and i.llist.rest is not None:
        val = i.llist.rest.first
        i.llist.rest.rest.first = i.llist.rest.first
        return val
    else:
        raise StopIteration("No remaining values in the sequence")


# function takes a linked list as an argument and yields each value within the list
def yield_iterator(ll: AnyList) -> Iterator:
    if ll is None:
        return
    yield ll.first
    yield from yield_iterator(ll.rest)


# empty_list ps: function takes no arguments and returns an empty list
def empty_list():
    return None


# add_to_front ps: function takes a list and an element and returns a list where the new element is
# first and the remaining elements follow it
def add_to_front(il: AnyList, element: int) -> AnyList:
    return Pair(element, il)


# add ps: takes a list, integer, another value and places value at index

def add(il: AnyList, index: int, value: int):
    if index < 0:
        raise IndexError("Index is less than 0")
    else:
        if il is None and index > 0:
            raise IndexError
        else:
            if index == 0:
                return Pair(value, il)
            else:
                return Pair(il.first, add(il.rest, index - 1, value))


# length ps: function takes a list and returns the number of elements in the list
def length(il: AnyList):
    if il is None:
        return 0
    else:
        return 1 + length(il.rest)


# get ps: function takes list and integer and return value at index position
def get(head: Pair, index: int):
    current_pair = head
    current_index = 0
    while current_pair is not None:
        if current_index == index:
            return current_pair.first
        current_pair = current_pair.rest
        current_index += 1
    else:
        raise IndexError("Index out of range")


# set ps: function takes a list, integer, and another value and replaces element at index position in the given value
def set(head: Pair, index: int, value: float):
    if index > length(head) or index < 0:
        raise IndexError("Index out of range")
    else:
        if index == 0:
            return Pair(value, head.rest)
        else:
            return Pair(head.first, set(head.rest, index - 1, value))


# remove ps: function takes a list and integer index and removes element at index position
def remove(il: AnyList, index: int):
    if index < 0:
        raise IndexError("Index is less than 0")
    if index == 0:
        return (il.first, il.rest)
    current_index = 0
    current_item = il
    while current_item is not None:
        if current_index + 1 == index:
            element = current_item.rest.first
            il.rest = current_item.rest.rest
            return (element, il)
        current_index += 1
        current_item = current_item.rest


# Test Cases

class Tests(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add_to_front(self):
        self.assertEqual(add_to_front((Pair(4, Pair(9, None))), 3), (Pair(3, Pair(4, Pair(9, None)))))

    def test_add(self):
        self.assertEqual(add((Pair(3, Pair(9, None))), 1, 4), (Pair(3, Pair(4, Pair(9, None)))))

    def test_length(self):
        self.assertEqual(length(Pair(3, Pair(7, Pair(5, None)))), 3)
        self.assertEqual(length(Pair(4, Pair(87, None))), 2)

    def test_get(self):
        self.assertEqual(get((Pair(8, Pair(3, None))), 1), 3)
        self.assertEqual(get(Pair(3, Pair(7, Pair(5, None))), 0), 3)

    def test_set(self):
        list_1 = Pair(8, Pair(3, None))
        list_test = Pair(8, Pair(5, None))
        list_2 = Pair(4, Pair(0, Pair(2, None)))
        list_test_2 = Pair(8, Pair(0, (Pair(2, None))))
        self.assertEqual(set(list_1, 1, 5), list_test)
        self.assertEqual(set(list_2, 0, 8), list_test_2)

    def test_remove(self):
        list_1 = Pair(4, Pair(3, Pair(2, None)))
