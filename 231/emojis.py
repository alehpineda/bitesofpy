import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r"[^\w\s,]")


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    emojis = re.findall(IS_EMOJI, text)
    _start_at = -1
    emoji_index = []

    for emoji in emojis:
        _start_at += 1
        emoji_index.append(text.index(emoji, _start_at))

    return emoji_index


# Pybites solution


def get_emoji_indices1(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    return [i for i, char in enumerate(text) if IS_EMOJI.match(char)]
