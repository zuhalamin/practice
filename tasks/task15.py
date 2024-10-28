# Task 15: Simple Banking System
# Objective:

# Create a program that simulates a simple banking system.
# The program should allow users to create accounts, deposit money, withdraw money, check their balance,
# and view transaction history.

# Instructions:

# Initialize an empty dictionary to store user accounts.
# The keys should be the account numbers (integers or strings), and the values should be dictionaries containing the following information:
# "name": A string representing the account holder's name.
# "balance": A float representing the current balance in the account.
# "transactions": A list of dictionaries, where each dictionary represents a transaction with the following keys:
# "type": A string indicating the transaction type ("Deposit", "Withdrawal").
# "amount": A float representing the transaction amount.
# "balance_after": A float representing the balance after the transaction.

# Provide a menu with the following options:
# Create a new account
# Deposit money
# Withdraw money
# Check balance
# View transaction history
# Exit

# Implement the functionality for each menu option using if statements and loops.
# The program should continue running until the user chooses to exit.

# Menu Example:
# ================================================================================
# Banking System Menu:
# 1. Create a new account
# 2. Deposit money
# 3. Withdraw money
# 4. Check balance
# 5. View transaction history
# 6. Exit
# ================================================================================

# Functionality Details:

# Create a new account:
# Prompt the user to enter their name.
# Generate a unique account number (you can simply increment from a starting number like 1000).
# Initialize the account with a balance of 0 and an empty transaction history.
# Inform the user of their new account number.
# Deposit money:
# Prompt the user to enter their account number and the amount to deposit.
# If the account exists, update the balance and record the transaction in the transaction history.
# If the account does not exist, inform the user.
# Withdraw money:
# Prompt the user to enter their account number and the amount to withdraw.
# If the account exists and there are sufficient funds, deduct the amount from the balance and record the transaction.
# If the account does not exist or there are insufficient funds, inform the user.
# Check balance:
# Prompt the user to enter their account number.
# If the account exists, display the current balance.
# If the account does not exist, inform the user.
# View transaction history:
# Prompt the user to enter their account number.
# If the account exists, display the transaction history in a readable format.
# If the account does not exist, inform the user.
# Exit:
# Exit the program.
# Example Usage:

# ================================================================================
# Banking System Menu:
# 1. Create a new account
# 2. Deposit money
# 3. Withdraw money
# 4. Check balance
# 5. View transaction history
# 6. Exit

# Enter your choice: 1
# Enter your name: John Doe
# Your account number is 1000. Account created successfully.

# Enter your choice: 2
# Enter your account number: 1000
# Enter amount to deposit: 500.00
# Deposit successful. New balance: $500.00

# Enter your choice: 3
# Enter your account number: 1000
# Enter amount to withdraw: 200.00
# Withdrawal successful. New balance: $300.00

# Enter your choice: 4
# Enter your account number: 1000
# Your balance is: $300.00

# Enter your choice: 5
# Enter your account number: 1000
# Transaction history:
# 1. Deposit of $500.00, Balance after transaction: $500.00
# 2. Withdrawal of $200.00, Balance after transaction: $300.00

# Enter your choice: 6
# Goodbye!
# ================================================================================
# This task will help you practice working with dictionaries, managing nested data structures, and handling user input in a more complex scenario.
# It also introduces you to basic financial calculations and transaction management.

# ================================================================================================
# WRITE YOUR CODE BELOW
# ================================================================================================
