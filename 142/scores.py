from collections import namedtuple

MIN_SCORE = 4
DICE_VALUES = range(1, 7)

Player = namedtuple("Player", "name scores")


def calculate_score(scores):
    """Based on a list of score ints (dice roll), calculate the
      total score only taking into account >= MIN_SCORE
      (= eyes of the dice roll).

      If one of the scores is not a valid dice roll (1-6)
      raise a ValueError.

      Returns int of the sum of the scores.
    """

    for score in scores:
        if score not in DICE_VALUES:
            raise ValueError("Not a valid dice roll")

    return sum(score for score in scores if score >= MIN_SCORE)


def get_winner(players):
    """Given a list of Player namedtuples return the player
    with the highest score using calculate_score.

    If the length of the scores lists of the players passed in
    don't match up raise a ValueError.

    Returns a Player namedtuple of the winner.
    You can assume there is only one winner.

    For example - input:
      Player(name='player 1', scores=[1, 3, 2, 5])
      Player(name='player 2', scores=[1, 1, 1, 1])
      Player(name='player 3', scores=[4, 5, 1, 2])

    output:
      Player(name='player 3', scores=[4, 5, 1, 2])
  """
    for player in players:
        if len(player.scores) != MIN_SCORE:
            raise ValueError(
                "the length of the scores lists of the players passed in don't match up"
            )

    return max(players, key=lambda player: calculate_score(player.scores))


# Pybites solution


def calculate_score1(scores):
    """Based on a list of score ints (dice roll), calculate the
       total score only taking into account >= MIN_SCORE
       (= eyes of the dice roll).

       If one of the scores is not a valid dice roll (1-6)
       raise a ValueError.

       Returns int of the sum of the scores.
    """
    if not all(i in DICE_VALUES for i in scores):
        raise ValueError("Includes invalid dice roll(s)")

    return sum(i for i in scores if i >= MIN_SCORE)


def get_winner1(players):
    """Given a list of Player namedtuples return the player
       with the highest score using calculate_score.

       If the length of the scores lists of the players passed in
       don't match up raise a ValueError.

       Returns a Player namedtuple of the winner.
       You can assume there is only one winner.

       For example - input:
         Player(name='player 1', scores=[1, 3, 2, 5])
         Player(name='player 2', scores=[1, 1, 1, 1])
         Player(name='player 3', scores=[4, 5, 1, 2])

       output:
         Player(name='player 3', scores=[4, 5, 1, 2])
    """
    score_lengths = {len(player.scores) for player in players}
    if len(score_lengths) > 1:
        raise ValueError("Players with different amount of score")

    return max(players, key=lambda x: calculate_score1(x.scores))
