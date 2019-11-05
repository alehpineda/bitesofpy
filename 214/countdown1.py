def countdown():
    """Write a generator that counts from 100 to 1"""
    return (x for x in reversed(range(1, 101)))


# second solution
def countdown1():
    """Write a generator that counts from 100 to 1"""
    return (x for x in range(100, 0, -1))


# pybites solution
def countdown2():
    """Write a generator that counts from 100 to 1"""
    for i in reversed(range(1, 101)):
        yield i