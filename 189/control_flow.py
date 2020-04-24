IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names):
    count = 0
    for name in names:
        if name.startswith(IGNORE_CHAR) or any(char.isdigit() for char in name):
            continue
        elif name.startswith(QUIT_CHAR) or count >= MAX_NAMES:
            break
        count += 1
        yield name
