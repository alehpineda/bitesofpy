from operator import itemgetter
VOWELS = list('aeiou')


def get_word_max_vowels(text):
   """Get the case insensitive word in text that has most vowels.
      Return a tuple of the matching word and the vowel count, e.g.
      ('object-oriented', 6)"""
   words = text.split()
   max_vowels = {}
   for word in words:
      max_vowels[word] = sum(map(word.lower().count, VOWELS))
   return (max(max_vowels.items(), key=itemgetter(1)))


# Pybites solution

def _count_vowels(word):
    return len([c for c in word if c in VOWELS])


def get_word_max_vowels1(text):
   """Get the case insensitive word in text that has most vowels.
      Return a tuple of the matching word and the vowel count, e.g.
      ('object-oriented', 6)"""

   words = text.lower().split()
   words = [(word, _count_vowels(word)) for word in words]

   return max(words, key=lambda x: x[1])