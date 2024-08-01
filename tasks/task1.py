# Task: Number Comparison

# Write a Python script that asks the user to input two numbers and then compares them.
# The script should:

# Prompt the user to input the first number.
# Prompt the user to input the second number.
# Compare the two numbers and print:
# "The first number is greater than the second number."
# "The first number is less than the second number."
# "Both numbers are equal."
# Requirements:

# Use if, elif, and else statements to handle the comparison.
# Ensure the script correctly handles all possible cases.
num1=input('Please enter your number:')
num2=input('please enter yoyr number:')
if num1>num2:
    print('The first number is greater than the second number.')
elif num1<num2:
    print('The first number is less than the second number.')
elif num1==num2:
    print('Both numbers are equal.')

