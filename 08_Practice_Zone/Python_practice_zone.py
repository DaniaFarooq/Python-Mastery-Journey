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

# Q5. Convert a string to an integer and vice versa.

str_num = "786"
print(int(str_num))  # String to integer
int_num = 786
print(str(int_num))  # Integer to string

# Q6: Calculate the area of a rectangle using user input.

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
area = length * width
print(f"The area of the rectangle is: {area}")

# Q7: Calculate the average of three numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"The average is: {average}")

# Q8: Convert between float and integer.

f_value = 123.45
print(int(f_value))  # Float to integer
int_value = 8097
print(float(int_value))  # Integer to float

# Q9: Write a program that converts a temperature in Fahrenheit to Celsius.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"Temperature in Celsius: {celsius}")

# Q10: Calculate sum of 5 subjects and Find percentage.

marks = [78, 65, 54, 87, 31]
total = sum(marks)
percentage = (total / 500) * 100  
print("Percentage =", percentage)

# Q11: Ask number of games played in a tournament. Ask the user number of games won and number of games loss.
# Calculate number of tie and total points. (1 win= 4 points, 1 tie =2 points)

total = int(input("Enter total number of games: "))
won = int(input("Enter number of games won: "))
lost = int(input("Enter number of games lost: "))
ties = total - (won + lost)
points = (won * 4) + (ties * 2)
print(f"Tied games: {ties}")
print(f"Total points: {points}")

# ============================================
# Arithematic and Assignment Operators
# ============================================

