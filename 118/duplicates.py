from collections import Counter


def get_duplicate_indices(words):
    """Given a list of words, loop through the words and check for each
      word if it occurs more than once.
      If so return the index of its first ocurrence.
      For example in the following list 'is' and 'it'
      occurr more than once, and they are at indices 0 and 1 so you would
      return [0, 1]:
      ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
      Make sure the returning list is unique and sorted in ascending order.
      count, list comprehension, set
   """
    return sorted(
        [words.index(word) for word, count in Counter(words).most_common() if count > 1]
    )


# Pybites solution


def get_duplicate_indices1(words):
    """Given a list of words, loop through the words and check for each
       word if it occurs more than once.
       If so return the index of its first ocurrence.
       For example in the following list 'is' and 'it'
       occurr more than once, and they are at indices 0 and 1 so you would
       return [0, 1]:
       ['is', 'it', 'true', 'or', 'is', 'it', 'not?'] => [0, 1]
       Make sure the returning list is unique and sorted in ascending order."""
    duplicate_words = {word for word in words if words.count(word) > 1}
    return sorted([words.index(word) for word in duplicate_words])
