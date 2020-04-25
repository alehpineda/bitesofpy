import inspect


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [
        key
        for key, _ in inspect.getmembers(mod, inspect.isclass)
        if key[0].isupper()
    ]
