import string
from random import *

def generate_pass():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(16))
    return password