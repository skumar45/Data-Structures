#
import os
import string
from typing import List

import numpy as np

from hashtable import Hashtable, make_hash, hash_count, has_key, lookup, add
import unittest


def remove_punctuation(line: str) -> str:
    line = line.replace("'", "")
    line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    return line


def build_stop_words_table(stop_words_file: str) -> Hashtable:
    stop_words = make_hash(128)
    with open(stop_words_file, 'r') as file:
        for line in file:
            word = line.strip()
            add(stop_words, word, -1)  # Use a default value for line number
    return stop_words


def build_word_concordance(input_file: str, stop_words: Hashtable) -> Hashtable:
    word_concordance = make_hash(128)
    line_number = 1
    with open(input_file, 'r') as file:
        for line in file:
            line = remove_punctuation(line)
            tokens = line.split()
            for token in tokens:
                if token.isalpha() and not has_key(stop_words, token):
                    if has_key(word_concordance, token):
                        line_numbers = lookup(word_concordance, token)
                        if line_number not in line_numbers:
                            add(word_concordance, token, line_number)
                    else:
                        add(word_concordance, token, line_number)
            line_number += 1
    return word_concordance


def generate_concordance_file(word_concordance: Hashtable, output_file: str) -> None:
    with open(output_file, 'w') as file:
        for index in range(word_concordance.size):
            node = word_concordance.table[index]
            if node is not None:
                word = node.key
                line_numbers = node.value
                line_numbers_str = ' '.join(map(str, line_numbers))
                file.write(f"{word}: {line_numbers_str}\n")


class ConcordanceTestCase(unittest.TestCase):

    def test_remove_punctuation(self):
        line = "Hello, World!."
        expected_result = "Hello  world "
        self.assertEqual(remove_punctuation(line), expected_result)

    def test_build_stop_words_table(self):
        stop_words_file = "stop_words.txt"
        expected_result = Hashtable(size=128,
                                    table=np.array([None, None, None, None, None, None, None, None, None, None, None,
                                                    ('do', -1), None, ('about', -1), None, None, None, None, None,
                                                    None, None, None, None, None, None, None, None, None, None, None,
                                                    ('this', -1), None, None, None, None, None, None, ('in', -1), None,
                                                    None, None, None, ('is', -1), ('it', -1), None, None, None, None,
                                                    None, None, None, None, None, None, None, None, None, None, None,
                                                    None, None, None, None, None, None, None, None, ('be', -1), None,
                                                    None, None, None, None, None, None, None, None, None, None, None,
                                                    ('can', -1), None, None, None, None, None, None, ('by', -1),
                                                    ('of', -1), None, None, None, None, None, None, ('on', -1), None,
                                                    ('a', -1), None, None, None, None, None, None, None, ('i', -1),
                                                    ('was', -1), None, None, None, None, None, None, ('the', -1), None,
                                                    None, None, None, None, None, None, None, None, ('to', -1), None,
                                                    None, None, None], dtype=object))
        self.assertEqual(build_stop_words_table(stop_words_file), expected_result)

    def test_build_word_concordance(self):
        stop_words = Hashtable(size=128,
                               table=[None, None, ('a', -1), None, ...])
        input_file = "input_file.txt"
        word_concordance = build_word_concordance(input_file, stop_words)

        self.assertEqual(lookup(word_concordance, 'apple'), [1, 2])
        self.assertEqual(lookup(word_concordance, 'banana'), [1])
        self.assertEqual(lookup(word_concordance, 'cherry'), [2])

    def test_generate_concordance_file(self):
        word_concordance = Hashtable(size=10, table=[
            ('apple', [1, 3, 5]),
            ('banana', [2, 4]),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ])
        output_file = 'concordance.txt'
        generate_concordance_file(word_concordance, output_file)

        with open(output_file, 'r') as file:
            content = file.read()
            expected_content = "apple: 1 3 5\nbanana: 2 4\n"
            self.assertEqual(content, expected_content)
