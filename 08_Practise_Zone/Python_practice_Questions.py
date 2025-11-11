# This file contains 150+ Python practice questions alongwith my suggested solutions.
# For your convenience in learning, I've created seperate sections for questions of each topic.
# If you find this repo helpful, show your support by giving it a star.

# After understanding the Python theory section, Let's start our practice journey:

# ==============================================
# Python Practice Questions and Solutions:
# ==============================================


# ==============================================
# Print statement and Escape sequences
# ==============================================

# Q1: Print the following path using escape sequences:
#     C:\Users\John\Desktop\File.txt

print( 'C:\\Users\\John\\Desktop\\File.txt')    

# Q2: Print a message containing double quotes: He said, "Hello!".

print( 'He said, "Hello!".')    

# Q3: Print a message containing both single and double quotes:
# She said, 'It's cold'.

print("She said, 'It's cold'.")

# ===============================================
# Input function and Type conversions
# ===============================================

# Q4: Add two numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
added = num1 + num2
print(f'Sum of both numbers is : {added}')
