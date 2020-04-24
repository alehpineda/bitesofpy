THUMBS_UP, THUMBS_DOWN = "👍", "👎"


class Thumbs:
    def __mul__(self, count):
        emoji = THUMBS_UP if count > 0 else THUMBS_DOWN
        count = abs(count)

        if count == 0:
            raise ValueError("Specify a number")

        return f"{emoji} ({count}x)" if count > 3 else emoji * count

    def __rmul__(self, count):
        return self.__mul__(count)
