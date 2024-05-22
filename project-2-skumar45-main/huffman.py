import numpy as np
from typing import *
from dataclasses import dataclass
import unittest


# put all of your functions and test cases in this file, yay!


# make a function called cnt_freq(str) that accepts a string and returns a numpy array that
# indicates number of occurrences of each character in the string

def cnt_freq(s: str) -> np.ndarray[int]:
    array = np.full(256, 0, np.int32)
    for char in s:
        code = ord(char)
        if code <= 255:
            array[code] += 1
    return array


# Data Definition of HTree is a binary tree of HNode and HLeaf.

HTree: TypeAlias = Union['HNode', 'HLeaf']


# HNode has an occurrence count, and a left and a right

@dataclass(frozen=True)
class HNode:
    occurrence: int
    left: HTree
    right: HTree


# HLEaf has one character and an occurrence count
@dataclass(frozen=True)
class HLeaf:
    char: str
    occurrence: int


# function accepts two HTrees and returns true if occurrence count of first is less than or equal to occurrence count
# of second
def tree_lt(a: HTree, b: HTree) -> bool:
    if a.occurrence <= b.occurrence:
        return True
    else:
        return False


# HTList data definition: represents a linked list of HTrees
HTList: TypeAlias = Union['HTNode', 'None']


@dataclass
class HTNode:
    first: HTree
    rest: HTList


# function accepts array of character counts, and returns an HTList containing 256 HTLeaf's, one for each ASCII code

def base_tree_list(counts: np.ndarray[int]) -> HTList:
    ht_list = None
    for i, count in enumerate(counts):
        code = chr(i)
        ht_leaf = HLeaf(code, count)
        if ht_list is None:
            ht_list = HTNode(ht_leaf, None)
        else:
            ht_list = HTNode(ht_leaf, ht_list)
    return ht_list


# function takes HTList of HTrees that is sorted in order specified by tree_lt, and another HTree, and inserts it in
# the correct location so the HTList is still sorted
def tree_list_insert(lst: HTList, t: HTree) -> HTList:
    if lst is None:
        return HTNode(t, None)
    elif tree_lt(t, lst.first):
        return HTNode(t, lst)
    else:
        return HTNode(lst.first, tree_list_insert(lst.rest, t))


# function accepts unsorted list and constructs a sorted list by inserting nodes from unsorted list into an initially
# empty sorted list

def initial_tree_sort(lst: HTList) -> HTList:
    sorted_list: HTList = None
    while lst is not None:
        sorted_list = tree_list_insert(sorted_list, lst.first)
        lst = lst.rest
    return sorted_list


# function accepts a sorted HTList of length 2 or more, and forms a new list by joining first and second node together
# into a new HNode and inserting the new HNode into the list containing the remaining elements.
def coalesce_once(hlist: HTList) -> HTList:
    assert hlist is not None and hlist.rest is not None, "HTList must have at least two elements"
    left = hlist.first
    right = hlist.rest.first
    new_occurrence = left.occurrence + right.occurrence
    new_node = HNode(new_occurrence, left, right)
    return HTNode(new_node, hlist.rest.rest)


# function accepts a sorted HTList of length one or more and calls coalesce_once repeatedly until the list contains only
# a single HTree, then returns that one HTree

def coalesce_all(hlist: HTList) -> HTree:
    while hlist.rest is not None:
        hlist = coalesce_once(hlist)
    return hlist.first


# function makes an encoder array from a Huffman decoding tree and returns a list of 256 strings, where each string
# represents the path taken to get from the root of the decoding tree to a leaf node containing a character
def build_encoder_array(tree: HTree) -> List[str]:
    encoder_array = [''] * 256
    build_encoder_array_helper(tree, '', encoder_array)
    return encoder_array


def build_encoder_array_helper(tree: HTree, path: str, encoder_array: List[str]):
    if isinstance(tree, HLeaf):
        encoder_array[ord(tree.char)] = path
    elif isinstance(tree, HNode):
        build_encoder_array_helper(tree.left, path + '0', encoder_array)
        build_encoder_array_helper(tree.right, path + '1', encoder_array)


# ps: function accepts a string and an encoder array and constructs the string formed by appending the encodings of each
# of the chars in the string
def encode_string_one(string: str, encoder_array: List[str]) -> str:
    encoded_string = " "
    for char in string:
        code = ord(char)
        if code < len(encoder_array):
            encoded_string += encoder_array[code]
    return encoded_string


# ps: function accepts a string of ones and zeros and converts it to a new string that is 1/8 as long
def bits_to_chars(bits: str) -> str:
    bits = bits.ljust((len(bits) + 7) // 8 * 8, '0')
    output = ""
    for i in range(0, len(bits), 8):
        binary = bits[i:i + 8]
        decimal = int(binary, 2)
        character = chr(decimal)
        output += character
    return output


# ps: function accepts a source and target file path, reads input file, constructs tree, maps this to an
# encoding tree, uses the encoding tree to encode the contents of the input file, converts it to the char
# representation, then writes this to the new file (replacing any file that was existing at this path).
def huffman_code_file(source_path: str, target_path: str):
    # Read the input file
    with open(source_path, 'r') as file:
        text = file.read()

    # Construct the Huffman tree
    tree = HTree(text)

    # Build the encoder array
    encoder_array = build_encoder_array(tree)

    # Encode the input string
    encoded_string = encode_string_one(text, encoder_array)

    # Convert the encoded string to characters
    char_representation = bits_to_chars(encoded_string)

    with open(target_path, 'w') as file:
        file.write(char_representation)


class TestCases(unittest.TestCase):
    def test_cnt_freq(self):
        ta = np.array(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 8, 16, 0, 2, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0])
        self.assertEqual(cnt_freq('hello')[108], 2)
        self.assertEqual(list(cnt_freq('ddddddddddddddddccccccccbbbbaaff'))[96:104], [0, 2, 4, 8, 16, 0, 2, 0])

    def test_tree_lt(self):
        tree_ex1: HTree = HNode(5, HNode(None, None, None), HLeaf('name', 4))
        tree_ex2: HTree = HNode(6, HNode(None, None, None), HLeaf('name', 7))
        self.assertEqual(tree_lt(tree_ex1, tree_ex2), True)

    def test_base_tree_list(self):
        cnt_freq_ex1 = np.array([4])
        htlist_ex1: HTList = HTNode(HLeaf('\x00', 4), None)
        cnt_freq_ex2 = np.array([6, 8])
        htlist_ex2: HTList = HTNode(HLeaf('\x01', 8), HTNode(HLeaf('\x00', 6), None))
        self.assertEqual(base_tree_list(cnt_freq_ex1), htlist_ex1)
        self.assertEqual(base_tree_list(cnt_freq_ex2), htlist_ex2)

    def test_tree_list_insert(self):
        ht_tree_ex1: HTList = HTNode(HLeaf('\x00', 6), HTNode(HLeaf('\x01', 8), None))
        h_leaf: HTree = HLeaf('\x02', 7)
        h_tree = HNode(7, h_leaf, None)
        expected: HTList = HTNode(HLeaf('\x00', 6),
                                  HTNode(HNode(7, HLeaf('\x02', 7), None), HTNode(HLeaf('\x01', 8), None)))
        self.assertEqual(tree_list_insert(ht_tree_ex1, h_tree), expected)

    def test_initial_tree_sort(self):
        unsorted_list: HTList = HTNode(HLeaf('b', 5),
                                       HTNode(HLeaf('a', 3), HTNode(HLeaf('c', 7), HTNode(HLeaf('d', 2), None))))
        expected_list: HTList = HTNode(HLeaf('d', 2),
                                       HTNode(HLeaf('a', 3), HTNode(HLeaf('b', 5), HTNode(HLeaf('c', 7), None))))
        self.assertEqual(initial_tree_sort(unsorted_list), expected_list)

    def test_coalesce_once(self):
        test: HTList = HTNode(HLeaf('a', 5),HTNode(HLeaf('b', 3), HTNode(HLeaf('c', 2), None)))
        expected: HTList = HTNode(HNode(8,HLeaf('a',5),HLeaf('b',3)), HTNode(HLeaf('c', 2), rest=None))
        self.assertEqual(coalesce_once(test), expected)

    def test_coalesce_all(self):
        test: HTList = HTNode(HNode(8, HLeaf('a',5), HLeaf('b', 3)), HTNode(HLeaf('c', 2),None))
        expected_tree: HTree = HNode(10,HNode(8,HLeaf('a', 5),HLeaf('b', 3)), HLeaf('c', 2))
        self.assertEqual(coalesce_all(test), expected_tree)

    def test_build_encoder_array(self):
        test: HTree = HNode(10,HNode(8,HLeaf('a', 5),HLeaf('b', 3)),HLeaf('c', 2))

        expected = ['',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '00',
                    '01',
                    '1',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '',
                    '']
        self.assertEqual(build_encoder_array(test), expected)

    def test_encode_string_one(self):
        encoder_array = [
            '65',  # ASCII code A
            '66',  # ASCII code B
            '67',  # ASCII code C
            '68',  # ASCII code D
            ...  # Rest of the encoder array
        ]
        input_string = "ABCD"
        expected = "10110110"
        self.assertEqual(encode_string_one(input_string, encoder_array), expected)

    def test_bits_to_chars(self):
        input_bits = '0100100001100101011011000110110001101111'
        expected = 'Hello'
        self.assertEqual(bits_to_chars(input_bits), expected)
