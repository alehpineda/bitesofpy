THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def __mul__(self, other):
        if other == 0:
            raise ValueError()
        elif 0 < other < 4:
            return THUMBS_UP * other
        elif other > 3:
            return f"{THUMBS_UP} ({other}x)"
        elif -4 < other < 0:
            return THUMBS_DOWN * -other
        elif other < -3:
            return f"{THUMBS_DOWN} ({-other}x)"

    def __rmul__(self, other):
        return self.__mul__(other)
