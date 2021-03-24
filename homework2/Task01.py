"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
import unicodedata
from collections import defaultdict
from typing import List


def tokenize(text):
    current_word = ""
    char = " "
    while char:
        char = text.read(1)
        if not char:
            break
        if unicodedata.category(char).startswith("P"):
            if current_word:
                yield "word", current_word
                current_word = ""
            yield "punctuation", char
            continue
        if char in string.whitespace:
            if current_word:
                yield "word", current_word
                current_word = ""
            yield "whitespace", char
            continue
        current_word += char
    if current_word:
        yield "word", current_word


def read_by_symbol(text):
    char = " "
    while char:
        char = text.read(1)
        yield char


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, encoding="unicode-escape") as f:
        d_words = defaultdict(int)
        for type_token, token in tokenize(f):
            if type_token == "word":
                d_words[token] = len(set(token))
        l_words = sorted(d_words.items(), key=lambda l: l[1], reverse=True)[:10]
        l_words = [i[0] for i in l_words]
        return l_words


def get_rarest_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as f:
        dic_char = defaultdict(int)
        for char in read_by_symbol(f):
            dic_char[char] += 1
        print("slovar", dic_char)
        rar_char = sorted(dic_char.items(), key=lambda k: k[1])[0][0]
        return rar_char


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        count = 0
        for type_token, token in tokenize(f):
            if type_token == "punctuation":
                count += 1
        return count


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="unicode-escape") as f:
        count = 0
        for char in read_by_symbol(f):
            if not char.isascii():
                count += 1
        return count


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, encoding="unicode-escape") as f:
        m_com = defaultdict(int)
        for char in read_by_symbol(f):
            if not char.isascii():
                m_com[char] += 1
        return sorted(m_com.items(), key=lambda v: v[1])[-1][0]


# done
