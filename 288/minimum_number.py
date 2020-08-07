from typing import List


def minimum_number(digits: List[int]) -> int:
    return int("".join(map(str, sorted(list(set(digits)))))) if digits else 0
