import pytest
from pandigital import is_pandigital


# Decorator
@pytest.mark.parametrize("values, expected", [
    (98140723568910, True),
    (90864523148909, False)
])
def test_is_pandigital(values, expected):
    assert is_pandigital(values) == expected


# Decorator
@pytest.mark.parametrize("values", [
    (98140723568910),
    ("90864523148909"),
])
def test_input_not_int(values):
    assert isinstance(values, int) == True
