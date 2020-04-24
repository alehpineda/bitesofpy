from difflib import get_close_matches, SequenceMatcher
import os
from urllib.request import urlretrieve
from tempfile import gettempdir

TMP = gettempdir()
DICTIONARY = os.path.join(TMP, "dictionary.txt")
if not os.path.isfile(DICTIONARY):
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/dictionary.txt",
        DICTIONARY,
    )


def load_words():
    "return dict of words in DICTIONARY"
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    # you code
    return get_close_matches(misspelled_word.lower(), words, n=1)[0]


def suggest_word1(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()

    # you code
    return max(
        words,
        key=lambda word: SequenceMatcher(None, misspelled_word, word).ratio(),
    )
