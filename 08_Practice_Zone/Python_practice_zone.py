# This file contains python practice questions from all the topics that we have learned in this repo.
# ⭐ Don't forget to star this repo if you find it helpful! Your support keeps the code flowing!

# =======================================
# Escape characters and Print statements
# =======================================

# Q1: Write a program that prints a path like this:
# C:\Users\John\Desktop\File.txt using the appropriate escape sequences.

print("C:\\Users\\John\\Desktop\\File.txt")

# Q2: Write a Python program that prints a message with a double-quote character inside it.
# For example: He said, "Hello!".

msg1 = 'He said, "Hello!"'
print(msg1)

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
# If-Elif-Else Statements
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

# Q32. Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.

print("Enter 4 different numbers:")
while True:
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))
    c = int(input("Number 3: "))
    d = int(input("Number 4: "))
    if len({a, b, c, d}) == 4:
        smallest = min(a, b, c, d)
        print(f"The smallest number is: {smallest}")
        break
    else:
        print("Error: All numbers must be different. Please try again.\n")

# Q33 Ask a number from a user:
# print 'fizz' if number is divisble by 3.
# print 'buzz' if number is divisble by 5.
# print 'fizzbuzz' if number is divisble by 3 and 5.
# print the number itself if none of the conditions are true.

num = int(input("Enter the number = "))
if num % 3 == 0 and num % 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0 :
    print("fizz")
elif num % 5 == 0:
    print("buzz")
else:
    print(num)

# Q34. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# a. Take following input from user
# i. Number of classes held
# ii. Number of classes attended.
# b. Print percentage of class attended
# c. Print Is student is allowed to sit in exam or not.

# a. Take input from user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))
# b. Calculate percentage
attendance_percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {attendance_percentage:.2f}%")
# c. Check eligibility
if attendance_percentage >= 75:
    print(" Student is allowed to sit in the exam.")
else:
    print(" Student is NOT allowed to sit in the exam.")

# Q35 Take three numbers as input from user and print which one is greater or they are equal.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    print("Number 1 is greatest.")
elif num2 >= num1 and num2 >= num3:
    print("Number 2 is greatest.")
else:
    print("Number 3 is greatest.")

# Q36 Take Salary as input from User and Update the salary of an employee.
# salary less than 10,000, 5 % increment
# salary between 10,000 and 20, 000, 10 % increment
# salary between 20,000 and 50,000, 15 % increment
# salary more than 50,000, 20 % increment

Current_salary = int(input("Enter the current salary: "))
if Current_salary < 10000: # less than 10000
    increment = 0.05 * Current_salary
elif 10000 <= Current_salary <= 20000:
    increment = 0.10 * Current_salary
elif 20001 <= Current_salary <= 50000:
    increment = 0.15 * Current_salary
else:
    increment = 0.20 * Current_salary
updated_salary = Current_salary + increment
print(f"Increment: {increment}")
print(f"Updated Salary: {updated_salary}")

# Q37: An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
# A leap year contains a leap day. These are the conditions used to identify leap years:
# if the year can be evenly divided by 4, it is then a leap year but if the year is evenly divided by 4 and also by 100, then it is NOT a leap year but if the year is evenly divided by 4 and also by 400, then it is a leap year. This means the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Ask a year input from user. And tell if the year entered by user is leap or not

input_Year = int(input("Enter the year: "))
if input_Year % 4 == 0:
    if input_Year % 100 == 0:
        if input_Year % 400 == 0:
            print("It is a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year.")
else:
    print("It is not a leap year.")

# ========================================
# Nested If-Else Statements
# ========================================

# Q38. Write a program that takes three numbers as input and determines the largest one using nested if-else statements. Make sure all 3 numbers entered by user are different

input_1 = int(input("enter the first number = "))
input_2 = int(input("enter the second number = "))
input_3 = int(input("enter the third number = "))
# Check if all numbers are different
if input_1 != input_2 and input_1 != input_3 and input_2 != input_3:
    if input_1 > input_2:
        if input_1 > input_3:
            print("First number is the greatest.")
        else:
            print("Third number is the greatest.")
    else:
        if input_2 > input_3:
            print("Second number is the greatest.")
        else:
            print("Third number is the greatest.")
else:
    print("Please enter three different numbers. They must be unique.")

# Q39. Write a program that checks if a given year is a leap year. 
# Leap years are divisible by 4, but not by 100 unless they are also divisible by 400.

Year = int(input("Enter the year = "))
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("It is a leap year")  # divisible by 400
        else:
            print("It is not a leap year")  # divisible by 100 but not 400
    else:
        print("It is a leap year")  # divisible by 4 but not by 100
else:
    print("It is not a leap year")  # not divisible by 4

# Q40. Create a program that calculates the price of a movie ticket based on the age of the customer.
#If the customer is under 12, the ticket costs $5; if they are between 12 and 65, the ticket costs $10; otherwise, it's $7.

Age = int(input("Age of the customer = "))
if Age > 12:
    print("Ticket price is 5")
else:
    if Age <= 65:
        print("Ticket price is 10")
    else:
        print("Ticket price is 7")

# Q41. Write a program that calculates a person's BMI based on their height (in meters) and weight (in kilograms). Use the following formula: BMI = weight / (height^2). Then, classify the BMI according to the following ranges:
# Underweight: BMI less than 18.5
# Normal weight: BMI 18.5 - 24.9
# Overweight: BMI 25 - 29.9
# Obesity: BMI 30 or greater

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
if bmi < 18.5:
    print("You are underweight.")
else:
    if bmi < 25:
        print("You have a normal weight.")
    else:
        if bmi < 30:
            print("You are overweight.")
        else:
            print("You are obese.")

# ========================================
#  Basic While loop
# ========================================

# Q42. Ask a number from user. Print all the numbers from 1 to that number.

Num = int(input("Enter the number = "))
i = 1
while i <= Num:
    print(i)
    i  = i + 1
    
# Q43. Ask a number (N) from user. Print all the numbers from N to 1.

entered_number = int(input("Enter the number = "))
i = entered_number
while i >= 1:
    print(i)
    i = i - 1

# Q44. Ask start number and end number from user. Print all the numbers from start to end using while loop.

start = int(input("Enter the first number "))
end = int(input("Enter the last number "))
i = start
while i <= end:
    print(i)
    i = i + 1

# Q45. Calculate the sum of all the numbers from 1 to 10.

i = 1
total = 0
while i <= 10:
    total = total + i
    i = i + 1
print(f"sum is {total}")

# Q46. Calculate product of all the numbers from 1 to 10.

i = 1
total = 1
while i <= 10:
    total = total * i
    i = i + 1
print(f"the total product is {total}")

# Q47. Calculate how many numbers are divisible by 7 from 1 to 100.

i = 1
count = 0
while i <= 100:
    if i % 7 == 0:
       count = count + 1
    i = i + 1
print(f"the value is {count}")

# Q48. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.

i = 1
count = 0
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    i = i + 1
print(f"the total count is {count}")

# Q49. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.

num = 0
i = 20
while i <= 50:
    if i % 4 == 0:
        num = num + i
    i = i + 1
print(f"the sum is {num}")

# Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.

i = 1
count = 0
while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    i = i + 1
print(f"the count is {count}")

# Q51. Ask a number from user. Print the multiplication table of that number.

table_of = int(input("Enter the number = "))
i = 1
table = 1
while i <= 10:
    table = table_of * i 
    print(f"the table is {table_of} *{ i }= {table}")
    i = i + 1
    
# Q52. Calculate factorial of a number entered by user.
# Example:
# Enter a number = 5
# Factorial of a number means product of all the numbers from 1 to that
# number.
# 5 factorial = 5 x 4 x 3 x 2 x 1
# Output = 120

number = int(input("enter the number = "))
i = 1
factorial = 1
while i <= number:
    factorial = factorial * i
    i = i + 1
print(f"the factorial is {factorial}")

# Q53. Ask to numbers x and y from the user. If x < y then print all the numbers from x to y, 
# but if y  <x then print all the numbers from y to x.

x = int(input("Enter the number x = "))
y = int(input("Enter the number y = "))
if x < y:
    i = x
    while i <= y:
        print(i)
        i += 1
else:
    i = y
    while i <= x:
        print(i)
        i += 1

# =============================
# Basic For Loop 
# =============================

# Q54. Ask a number from user. Print all the numbers from 1 to that number.

num = int(input("Enter the number = "))
for i in range(1, num + 1):
    print(i)

# Q55. Ask a number (N) from user. Print all the numbers from N to 1.

Num = int(input("Enter the number = "))
for i in range(Num, 0, - 1):
    print(i)

# Q56. Ask start number and end number from user. Print all the numbers from start to end using while loop.

start = int(input("Enter the first number "))
end = int(input("Enter the last number "))
for i in range(start, end + 1):
    print(i)

# Q57. Calculate the sum of all the numbers from 1 to 10.

count = 0
for i in range(1, 10):
    count = count + 1
print(count)

# Q58. Calculate product of all the numbers from 1 to 10.

count = 1
for i in range(1, 11):
    count = count * i
print(f"the count is {count}")

# Q59. Calculate how many numbers are divisible by 7 from 1 to 100.

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count = count + 1
print(f"Count is {count}")

# Q60. Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.

count = 0
for i in range(1, 201):
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    print(f"Numbers divisible by 6 and 7 from 1 to 200 are {count} in total.")

#Q61. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.

total = 0
for num in range(20, 51):  # 51 because range end is exclusive
    if num % 4 == 0:
        total += num
print(f"Sum of numbers divisible by 4 from 20 to 50: {total}")

# Q62. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.

count = 0
for i in range(1, 201):
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    print(f"Numbers divisible by 6 and 7 from 1 to 200 are {count} in total.")

# Q 63 Ask a number from user. Print the multiplication table of that number.
# Example
# Enter a number = 8
# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24

table_of = int(input("Enter the number = "))
for i in range(1, 11):
    table = table_of * i
    print(f"{table_of} * {i} = {table}")

# Q64. Calculate factorial of a number entered by user.
# Example:
# Enter a number = 5
# Factorial of a number means product of all the numbers from 1 to that
# number.
# 5 factorial = 5 x 4 x 3 x 2 x 1
# Output = 120

num = int(input("Enter the number = "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print(f"the value of the factorial is = {factorial}")

# Q65. Ask to numbers x and y from the user. If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
if x < y:
    for i in range(x, y + 1):
        print(i)
else:
    for i in range(y, x + 1):
        print(i)

# ======================================
# Basic Nested Loops (patterns)
# ======================================

# Q66: Create a pattern using nested loop
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

for i in range(5):                        
    for j in range(5):                     
        print("*", end="")                 
    print()                                
print("\n" + "-"*20)

# Q67: Create a pattern using nested loop
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

for i in range(5):                       
    for j in range(1, 6):                  
        print(j, end="")
    print()
print("\n" + "-"*20)

# Q68: Create a pattern using nested loop
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

for i in range(5):                         
    for j in range(5, 0, -1):              
        print(j, end="")
    print()
print("\n" + "-"*20)

# Q69: Create a pattern using nested loop
# 1 1 1 1 1
# 2 2 2 2 2 
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):                      
    for j in range(5):                    
        print(i, end="")                  
    print()
print("\n" + "-"*20)


# Q70: Create a pattern using nested loop
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1 

for i in range(5, 0, -1):                 
    for j in range(5):                     
        print(i, end="")
    print()
print("\n" + "-"*20)

# Q71: Ask N from user. Print pattern:
# Example N=6
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 3 3 3 3 3 3
# 4 4 4 4 4 4
# 5 5 5 5 5 5
# 6 6 6 6 6 6 

n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):                 
    for j in range(n):                    
        print(i, end="")
    print()
print("\n" + "-"*20)

# Q72: Ask N from user. Print pattern:
# Example N=9
# 8 8 8 8 8 8 8 8 8
# 7 7 7 7 7 7 7 7 7
# 6 6 6 6 6 6 6 6 6
# 5 5 5 5 5 5 5 5 5
# 4 4 4 4 4 4 4 4 4 
# 3 3 3 3 3 3 3 3 3
# 2 2 2 2 2 2 2 2 2
# 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0

n = int(input("Enter the number of lines: "))
for i in range(n - 1, -1, -1):            
    for j in range(n):                    
        print(i, end="")
    print()
    
# ======================================
# Intermediate Nested Loops (patterns)
# ======================================

# Q73: Print the following pattern.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):             
        print(j, end="")
    print()


# Q74: Print the following pattern.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()

# Q75: Print the following pattern.
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(1, 6):
    for j in range(i, 0, -1):             
        print(j, end="")
    print()

# Q76: Print the following pattern.
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

for i in range(1, 6):
    for j in range(5, 5 - i, -1):          
        print(j, end="")
    print()

# Q77: Print the following pattern.
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

for i in range(1, 6):
    for j in range(i):
        print(6 - i, end="")               
    print()

# Q78: Print the following pattern.
# *
# * *
# * * *
# * * * *
# * * * * *

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Q79: Print the following pattern.
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

for i in range(5, 0, -1):
    for j in range(i):
        print(5 - j, end="")              
    print()

# Q80: Print the following pattern.
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(5, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

# Q81: Print the following pattern.
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
    
# Q82: Print the following pattern.
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Q83: Print the following pattern.
# 1
# 2 3
# 4 5 6
# 7 8 9 1 0
# 11 12 13 14 15

count = 1
for i in range(1, 6):
    for j in range(i):
        print(count, end="")
        count += 1
    print()

# Q84: Print the following pattern.
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(1, 6):
    for j in range(i, 0, -1):             
        print(j, end="")
    print()
    
# ======================================
# Advanvced Nested Loops (patterns)
# ======================================

# Q85: Print the following pattern.
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

# Q86: Print the following pattern.
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print(k + 1, end="")
    print()

# Q87: Print the following pattern.
#         1
#       2 2
#     3 3 3
#   4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()

# Q88: Print the following pattern.
#       *
#     * * *
#    * * * * *
#  * * * * * * *
# * * * * * * * * *

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q89: Print the following diamond pattern.
#      *
#    * * *
#   * * * * *
# * * * * * * *
#* * * * * * * * * 
#  * * * * * * *
#   * * * * *
#     * * *
#       *

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q90: Print the following inverted pyramid.
# * * * * * * * * *
#  * * * * * * *
#   * * * * *
#    * * *
#      *

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Q91: Print inverted + upright pyramid.
# * * * * * * * * *
#  * * * * * * *
#   * * * * *
#    * * *
#      *
#    * * *
#   * * * * *
#  * * * * * * *
# * * * * * * * * *

for i in range(5, 0, -1):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()
for i in range(2, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# ====================================
# Basic List iterations
# ====================================

# Q92. Make your own list. Print the list in reverse.

list_r = ["D", 89, "Python", False, 0.7]
print(list_r[::-1])

# Q93. Make your own list. Print all the even numbers present in the list.

list_ev = [1,2,3,4,5,6,7,8,9,10]
for var in list_ev:
    if var % 2 == 0:
        print(var, end = " ")

# Q94. Make your own list. Print all the odd numbers present in the list.

list_odd = [1,2,3,4,5,6,7,8,9,10]
for var in list_odd:
    if var % 2 != 0:
        print(var, end = " ")

# Q95. Make your own list. Print all the elements present at even index position.

list_e = ["Course", 90, "list", 0.98, 'hi']
print(list_e[0::2])

# Q96. Make your own list. Print the sum of all elements present in that list.

list_f = [1,2,3,4,5,6,7,8,9,10]
print(sum(list_f))

# Q97. Make your own list. Count the number of even numbers present in that list.

list_1 = [11,12,13,14,15,26,57,68,96,190]
even = 0
for a in list_1:
    if a % 2 == 0:
        even = even + 1
print(even)

# Q98. Make your own list. Count how many numbers are divisible by both 2 and 5 in that list. 

list_5 = [1,32,23,45,35,6,96,46,17,75,85,90,0,10,4,55,754,25,50, 60]
count = 0
for i in list_5:
    if i % 2 == 0 and i % 5 == 0:
        count = count + 1
print(count)

# Q99. Make your own list. Find the sum of all even numbers present in that.

list_2 = [1,32,23,45,35,6,96,46,17,75,85,90,0,10,4,55,754,25,50, 60]
even = 0
for a in list_2:
    if a % 2 ==0:  
        even += a
print(even)

# Q100. Make your own list. Find the sum of all numbers divisible by 3 or 4. 

list_s = [1,32,23,45,35,6,96,46,17,75,85,90,0,10,4,55,754,25,50, 60]
sum_s = 0
for i in list_s:
    if i % 3 == 0 or i % 4 == 0:
        sum_s = sum_s + i
print(sum_s)

# Q101. Make your own list. Print how many positive and negative numbers are there in that list.

list_1 = [1,4,5,6,2,-6,-4,-44,3,-3,2,6,-67,4]
positive = 0 
neg= 0
for i in list_1:
    if i > 0:
        positive = positive + 1
    if i < 0:
        neg = neg + 1
print(positive)
print(neg_)

# Q102. Make your own list. Print the largest number present in that list.

list_2 = [1, 4, 5, 6, 2, -6, -4, -44, 3, -3, 2, 6, -67, 4]
largest = list_2[0]
for i in list_2:
    if i > largest:  
        largest = i
print("Largest number:", largest) 

# Q103. Make your own list. Print the smallest number present in that list.

list_2 = [1, 4, 5, 6, 2, -6, -4, -44, 3, -3, 2, 6, -67, 4]
smallest = list_2[0]
for i in list_2:
    if i < smallest: 
        smallest = i
print("Smallest number:", smallest)  

# ====================================
# Basic List methods
# ====================================

# Q104. Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list.
# Display the final list as the output.

value = int(input("Enter how many numbers you want in the list = "))
answer = []
for i in range(value):
    num = int(input(f"Enter the number {i + 1}"))
    answer.append(num)
print(answer)

# Q105. Create a list and prompt the user for an 'old number' followed by a 'new number.' If the 'old number' exists in the list, replace it with the 'new number' provided by the user.

numbers = [34, 67, 12, 89, 45, 23, 78, 56, 91, 14, 33, 67, 82, 19, 41, 55, 73, 28, 97, 60]
num_odd = int(input("Enter the old number = "))
if num_odd % 2 != 0:
    print(f"{num_odd} is odd")
else:
    print(f"{num_odd} is not odd")
if num_odd in list_:
    new_num = int(input("Enter the new number = "))
    index = list_.index(num_odd)  
    list_[index] = new_num        
else:
    print("Number not found in the list.")
print(list_)

# Q106. Remove all the even numbers from the list.

numbers = [34, 67, 12, 89, 45, 23, 78, 56, 91, 14, 33, 67, 82, 19, 41, 55, 73, 28, 97, 60]
number = [num for num in numbers if num % 2 != 0]
print(number)

# Q107. Ask the user for a number. Then, from a list of numbers, remove all the numbers that can be divided by the number the user entered.

numb = [34, 67, 12, 89, 45, 23, 78, 56, 91, 14, 33, 67, 82, 19, 41, 55, 73, 28, 97, 60]
numb = []
num = int(input("Enter the number: "))
for i in numb:
    if i % num != 0:
        numb.append(i) 
print("Filtered list:", numb)

# 108. Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even.'
# Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list.

num = [34, 67, 12, 89, 12, 89, 45, 23, 78, 56, 91, 14, 33]
odd = []
even = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(even)

# Q109. Start by creating two separate lists with random numbers. 
# Then, create a third list that merges the numbers from the first and second lists together.

list1 = [12, 89, 45, 23, 78, 56, 91, 14, 33]
list2 = [32, 88, 4, 55, 90, 34, 23, 78, 64]
new_list= list1 + list2
print(new_list)

# ========================================
# List Methods (Intermediate)
# ========================================

# Q110. Make a list of your own. And remove all the duplicates element from that list.

list1 = [67, 12, 67, 12, 89, 12, 14, 33, 89, 12, 14, 33]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# Q111. Make a list. Then ask a number from user. If number exists in that list then print the position of the element else print -1.

list1 = [67, 12, 67, 12, 89, 12, 14, 33, 89, 12, 14, 33]
num = int(input("Enter the value = "))
if num in list_:
    position = list_.index(num)
    print(position)
else:
    print(-1)

# Q112. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

list_int = []
for i in range(10):
    num = int(input("Enter ten integers = "))
    list_int.append(num)
list_rev = list_int[::-1]
print(list_int)
print(list_rev)

# Q113. Write a program to find the average of all the numbers present in the list.

list1 = [67, 12, 67, 12, 89, 12, 14, 33, 89, 12, 14, 33]
for i in list1:
    list2 = (i / len(list1) ) * 100
print(list2)

# Q114: Find the occurrence of each element and print the one with highest occurrence.

list1 = [67, 12, 67, 12, 89, 12, 14, 33, 89, 12, 14, 33]
occurrence = {}
for num in list1:
    if num in occurrence:
        occurrence[num] += 1
    else:
        occurrence[num] = 1
max_element = max(occurrence, key=occurrence.get)
max_count = occurrence[max_element]
print("Occurrences:", occurrence)
print(f"Element with highest occurrence: {max_element} (appears {max_count} times)")

 # Q115. Write a program that has two lists and make a new list that contains only the common elements between them without duplicates.

l1 = [1,  2, 67, 12, 89, 12, 3, 4, 4, 5, 56, 6, 7, 7]
l2 = [67, 12, 67, 12, 89, 12, 14, 33, 89, 12, 14, 33]
l3 = []
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)

# Q116. Write a Python code to find the second largest element in a list without sorting.

def second_largest(lst):
    first = second = float('-inf')
    
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None

# Q117. Make a program that takes a list of integers and returns the product of all the elements.

def product_of_list(lst):
    if not lst:
        return 0
    product = 1
    for num in lst:
        product *= num
    return product

# Q118.  Write a program to find and print all prime numbers within a given list.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def find_primes_in_list(lst):
    return [num for num in lst if is_prime(num)]
    
# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
prime_numbers = find_primes_in_list(numbers)
print(f"Prime numbers in the list: {prime_numbers}")

# Q119. Write a program to split a given list into two halves.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
mid = len(numbers) // 2  
list_a = numbers[:mid]  
list_b = numbers[mid:] 
print(list_a)
print(list_b)

# Q120. Write a program that swaps the first and last elements of a given list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)

# ==================================
# List Comprehension
# ==================================

# Q121. Generate a list of squares of numbers from 1 to 10 using list comprehension.

squares = [x**2 for x in range(1, 11)]
print(squares)

# Q122. Given a list of strings, create a new list containing the lengths of each string using list comprehension.

lst = ["learning", "python", "with", "Dania"]
len_list = [len(i) for i in lst]
print(len_list)

# Q123. Generate a list of strings where each string repeats itself three times, using list comprehension.

lst = ["learning", "python", "with", "Dania"]
rep_list = [i*3 for i in lst]
print(rep_list)

# Q124. Generate a list of list using list comprehension where format should be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]].

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
new_list = [[i, "ODD"] if i % 2 != 0 else [i, "EVEN"] for i in lst]
print(new_list)

# ================================
# List Slicing Questions
# ================================

# Q125. Write a python program to reverse a list using slicing.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
print(lst[::-1])

# Q126. Write a python program to get every third element from a list using slicing.

list1 = ["learning", "python", "with", "Dania", 2, 3, 4, 5,]
print(list1[::3])

# Q127. Implement a python program to split a list into two equal parts using Slicing. 
# One list should contain 1st half and another list should contain 2nd half.

list_2 = ["learning", "python", "with", "Dania", 2, 3, 4, 5,]
splt = len(list_2) // 2
list_a = list_2[:splt]
list_b = list_2[splt:]
print(list_a)
print(list_b)

# Q128. Implement a python program to get the last 'n' elements from a list using slicing.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
n = int(input("Enter the nth value = "))
last_n_elements = lst[-n:]
print(last_n_elements)

# Q129. Ask ‘n’ from user. Create a list of last n elements but in reverse order using slicing.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
n = int(input("Enter the nth value = "))
last_n_elements = lst[-n:][::-1]
print(last_n_elements)

# Q130. Ask start and end index from the user. Create a list from start index to end index using slicing.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
new_lst = lst[start:end]
print(new_lst)

# Q131. Ask start and end index from the user. Create a list of last n elements but in reverse order using slicing.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 19, 21]
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
reversed_lst = lst[start:end][::-1]
print(reversed_lst)

# ==================================
# String Methods (Part-1)
# ==================================

# Q132. Ask a string from user. Count how many alphabets are there in that string.

strg = input("Enter a string: ")
count = 0
for ch in strg:
    if ch.isalpha():
        count = count + 1
print(count)

# Q133. Ask a string from user. Count the number of uppercase an lowercase characters in that String.

strg_1 = input("Enter a string with some uppercase and lowercase characters: ")
upper_count = 0
lower_count = 0
for ch in strg_1:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)


# Q134. Ask a string from user. Convert all the alphabets to uppercase.

strg = input("Enter a string: ")
strg_upper = strg_.upper()
print(strg_upper)

# Q135. Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and don’t change the other letters. 

text = input("Enter the string: ")
result = ""
for char in text:
    if char.isupper():
        result = result + char.lower()
    elif char.islower():
        result = result + char.upper()
    else:
        result = result + char
print(result)

# Q136. Count the number of spaces in a string entered by user.

strng = "Python     Mastery      Repo"
print(strng.count(" "))

# Q137. Ask a string from user. Print the count of how many alphabets, digits, spaces and symbols are there in that string.

text = input("Enter the string: ")
alphabets = 0
digits = 0
spaces = 0
symbols = 0
for char in text:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        space += 1
    else:
        symbols += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Symbols:", symbols)

# ==================================
# String Methods (Part-2)
# ==================================

# Q138. Write a program to reverse the order of words.

strng = "Python  Mastery  Repo"
reversed_str = " ".join(strng.split()[::-1])
print(reversed_str)

# Q139. Write a program that accepts a string and capitalizes the first letter of each word 
# while converting all other letters to lowercase.

str_1 = input("Enter a string: ")
result = str_1.title()
print("Formatted string:", result)

# Q140. Write a program that reverses each word in a sentence while maintaining the word order. 
# For example, "Hello World" should become "olleH dlroW".

strg = "Python  Mastery  Repo"
reversed_words = " ".join(word[::-1] for word in strg.split())
print(reversed_words)

# Q141. Write a program that converts a string in camelCase to snake_case. 
# For example, converting "helloWorldHowAreYou" should result in "hello_world_how_are_you". 

def camel_to_snake(camel_str):
    snake_str = ""
    for char in camel_str:
        if char.isupper():  
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str

# ====================================
# Dictionary Iteration
# ====================================

# Q142. Ask subject name and marks from the user and keep adding it to the dictionary Ask total number of subjects.

total_sub = int(input("Enter the total number of subjects: "))
subjects = {}
for i in range(total_sub):
    sub = input(f"Enter the name of subject {i+1}: ")
    marks = int(input(f"Enter the marks for {sub}: "))
    subjects[sub] = marks  
print("\nSubjects and Marks:")
print(subjects)
