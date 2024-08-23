# Task: Password Validator
# Objective:

# Write a program that asks the user to enter a password.
# The program should repeatedly prompt the user to enter a password until they enter one that meets the following criteria:

# The password must be at least 8 characters long.
# The password must contain at least one uppercase letter.
# The password must contain at least one lowercase letter.
# The password must contain at least one digit.

# Instructions:

# Prompt the user to enter a password.
# Use a while loop to keep asking for a password until the user provides one that meets all the criteria.
# After the user enters a valid password, print a success message.

# ===============================================================================================
# Example:

# Enter a password: abc
# Password is too short.

# Enter a password: abcdefgh
# Password must contain at least one uppercase letter.

# Enter a password: ABCDEFGH
# Password must contain at least one lowercase letter.

# Enter a password: Abcdefgh
# Password must contain at least one digit.

# Enter a password: Abcdefg1
# Password is valid!
# ================================================================================================

# Hint:
# You can use the isupper(), islower(), and isdigit() string methods to check if a character is uppercase, lowercase, or a digit, respectively.

# ================================================================================================
# WRITE YOUR CODE BELOW #
# ================================================================================================


"""password="zuhal12"

if len(password) < 8:
    print("Password is too short.")
for char in password:
    if char.isupper():
        print("Password must contain at least one uppercase letter")""
"""

while True:

    password=input("Enter a password :")

    if len(password) < 8:
        print("Password is too short.")
        continue

    continue_upper = False
    continue_lower = False
    continue_digit = False

    for char in password:

        if char.isupper():
            continue_uppper = True

        if char.islower():
            continue_lower = True

        if char.isdigit():
            continue_digit = True

    if not continue_upper:
        print("Password must contain at least one uppercase letter.")
        continue

    if not continue_lower:
        print("Password must contain at least one lowercase letter.")
        continue

    if not continue_digit:
        print("Password must contain at least one digit.")
        continue

    print("Password is valid!")
    break



