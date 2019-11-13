from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(UPPER_SLICE)
        # do some stuff before the original
        # function gets called        
        func(*args, **kwargs)
        # do some stuff after function call and
        # return the result        
        print(LOWER_SLICE)
    # return wrapper as a decorated function        
    return wrapped
