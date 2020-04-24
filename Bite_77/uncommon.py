"""
You want to find people who have as much exposure to different cultures as yourself.

Complete the uncommon_cities helper that takes the cities you have visited (my_cities) and the cities the other person has visited (other_cities) and returns the number of cities that both sequences do NOT have in common.

So given [A B C] and [B C D] it should return 2 because only A and D are different.

You can loop through both sequences but maybe there is a more concise way to do it?
"""


def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(list(set(my_cities) ^ set(other_cities)))
