"""
INPUT FUNCTION IN PYTHON
Getting user input with input() function
"""

print("=== INPUT FUNCTION GUIDE ===\n")

# =============================================
# 1. BASIC INPUT
# =============================================
print("1. BASIC INPUT")

# Simple input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input without message
age = input()
print(f"You entered: {age}")
print()

# =============================================
# 2. INPUT WITH DIFFERENT DATA TYPES
# =============================================
print("2. INPUT WITH CONVERSION")

# String input (default)
color = input("What's your favorite color? ")
print(f"Nice! {color} is a great color!")

# Number input - convert to integer
number = input("Enter a number: ")
number_int = int(number)
print(f"Your number doubled: {number_int * 2}")

# =============================================
# 3. SIMPLE EXAMPLES
# =============================================
print("3. SIMPLE EXAMPLES")

# Example 1: Personal info
print("PERSONAL INFO:")
user_name = input("What is your name? ")
user_age = input("How old are you? ")
user_city = input("Where do you live? ")

print(f"\nHello {user_name}!")
print(f"You are {user_age} years old.")
print(f"You live in {user_city}.")
# Decimal input - convert to float
price = input("Enter a price: ")
price_float = float(price)
print(f"Price with tax: ${price_float * 1.1:.2f}")
print()

# Example 2: Simple calculator
print("\nSIMPLE CALCULATOR:")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to numbers
n1 = int(num1)
n2 = int(num2)

print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")

# Example 3: Favorite things
print("\n⭐ FAVORITE THINGS:")
food = input("What's your favorite food? ")
movie = input("What's your favorite movie? ")
hobby = input("What's your hobby? ")

print(f"\nYou love eating {food}!")
print(f"You enjoy watching {movie}!")
print(f"Your hobby is {hobby}!")
print()

# =============================================
# 4. COMMON MISTAKES
# =============================================
print("4. COMMON MISTAKES")

print("❌ Forgetting to convert numbers:")
# age = input("Enter age: ")
# print(age + 5)  # Error! Can't add string and number

print("✅ Always convert numbers:")
age = input("Enter age: ")
age_int = int(age)
print(f"In 5 years, you'll be {age_int + 5}")

print("\n❌ No input validation:")
# number = int(input("Enter number: ")) 
# If user enters text, program crashes

print("✅ Check if input is number:")
user_input = input("Enter a number: ")
if user_input.isdigit():
    number = int(user_input)
    print(f"Good! You entered: {number}")
else:
    print("Please enter a valid number")
print()

# =============================================
# 5. SIMPLE EXERCISES
# =============================================
print("5. SIMPLE EXERCISES")

print("Exercise 1: Greeting Program")
# Get user's name and age
# Print a personalized greeting

print("\nExercise 2: Simple Math")
# Ask for two numbers
# Print their sum and product

print("\nExercise 3: Story Maker")
# Ask for a name, place, and animal
# Create a simple story using them
print()

# =============================================
# 6. QUICK TIPS
# =============================================
print("6. QUICK TIPS")

print("✓ input() always returns a string")
print("✓ Convert to int() for numbers") 
print("✓ Convert to float() for decimals")
print("✓ Use meaningful prompt messages")
print("✓ Always validate user input")

print("\n" + "="*40)
print("Great! You learned input() function!")
