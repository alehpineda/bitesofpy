"""
Calculate the dictionary word that would have the most value in Scrabble.

There are 3 tasks to complete for this Bite:

 - First write a function to read in the dictionary.txt file ( = DICTIONARY 
 constant), returning a list of words (note that the words are separated 
 by new lines).

- Second write a function that receives a word and calculates its value. 
Use the scores stored in LETTER_SCORES. Letters that are not in 
LETTER_SCORES should be omitted (= get a 0 score).
With these two pieces in place. 

- Third write a function that takes a list of words and returns the word with the highest value.

Look at the TESTS tab to see what your code needs to pass. Enjoy!
"""

import os
import urllib.request
from tempfile import gettempdir

# PREWORK
TMP = gettempdir()
DICTIONARY = os.path.join(TMP, 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    words = []
    # don't read the whole file into memory when you don't have too
    # files are iterable
    with open(DICTIONARY) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words.append(line)
    return words


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    value = []
    for char in word:
        for val, lists in scrabble_scores:
            if char.lower() in lists.lower().split():
                value.append(val)

    return sum(value)


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    if words == None:
        words = load_words()
    value_list = [calc_word_value(word) for word in words]
    return words[value_list.index(max(value_list))]

# Pybites solution

# START HERE
def load_words1():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
        return [word.strip() for word in f.read().split()]


def calc_word_value1(word):
    """given a word calculate its value using LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value1(words=None):
    """given a list of words return the word with the maximum word value"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)
