# Task: Character Frequency Counter
# Objective:

# Write a program that counts the frequency of each character in a given string, ignoring spaces.
# The program should print each character and its corresponding frequency.

# Instructions:

# Prompt the user to enter a string.
# Remove all spaces from the string.
# Initialize an empty dictionary to keep track of character frequencies.
# Use a for loop to iterate through each character in the string.
# Use an if statement to check if the character is already in the dictionary:
# If it is, increment its count.
# If it isn't, add it to the dictionary with a count of 1.
# Print each character and its frequency.
# ===============================================================================================
# Example:

# Enter a string: Hello World
# Character frequencies:
# H: 1
# e: 1
# l: 3
# o: 2
# W: 1
# r: 1
# d: 1

# Enter a string: Python programming
# Character frequencies:
# P: 1
# y: 1
# t: 1
# h: 1
# o: 2
# n: 2
# p: 1
# r: 2
# g: 2
# a: 1
# m: 2
# i: 1
# ================================================================================================

# Hint:

# Use the replace() method to remove spaces from the string.
# Use a dictionary to keep track of character counts.

# ================================================================================================
# WRITE YOUR CODE BELOW #
# ================================================================================================

user_input=input("Enter a string:")
new_input= user_input.replace(" ","")


dic={}

for lst in new_input:

    if lst in dic:
        dic[lst] +=1
    else:
        dic[lst]=1


print("Character frequenciesf: ")

for charactr,char in dic.items():
    print(f"{charactr}:{char}")



    
