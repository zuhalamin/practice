# Task Six: Sum of List Elements
# Scenario:

# Create a Python script that calculates and prints the sum of all elements in a list of numbers provided by the user.

# Objective:

# Encapsulate the logic for summing the elements in a list within a method.
# The script should prompt the user to enter a list of numbers (comma-separated) and then use the method to compute and print the sum.

# Steps to Complete the Task:

# Define a Method:
# Create a method named sum_of_list that takes one parameter: numbers_list.
# Inside the method, use a loop or built-in function to calculate the sum of the list elements.
# User Input:
# In the main part of the script, prompt the user to enter a list of numbers (comma-separated).
# Process Input:
# Convert the user input into a list of numbers.
# Call the Method:
# Pass the list of numbers to the sum_of_list method to compute and print the sum.

#########################
# WRITE YOUR CODE BELOW #
#########################

def sum_of_list(numbers_list):
    list= range(numbers_list)
    for sum in list:
        x += sum
        print(sum)
number=int(input("Enter your number: ")) 
sum_of_list(numbers_list=[])  