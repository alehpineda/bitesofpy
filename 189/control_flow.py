IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    _names = []
    for name in names:
        if name.lower()[0] == IGNORE_CHAR:
            pass
        elif any(char.isdigit() for char in name):
            pass
        elif name.lower()[0] == QUIT_CHAR:
            break
        else:
            _names.append(name)
            if len(_names) == 5:
                break
    return _names
