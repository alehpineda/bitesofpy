import unicodedata


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    # decomposition return base char + added symbol or ''
    # you could also use unicodedata.normalize
    return {char for char in text.lower() if unicodedata.decomposition(char)}
