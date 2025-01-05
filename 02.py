# Aim
# Write a program in Python that generates a random password with a specified length.

import random
import string

passwordLength = random.randrange(0,99,1)
charList = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(passwordLength):
    password += random.choice(charList)

print(f"Generated Password: {password}")