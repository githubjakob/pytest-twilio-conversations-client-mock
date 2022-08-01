from string import digits, ascii_letters
from random import choice as randomchoice


def create_sid(prefix, size=10):

    random = "".join(randomchoice(digits) for x in range(size))
    return f"{prefix}{random}"
