import re
import typing

from docstring import sum_numbers


def test_sum_numbers():
    doc = f'\n{sum_numbers.__doc__.strip()}'

    # for some lines allow variable content after colon
    for line in (r'Sums numbers',
                 r'    :param numbers: \S.*?\n',
                 r'    :type numbers: list',
                 r'    :raises TypeError: \S.*?\n',
                 r'    :return: \S.*?\n',
                 r'    :rtype: int'):
        # newline to test proper indenting
        assert re.search(rf'\n{line}', doc)


def test_sum_numbers_annotatios():
    res = sum_numbers.__annotations__
    assert res.get('numbers') == typing.List[int]
    assert res.get('return') == int
