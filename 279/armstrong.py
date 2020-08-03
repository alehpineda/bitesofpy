def is_armstrong(n: int) -> bool:
    return sum([pow(int(x), len(str(n))) for x in str(n)]) == n
