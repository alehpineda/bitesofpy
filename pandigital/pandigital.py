"""
A pandigital number will contain all digits (0-9) at least
once.
Write a function that returns a boolean indicating if the
integer is pandigital or not.

Examples

is_pandigital(98140723568910) -> TRUE
is_pandigital(90864523148909) -> FALSE (the # 7 is missing)
"""


def is_pandigital(num):
    return len(set(str(num))) == 10


print(is_pandigital(98140723568910))
print(is_pandigital(90864523148909))
