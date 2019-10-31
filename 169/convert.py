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
