import pytest

from numbers_to_dec import list_to_decimal

# [0, 4, 2, 8] => 428
# [1, 2] => 12
# [3] => 3
# [6, 2, True] => raises TypeError
# [-3, 12] => raises ValueError
# [3.6, 4, 1] => raises TypeError
# ['4', 5, 3, 1] => raises TypeError

# Decorator
@pytest.mark.parametrize(
    "values, expected",
    [
        ([0, 4, 2, 8], 428),
        ([1, 2], 12),
        ([3], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 1234567890),
    ],
)
def test_valid_input(values, expected):
    # assert all(isinstance(x, int) for x in values)==True
    # assert isinstance(list_to_decimal(values), int) == True
    assert list_to_decimal(values) == expected


# Decorator
@pytest.mark.parametrize(
    "values",
    [
        ([0, -4, 2, 8]),
        ([10, 4, 2, 8]),
        ([1, -2]),
        ([-10, -2]),
        ([10, 12]),
        ([-3]),
        ([1, 4, 2, 80]),
        ([11]),
    ],
)
def test_raise_value(values):
    with pytest.raises(ValueError):
        list_to_decimal(values)


# Decorator
@pytest.mark.parametrize(
    "values",
    [
        ([0, 4.2, 2, 8]),
        ([1, 2, True]),
        (["10", 2]),
        ([False, 1, 2]),
        (["hello"]),
        (["hello", True]),
    ],
)
def test_raise_type(values):
    with pytest.raises(TypeError):
        list_to_decimal(values)
