def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    if numbers is None:
        return sum(list(range(101)))
    return sum(numbers)
