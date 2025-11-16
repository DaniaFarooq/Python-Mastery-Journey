# This file contains python practice questions from all the topics that we have learned in this repo.
# Solutions are the code lines without # symbol. 
# ⭐ Don't forget to star this repo if you find it helpful! Your support keeps the code flowing!

# =======================================
# Escape characters and Print statement
# =======================================

# Q1: Write a program that prints a path like this:
# C:\Users\John\Desktop\File.txt using the appropriate escape sequences.

print("C:\\Users\\John\\Desktop\\File.txt")

# Q2: Write a Python program that prints a message with a double-quote character inside it.
# For example: He said, "Hello!".

msg = 'He said, "Hello!"'
print(msg)

# Q3: Create a program that prints a message containing both single anddouble quotes, like this: She said, 'It's cold'.

msg2 = "She said, 'It's cold'."
print(msg2)

# ========================================
# User input and Type casting
# ========================================

# Q4: Write a Python program to add two numbers entered by the user.

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
result = num1 + num2
print(f"The sum of both numbers is: {result}")
