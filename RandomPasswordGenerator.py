import random
import string
from HelperFunctions import *

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

count = input("How long should the password be: ")

while(not is_number(count)):
    count = input("Please enter number input: ")

password = generate_password(int(count))
print(password)