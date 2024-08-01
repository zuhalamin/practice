# Task Two: Refactor Task One Logic into a Method
# Objective:

# Refactor the number comparison logic from Task One into a method to promote code organization and reusability.

# Description:

# In Task One, we created a simple script to compare two numbers input by the user. The goal of Task Two is to encapsulate this comparison logic into a dedicated method named compare_numbers. This method will handle the comparison and printing of results based on user inputs, allowing the main script to remain clean and focused on user interaction.

# Steps to Complete the Task:

# Create a Method:
# Define a method called compare_numbers that takes two parameters: first_number and second_number.
# Inside the method, emplement TASK1 core logic.
# User Input:
# In the main part of the script, prompt the user to enter the first and second numbers.
# Call the Method:
# Pass the user-provided numbers to the compare_numbers method to execute the comparison.
# Benefits of This Approach:

# Modularity: The comparison logic is separated from user input handling, making the code easier to manage and maintain.
# Reusability: The compare_numbers method can be reused in other parts of the program or in different programs if needed.

#########################
# WRITE YOUR CODE BELOW #
#########################
def comper_numbers(first,second):
    if first>second:
     print('The first number is greater than the second number.')
    elif first<second:
     print('The first number is less than the second number.')
    else:
     print('Both numbers are equal.')




num1=input('Enter first number:')
num2=input('Enter your second number:')
comper_numbers(num1,num2)

num3=input('Enter first number:')
num4=input('Enter your second number:')
comper_numbers(num3,num4)
