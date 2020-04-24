def find_number_pairs(numbers, N=10):
    combos = []
    pair = {}

    for i, num in enumerate(numbers):
        diff = round(N - num, 2)
        if diff in pair:
            combos.append((num, diff))
        else:
            pair[num] = i

    return list(set(_sort_all(combos)))


def _sort_all(ret):
    return sorted([tuple(sorted(n)) for n in ret])


# Pybites solution

from itertools import combinations


def find_number_pairs1(numbers, N=10):
    return [(i, j) for i, j in combinations(numbers, 2) if i + j == N]
