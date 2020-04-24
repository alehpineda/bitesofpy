from collections import Counter


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1, word2 = _clean_word(word1), _clean_word(word2)
    return set(word1) == set(word2) and len(word1) == len(word2)


def _clean_word(word):
    return word.strip().replace(" ", "").lower()


def is_anagram1(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1, word2 = _clean_word(word1), _clean_word(word2)
    return Counter(word1) == Counter(word2)
