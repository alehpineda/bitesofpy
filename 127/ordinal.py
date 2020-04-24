def get_ordinal_suffix(number):
    """Receives a number int and returns it appended with its ordinal suffix,
      so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.
      
      Rules:
      https://en.wikipedia.org/wiki/Ordinal_indicator#English
      - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
      - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
      - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
      - As an exception to the above rules, all the "teen" numbers ending with
        11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
        pronounced one hundred [and] twelfth)
      - th is used for all other numbers (e.g. 9th, pronounced ninth).
    """
    number = str(number)

    # create a dictionary with keys 1,2,3 and values st, nd, rd
    f_123 = dict(zip("1 2 3".split(), "st nd rd".split()))

    # save the suffix
    # use get from dict to check if the number ends with 1,2, or 3 if not
    # save 'th'
    suffix = f_123.get(number[-1]) or "th"

    # teen numbers
    # if the number is 10 or more and the second last is 1
    if len(number) > 1 and number[-2] == "1":
        suffix = "th"

    # return f-string with number and suffix
    return f"{number}{suffix}"
