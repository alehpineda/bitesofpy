from fizzbuzz1 import fizzbuzz
import pytest
# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize("values, expected", [
    (1, 1),
    (2, 2),
    (3, 'Fizz'),
    (4, 4),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, 7),
    (8, 8),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, 11),
    (12, 'Fizz'),
    (13, 13),
    (14, 14),
    (15, 'Fizz Buzz'),
])
def test_valid_input(values, expected):
    assert fizzbuzz(values) == expected
