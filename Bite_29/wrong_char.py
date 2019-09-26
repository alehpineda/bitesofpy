"""
Martin is preparing to pass an IQ test.

The most frequent task in this test is to find out 
which one of the given characters differs from the 
others. He observed that one char usually differs 
from the others in being alphanumeric or not.

Please help Martin! To check his answers, he needs 
a program to find the different one (the alphanumeric 
among non-alphanumerics or vice versa) among the given 
characters.

Complete get_index_different_char to meet this goal. 
It receives a chars list and returns an int index 
(zero-based).

Just to be clear, 
alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:

['A', 'f', '.', 'Q', 2]  # returns index 2 
(dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 
('a' is alphanumeric among non-alphanumerics)
See the TESTS tab for more details
"""
# My solution using regex
from re import findall

def get_index_different_char(chars):
    alpha = findall(r"[a-zA-Z0-9]", ''.join(map(str, chars)))
    non_alpha = findall(r"[^a-zA-Z0-9]", ''.join(map(str, chars)))

    if len(non_alpha) < len(alpha):
        return chars.index(non_alpha[0])
    else:
        return chars.index(int(alpha[0])) if alpha[0] in '1234567890' else chars.index(alpha[0])


# Solution from pybites
import string

alphanumeric_chars = list(string.ascii_letters + string.digits)


def get_index_different_char_1(chars):
    matches, no_matches = [], []
    for i, char in enumerate(chars):
        if str(char).lower() in alphanumeric_chars:
            matches.append(i)
        else:
            no_matches.append(i)
    return matches[0] if len(matches) == 1 else no_matches[0]

# Solution from pybites forum

def get_index_different_char_2(chars):
    # A list of 0,1's representing whether each char is alphanum or not
    #   1 if it is alphanum
    #   0 if not alphanum
    #   e.g. ['A', 'f', '.', 'Q', 2] = [1, 1, 0, 1, 1]
    num_alnum = [1 if str(char).isalnum() else 0 for char in chars]

    # If the sum of the array of ints == 1 this implies a single alphanum
    #   Return the index of the only 1 in the array
    # If the  sum of the array of ints > 1 this implies a single non alphanum
    #   Return the index of the only 0 in the array
    return num_alnum.index(1) if sum(num_alnum) == 1 else num_alnum.index(0)
