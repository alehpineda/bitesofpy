"""
Create a function that reverses the letters in a given string, 
but keeps the digits in their original position.
Example:
foo("a8c") -> "c8a"
foo("1x2") -> "1x2"
foo("a1b2c3") -> "c1b2a3"
"""

def reverse_str(letters):
    is_str = [char for char in letters if char.isalpha()]
    reverse = []
    for char in letters:
        if char.isdigit():
            reverse.append(char)
        if char.isalpha():
            reverse.append(is_str.pop())
    return ''.join(reverse)


print(reverse_str("a8c"))
print(reverse_str("1x2"))
print(reverse_str("a1b2c3"))
