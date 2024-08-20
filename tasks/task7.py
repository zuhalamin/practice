# Task: Word Reversal
# Objective:

# Write a program that takes a sentence from the user and returns the sentence with each word reversed,
# but the order of the words remains the same.

# Instructions:

# Prompt the user to enter a sentence.
# Split the sentence into words.
# Reverse each word individually.
# Join the reversed words back into a single string.
# Print the resulting sentence.
# ================================================================================================
# Example:
# Enter a sentence: Hello World
# Result: olleH dlroW

# Enter a sentence: Python is fun
# Result: nohtyP si nuf
# ================================================================================================

# Hint:

# Use the split() method to break the sentence into words.
# Use slicing or the reversed() function to reverse each word.
# Use the join() method to combine the reversed words into a single string.

# ================================================================================================
# WRITE YOUR CODE BELOW #
# ================================================================================================

def reverse_sentances(sentance):
    words = sentance.split()
    x=[]
    for word in words:
      x.append(word[::-1])

    sentance =" ".join(x)
    print(sentance)  
user_input=input("Enter a sentence :")

reverse_sentances(sentance=user_input)



