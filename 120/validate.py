from functools import wraps


def int_args(func):
    @wraps(func)
    # complete this decorator
    def wrapper(*args):
        if not all(isinstance(x, int) for x in args):
            raise TypeError
        if any(x < 0 for x in args):
            raise ValueError
        else:
            return func(*args)

    return wrapper
