def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError
    if fmt.lower() not in ['cm', 'in']:
        raise ValueError
    if fmt.lower() == 'cm':
        convert = value * 2.54
    if fmt.lower() == 'in':
        convert = value / 2.54
    return round(convert, 4)

# Pybites solution

FORMATS = {"cm": 2.54, "in": 0.393_700_787_4}


def convert1(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()

    if fmt not in FORMATS.keys():
        raise ValueError(f"{fmt} is an unsupported format!")

    try:
        return round(value * FORMATS[fmt], 4)
    except TypeError as e:
        raise TypeError(f"{e} must be a numeric!")
