from random import choice

COLORS = "red blue green yellow brown purple".split()


class EggCreator:
    """Iterator that counts upward eggs."""

    def __init__(self, limit):
        self.limit = limit
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num > self.limit:
            raise StopIteration("Limit exceeded")
        else:
            return f"{choice(COLORS)} egg"
