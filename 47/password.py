import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):
    """ Function to validate password """

    punctuation_chars = "".join(PUNCTUATION_CHARS)
    reg = fr"^(?=.*[a-z]{{2,}})(?=.*[A-Z])(?=.*\d)(?=.*[{punctuation_chars}])[A-Za-z\d{punctuation_chars}]{{6,12}}$"
    pat = re.compile(reg)  # compiling regex
    mat = re.search(pat, password)  # searching regex

    if mat and password not in used_passwords:  # validating conditions
        used_passwords.add(password)
        return True
    return False


def validate_password1(password):
    if not 6 <= len(password) <= 12:
        return False

    if not re.search(r"[a-z].*[a-z]", password):
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not any(char in PUNCTUATION_CHARS for char in password):
        return False

    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True
