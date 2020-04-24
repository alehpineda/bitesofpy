def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    word = sorted([word for word in words if word[0].isalpha()], key=str.lower)
    number = sorted(
        [number for number in words if number[0].isdigit()], key=str.lower
    )
    return word + number


# Pybites solution


def sort_words_case_insensitively1(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # this works because: >>> sorted([True, False])
    # [False, True]
    return sorted(words, key=lambda x: (x[0].isdigit(), str(x).lower()))
