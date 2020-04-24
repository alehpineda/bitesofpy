from itertools import count


class Animal:
    # class variables shared by all instances
    _zoo = {}
    _seq = count(start=10001, step=1)

    def __init__(self, name):
        self.name = name.title()
        self._id = next(self._seq)
        self._zoo.update({self._id: self.name})

    def __str__(self):
        return f"{self._id}. {self.name}"

    @classmethod
    def zoo(cls):
        # instead of self, call cls
        return "\n".join([f"{_id}. {name}" for _id, name in cls._zoo.items()])


# Pybites solution


class Animal1:
    _seq = count(10001)
    _zoo = []

    def __init__(self, name):
        self.id = next(self._seq)
        self.name = name.title()
        self._zoo.append(self)

    def __str__(self):
        return f"{self.id}. {self.name}"

    @classmethod
    def zoo(cls):
        return "\n".join([str(animal) for animal in cls._zoo])
