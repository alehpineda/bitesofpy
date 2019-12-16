from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_
def test_first_ten():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34


def test_raise_valueerror():
    with pytest.raises(ValueError):
        for n in range(-1, -11, -1):
            fib(n)
