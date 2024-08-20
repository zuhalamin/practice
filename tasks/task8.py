# Task: Vowel Counter
# Objective:

# Write a program that counts the number of vowels in a given string.
# The program should ignore case, meaning it should count both uppercase and lowercase vowels.

# Instructions:

# Prompt the user to enter a string.
# Convert the string to lowercase to handle case insensitivity.
# Count the number of vowels (a, e, i, o, u) in the string.
# Print the total number of vowels.
# ===============================================================================================
# Example:
# Enter a string: Hello World
# Number of vowels: 3

# Enter a string: Python is Amazing
# Number of vowels: 5
# ================================================================================================
# Hint:
# Use the lower() method to convert the string to lowercase.
# Use a loop or a comprehension to iterate through the characters and count the vowels.

# ================================================================================================
# WRITE YOUR CODE BELOW #
# ================================================================================================


def count_number(sentance):
    count=0
    vowel =["a","e","i","o","u"]
    for word in sentance.lower():
        for latter in word:
            if latter in vowel:
              count += 1
    print("number of vowel in :",count)

             
user_input = input("Number of vowle: ")

count_number(user_input)