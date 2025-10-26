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
