"""
In this bite you learn to catch/raise exceptions.

Write a simple division function meeting the following requirements:

when denominator is 0 catch the corresponding exception and return 0.
when numerator or denominator are not of the right type reraise the 
corresponding exception.
if the result of the division (after surviving the exceptions) is 
negative, raise a ValueError
As always see the tests written in pytest to see what your code need 
to pass. Have fun!
"""

def positive_divide(numerator, denominator):
    try:
        div = numerator/denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
    else:
        if div < 0:
            raise ValueError
        return div

# pybites solution
def positive_divide1(numerator, denominator):
    try:
        result = numerator/denominator
        if result < 0:
            raise ValueError('Cannot be negative')
        else:
            return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
