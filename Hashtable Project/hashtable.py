import numpy as np
from typing import *
from dataclasses import dataclass
import unittest


@dataclass
class Hashtable:
    size: int
    table: np.array


@dataclass
class Node:
    key = int
    value = int
    next: Optional['Node'] = None

    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value


# Make a fresh hash table with given size, containing no elements
def make_hash(size: int) -> Hashtable:
    table = np.array([None] * size)
    return Hashtable(size, table)


# Return the size of the given hash table
def hash_size(ht: Hashtable) -> int:
    return ht.size


# Return the number of elements in the given hash table
def hash_count(ht: Hashtable) -> int:
    return np.count_nonzero(ht.table)


def hash_function(key: str, size: int) -> int:
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % size
    return hash_value


# Does the hash table contain a mapping for the given word?
def has_key(ht: Hashtable, word: str) -> bool:
    index = hash_function(word, ht.size)
    node = ht.table[index]
    while node is not None:
        if node.key == word:
            return True
        node = node.next
    return False


# What line numbers is the given key mapped to in the given hash table?
# this should not contain duplicates, but need not be sorted
def lookup(ht: Hashtable, word: str) -> List[int]:
    index = hash_function(word, ht.size)
    node = ht.table[index]
    while node is not None:
        if node.key == word:
            return node.value
        node = node.next
    return []


# Add a mapping from the given word to the given line number in
# the given hash table
def add(ht: Hashtable, word: str, line: int) -> None:
    index = hash_function(word, ht.size)
    while ht.table[index] is not None:
        index = (index + 1) % ht.size
    ht.table[index] = (word,line)


# What are the words that have mappings in this hash table?
# this list should not contain duplicates, but need not be sorted.
def hash_keys(ht: Hashtable, word: str) -> List[str]:
    keys = []
    seen = set()
    for i in range(ht.size):
        if ht.table[i] is not None and ht.table[i] != 'deleted' and ht.table[i][0] == word:
            if ht.table[i][0] not in seen:
                keys.append(ht.table[i][0])
                seen.add(ht.table[i][0])
    return keys


def resize_table(ht: Hashtable) -> Hashtable:
    new_size = ht.size * 2
    new_table = [None] * new_size
    for item in ht.table:
        if item is not None and item != 'deleted':
            word = item.key
            index = hash_function(word, new_size)
            step = 1
            while new_table[index] is not None:
                index = (index + step) % new_size
                step += 1
            new_table[index] = item
    return Hashtable(new_size, new_table)


# given a list of stop words and a list of strings representing a text,
# return a hash table
def make_concordance(stop_words: List[str], text: List[str]) -> Hashtable:
    size = 128
    ht = Hashtable(size, np.array([None] * size))
    count = 0

    for word in text:
        if word not in stop_words:
            index = hash_function(word, size)
            step = 1
            while ht.table[index] is not None and ht.table[index] != 'deleted':
                if ht.table[index][0] == word:
                    ht.table[index].append(count)
                    break
                index = (index + step) % size
                step += 1
            else:
                ht.table[index] = [word, count]
                count += 1

            load_factor = (count + 1) / size
            if load_factor > 0.5:
                ht = resize_table(ht)
                size = ht.size

    return ht


class TestCases(unittest.TestCase):
    def test_make_hash(self):
        test = Hashtable(size=5, table=list(np.array([None, None, None, None, None])))
        self.assertEqual(make_hash(5), list(test))

    def test_hash_size(self):
        self.assertEqual(hash_size(Hashtable(size=5, table=np.array([None, None, None, None, None]))), 5)
        self.assertEqual(hash_size(Hashtable(size=3, table=np.array([None, None, None]))), 3)

    def test_hash_count(self):
        test = Hashtable(size=5, table=np.array([None, 5, None, None, None]))
        test_2 = Hashtable(size=5, table=list(np.array([3, 4, None, 9, 4])))
        self.assertEqual(hash_count(test), 1)
        self.assertEqual(hash_count(test_2), 4)

    def test_hash_function(self):
        self.assertEqual(hash_function("hello", 10), 2)
        self.assertEqual(hash_function("world", 7), 2)

    def test_has_key(self):
        test = Hashtable(size=3, table=[Node('str', 5)])
        self.assertEqual(has_key(test, 'banana'), False)

    def test_lookup(self):
        test = Hashtable(size=3, table=[Node(key='str', value=5)])
        test_2 = Hashtable(size=5, table=[Node(key='apple', value=10), Node(key='banana', value=15),Node(key='cherry', value=20)])
        self.assertEqual(has_key(test_2, 'apple'), True)
        self.assertEqual(has_key(test, 'banana'), False)

    def test_add(self):
        test = Hashtable(size=5, table=[None, None, None, None, None])
        self.assertEqual(add(test,'apple', 1), None)

    def test_hash_keys(self):
        test = Hashtable(size=5, table=[('apple', 1), ('banana', 2), None, ('apple', 3), None])
        self.assertEqual(hash_keys(test, 'apple'), ['apple'])

    def test_resize_table(self):
        test_table = Hashtable(size=5, table=[Node('apple', 1), Node('banana', 2), None, None, Node('orange', 3)])
        expected_table = Hashtable(size=10, table=[Node('apple', 1), None, None, None, None, None, Node('banana', 2), None, None, Node('orange', 3)])
        self.assertEqual(resize_table(test_table), expected_table)


    def test_make_concordance(self):
        stop_words = ['the', 'and', 'in']
        text = ['apple', 'banana', 'apple']
        expected_table = Hashtable(size=128,
          table=np.array([None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, list(['apple', 0, 2]), None, None, None, None, None,
       None, None, None, None, None, list(['banana', 1]), None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None, None, None, None, None, None, None, None, None, None,
       None, None], dtype=object))
        self.assertEqual(make_concordance(stop_words, text), expected_table)






