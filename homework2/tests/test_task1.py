from Task01 import *


def test_longest_diverse_word():
    assert get_longest_diverse_words("data.txt") == [
        "unmißverständliche",
        "Bevölkerungsabschub",
        "Kollektivschuldiger",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "Selbstverständlich",
        "Fingerabdrucks",
        "Friedensabstimmung",
        "außenpolitisch",
        "Seinsverdichtungen",
    ]


def test_rarest_char():
    assert get_rarest_char("data.txt") == "›"


def test_count_punctuation_chars():
    assert count_punctuation_chars("data.txt") == 5475


def test_count_non_ascii_char():
    assert count_non_ascii_chars("data.txt") == 2972


def test_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char("data.txt") == "ä"
