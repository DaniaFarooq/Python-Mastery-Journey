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

# =========================================
# Arithematic and Assignment Operators
# =========================================

# Q12. Write a Python program that takes two numbers as input and performs the following operations: addition, subtraction, multiplication,
# division, and modulus. Display the results.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# Q13. Write a Python program to swap the values of two variables without using a temporary variable.

a = 6
b = 12
a, b = b, a
print("a =", a)
print("b =", b)

# Q14. Write a Python program to calculate the compound interest for a given principal, rate of interest, and time period. 
# Ask everything from the user.

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time (in years): "))
A = P * (1 + R / 100) ** T
print("Compound Interest Amount:", A)

# Q15. Write a Python program that takes the radius of a circle as input and calculates its area. 

radius = float(input("Enter the radius: "))
circle_area = 3.14 * radius ** 2
print("Area of the circle =", circle_area)

# =========================================
# Comparison and Logical operators
# =========================================

# Q16. Guess the output.

x = 5
y = 3
print(x > y)  # True

# Q17. Guess the output. 

a = 10
b = 20
c = 30
print(a < b and b < c)  # True

# Q18. Guess the output.

p = True
q = False
print(not p or q)  # False

# Q19. Guess the output.

num1 = 15
num2 = 10
print(num1 == num2 or num1 > num2)  # True

# Q20. Guess the output.

m = 8
n = 6
print(m >= n and n != m)  # True

# Q21. Guess the output.

a = 5
b = 5
c = 10
print(a <= b and b != c)  # True

# Q22. Guess the output.

num = 25
print(num % 2 == 0)  # False 

# =====================================
# If-Else Statement 
# =====================================

# Q23. Write a Python program that takes an integer input and prints whether it's positive, negative. (Consider 0 as positive)

num = int(input("Enter an integer: "))
if num >= 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# Q24. Write a program that takes a character as input and prints whether it's a vowel or a consonant. (Multiple OR will be used)

char = input("Enter a single character: ").lower()
if char in 'aeiou':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

# Q25. Write a program that takes two numbers as input and checks if the first number is divisible by the second.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num2 == 0:
    print("Error: Division by zero is not allowed.")
elif num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")

# Q26. A student will not be allowed to sit in exam if his/her attendance is less than 75%. Take following input from user:
# Number of classes held, Number of classes attended.

classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print(" The student is allowed to sit in the exam.")
else:
    print(" The student is NOT allowed to sit in the exam.")

# =======================================
# If Elif Else Statements
# =======================================

# Q27. Write a program to check if the number is ODD, EVEN or Equal to Zero.

number = int(input("enter the number = "))
if number == 0:
    print("The number is zero.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Q28. Write a program to check if number is divisible by 2 and 3 but not 8.

Num = int(input("Enter the number = "))
if Num % 2 == 0 and Num % 3 == 0 and Num % 8 != 0:
    print("The number is divisible by 2 and 3 but NOT by 8.")
else:
    print("Condition unsatisfied.")

# Q29. Write a program to print the last digit of a number. (NOT A IF ELSE QUESTION)
# Example  Input: 45321  Output: 1

number = 6789989
last = number % 10
print(last)

# Q30. Write a program to check if the last digit of a number is divisible by 5 or not.

num = 865433235
num1 = num % 10
print(num1)
if num1 % 5 == 0:
    print("number is divible by 5")
else:
    print("number is not divible by 5")

# Q31. Write a program to calculate bill. Ask the final amount from the user.You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.

amount = float(input("Enter bill amount: Rs. "))
if amount >= 50000:
    discount = 30
elif amount >= 40000:
    discount = 25
elif amount >= 30000:
    discount = 20
elif amount >= 10000:
    discount = 10
elif amount >= 1:
    discount = 0
else:
    print("Invalid amount!")
    discount = None    
if discount is not None:
    discount_amount = (discount / 100) * amount
    final_bill = amount - discount_amount
    print(f"You got {discount}% discount")
    print(f"Your final bill is Rs. {final_bill:.2f}")
