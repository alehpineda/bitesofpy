from string import ascii_uppercase
from itertools import cycle, chain


def sequence_generator():
    return cycle(
        chain.from_iterable(
            zip(range(1, len(ascii_uppercase) + 1), ascii_uppercase)
        )
    )


def sequence_generator_2():
    return chain.from_iterable(cycle(enumerate(ascii_uppercase, 1)))
