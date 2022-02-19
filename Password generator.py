import string
from random import *
characters = string.digits + string.ascii_letters + string.punctuation
password = "".join(choice(characters)for x in range (randint(7,21)))
print(password)