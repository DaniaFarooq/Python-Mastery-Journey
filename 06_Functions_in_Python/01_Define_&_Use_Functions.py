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

# =============================================
# 3. RETURN STATEMENTS
# =============================================
print("3. RETURN STATEMENTS")

# Function that returns a value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Function with multiple returns
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(f"10 is {check_number(10)}")
print(f"-5 is {check_number(-5)}")
print(f"0 is {check_number(0)}")
print()

# =============================================
# 4. DEFAULT PARAMETERS
# =============================================
print("4. DEFAULT PARAMETERS")

def greet_person(name, message="Hello"):
    print(f"{message}, {name}!")

greet_person("Alice")                    # Uses default message
greet_person("Bob", "Good morning")      # Uses custom message
greet_person("Charlie", "Welcome")       # Uses custom message

# Multiple default parameters
def create_profile(name, age=25, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

create_profile("Diana")
create_profile("Eve", 30)
create_profile("Frank", 35, "New York")
print()
