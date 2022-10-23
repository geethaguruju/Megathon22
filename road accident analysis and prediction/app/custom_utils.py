from random import choices
from string import ascii_letters, digits


def generate_id():
    chars = ascii_letters + digits
    return ''.join(choices(chars, k=8))