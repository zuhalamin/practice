#  Task: Word Length Calculator
# Objective:

# Write a program that takes a list of words from the user and calculates the length of each word.
# Store the words and their lengths in a dictionary and print the dictionary.

# Instructions:

# Prompt the user to enter a list of words separated by spaces.
# Split the input string into individual words.
# Create an empty dictionary to store each word and its length.
# Use a for loop to iterate through the list of words.
# For each word, calculate its length and add it to the dictionary with the word as the key and the length as the value.
# Print the resulting dictionary.
# ===============================================================================================
# Example:

# Enter words separated by spaces: apple banana cherry
# Word lengths: {'apple': 5, 'banana': 6, 'cherry': 6}

# Enter words separated by spaces: dog cat elephant
# Word lengths: {'dog': 3, 'cat': 3, 'elephant': 8}
# ================================================================================================

# Hint:

# Use the split() method to break the input string into a list of words.
# Use the len() function to get the length of each word.

# ================================================================================================
# WRITE YOUR CODE BELOW #
# ================================================================================================
# 

def convert_words_to_dic(words_list):
      dic={}
      for word in words_list:
            dic[word]=len(word)

      print(dic)


user_input=input("Enter words separeted by space :")
lst=user_input.split()

convert_words_to_dic(lst)


