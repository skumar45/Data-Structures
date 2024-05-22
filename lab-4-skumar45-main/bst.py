import numpy as np
from typing import *
from dataclasses import dataclass
from typing import Any, Callable
import unittest


@dataclass
class BinarySearchTree:
    comparator: Callable[[Any, Any], bool]
    content: 'BSTree'


BSTree: TypeAlias = Union[None, 'Node']


@dataclass(frozen=True)
class Node:
    c: any
    l: BSTree
    r: BSTree


# given a BSTree, returns an iterator of the elements in prefix order wherein, for a given node, the node is visited
# before its children
def prefix_iterator(tree: BinarySearchTree) -> Iterator:
    if tree.content is None:
        return
    yield tree.content.c

    if tree.content.l:
        yield from prefix_iterator(BinarySearchTree(tree.comparator, tree.content.l))

    if tree.content.r:
        yield from prefix_iterator(BinarySearchTree(tree.comparator, tree.content.r))


# given a BSTree, returns an iterator of the elements in infix order wherein, for a given node, the node is visited
# after its left child but before its right child
def infix_iterator(tree: BinarySearchTree) -> Iterator:
    if tree.content is None:
        return
    if tree.content.l:
        yield from infix_iterator(BinarySearchTree(tree.comparator, tree.content.l))

    yield tree.content.c

    if tree.content.r:
        yield from infix_iterator(BinarySearchTree(tree.comparator, tree.content.r))


# given a BSTree, returns an iterator of the elements in postfix order werhein, for a given node, the node is
# visited before its children
def postfix_iterator(tree: BinarySearchTree) -> Iterator[any]:
    if tree.content is None:
        return

    if tree.content.l:
        yield from postfix_iterator(BinarySearchTree(tree.comparator, tree.content.l))

    if tree.content.r:
        yield from postfix_iterator(BinarySearchTree(tree.comparator, tree.content.r))

    yield tree.content.c


# determines if one value comes before another
def comes_before(any1: any, any2: any) -> bool:
    return any1 < any2


# function returns True if the given BinarySearchTree is empty and false otherwise
def is_empty(b: BSTree) -> bool:
    if b == Node(None, None, None):
        return True
    else:
        return False


# function takes a BStree and a value, then adds the value to the tree, then returns tree
def insert(b: BSTree, c: int) -> BSTree:
    if b is None:
        return Node(c, None, None)
    elif comes_before(c, b.c):
        return Node(b.c, insert(b.l, c), b.r)
    else:
        return Node(b.c, b.l, insert(b.r, c))


# function takes BStree and a value, then returns true if value is stored in true and false otherwise,
def lookup(b: BSTree, c: int) -> bool:
    if b is None:
        return False
    elif c == b.c:
        return True
    elif comes_before(c, b.c):
        return lookup(b.l, c)
    else:
        return lookup(b.r, c)


def find_min(bst: BSTree) -> Any:
    if bst.l is None:
        return bst.c
    return find_min(bst.l)


# function takes BSTree and a value, then deletes the value from the tree, returns tree
def delete(b: BSTree, c: int) -> BSTree:
    if b is None:
        raise ValueError
    elif comes_before(c, b.c):
        return Node(b.c, delete(b.l, c), b.r)
    elif comes_before(b.c, c):
        return Node(b.c, b.l, delete(b.r, c))
    else:
        if b.l is None:
            return b.r
        elif b.r is None:
            return b.l
        else:
            min = find_min(b.r)
            return Node(min, b.l, delete(b.r, min))
