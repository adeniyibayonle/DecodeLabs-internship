# Laboratory Password Generator

import random
import string

print("\n===== LABORATORY PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + "@#$%"

password = ""

for i in range(length):

    password += random.choice(characters)

print("\nGenerated Password:", password)

if length < 6:
    print("Password Strength: Weak")

elif length < 10:
    print("Password Strength: Medium")

else:
    print("Password Strength: Strong")