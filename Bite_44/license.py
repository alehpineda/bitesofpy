"""
Write a function called gen_key that creates a license key with this 
format: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

The key consists of a combination of upper case letters and digits.

It takes two arguments: parts and chars_per_part which default to 4 
and 8 respectively, so you can call the function like:

gen_key() to get a similar key as above, or
as gen_key(parts=3, chars_per_part=4) to get a shorter one, e.g. 
54N8-I70K-2JZ7
Before you default to random, check if Python >= 3.6 has a better 
option available for this task ...
"""
import secrets
import re
import textwrap


def gen_key(parts=4, chars_per_part=8):
    size = parts * chars_per_part
    key = re.findall(r"[A-Z0-9]", secrets.token_urlsafe(size).upper())
    return "-".join(textwrap.wrap("".join(key)[:size], chars_per_part))


# Pybites solution

from secrets import choice
from string import ascii_uppercase, digits

ALPHABET = ascii_uppercase + digits
DASH = "-"


def gen_key1(parts=4, chars_per_part=8):
    return DASH.join(
        "".join(choice(ALPHABET) for i in range(chars_per_part)) for _ in range(parts)
    )
