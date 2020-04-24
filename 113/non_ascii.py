def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    words = text.split()
    return [word for word in words if _is_ascii(word)]


# Pybites solution
def _is_ascii(word):
    """Helper to determine if a word consists of only ascii chars
    Returns False if the word consists of only ascii chars
    """
    return not all(ord(char) < 128 for char in word)


def extract_non_ascii_words1(text):
    """Filter a text returning a list of non-ascii words"""
    return [word for word in text.split() if _is_ascii(word)]
