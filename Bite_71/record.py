class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self._score = None


    def __call__(self, new_score):
        if not self._score:
            self._score = new_score
        self._score = max(self._score, new_score)
        return self._score

    # Print the score value
    def __str__(self):
        return f'Top Score: {self._score}'


# Pybites solution
class RecordScore1():
    """Class to track a game's maximum score"""

    def __init__(self):
        self._score = float('-inf')

    def __call__(self, num):
        self._score = max(self._score, num)
        return self._score