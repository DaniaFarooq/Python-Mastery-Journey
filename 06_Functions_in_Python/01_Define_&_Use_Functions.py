"""
FUNCTIONS IN PYTHON
Reusable blocks of code for organized programming
"""

print("=== FUNCTIONS IN PYTHON ===\n")

# =============================================
# 1. BASIC FUNCTION DEFINITION
# =============================================
print("1. BASIC FUNCTION DEFINITION")

# Simple function without parameters
def greet():
    print("Hello, welcome to Python!")
    
# Call the function
greet()
print()

# =============================================
# 2. FUNCTIONS WITH PARAMETERS
# =============================================
print("2. FUNCTIONS WITH PARAMETERS")

# Function with one parameter
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")
greet_name("Bob")

# Function with multiple parameters
def introduce(name, age):
    print(f"My name is {name} and I'm {age} years old.")

introduce("Charlie", 25)
print()
