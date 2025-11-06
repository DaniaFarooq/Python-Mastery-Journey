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

# =============================================
# 5. KEYWORD ARGUMENTS
# =============================================
print("5. KEYWORD ARGUMENTS")

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Positional arguments
describe_pet("dog", "Buddy")

# Keyword arguments (order doesn't matter)
describe_pet(pet_name="Whiskers", animal_type="cat")

# Mix of positional and keyword
describe_pet("hamster", pet_name="Nibbles")
print()

# =============================================
# 6. PRACTICAL FUNCTION EXAMPLES
# =============================================
print("6. PRACTICAL FUNCTION EXAMPLES")

# Example 1: Calculator Functions
print("CALCULATOR FUNCTIONS:")

def calculate_area(length, width):
    return length * width

def calculate_volume(length, width, height):
    return length * width * height

room_area = calculate_area(10, 8)
room_volume = calculate_volume(10, 8, 3)

print(f"Room area: {room_area} sq ft")
print(f"Room volume: {room_volume} cubic ft")

# Example 2: Data Validation
print("\nDATA VALIDATION:")

def is_valid_age(age):
    return 0 <= age <= 120

def can_vote(age, is_citizen=True):
    return age >= 18 and is_citizen

print(f"Age 25 valid: {is_valid_age(25)}")
print(f"Age 150 valid: {is_valid_age(150)}")
print(f"Can 20-year-old citizen vote: {can_vote(20)}")
print(f"Can 16-year-old vote: {can_vote(16)}")
print()

# =============================================
# 7. VARIABLE SCOPE
# =============================================
print("7. VARIABLE SCOPE")

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Global inside function: {global_var}")
    
demonstrate_scope()
print(f"Global outside function: {global_var}")
# print(local_var)  # This would cause an error!
print()

# =============================================
# 8. DOCSTRINGS
# =============================================
print("8. DOCSTRINGS")

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    """
    return 3.14159 * radius ** 2
    
 # Using the function
area = calculate_circle_area(5)
print(f"Circle area with radius 5: {area:.2f}")

# View docstring
print("Function docstring:")
print(calculate_circle_area.__doc__)
print()

# =============================================
# 9. LAMBDA FUNCTIONS
# =============================================
print("9. LAMBDA FUNCTIONS")

# Simple lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
multiply = lambda a, b: a * b
print(f"3 * 4 = {multiply(3, 4)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Numbers: {numbers}")
print(f"Squared: {squared}")
print()

# =============================================
# 10. EXERCISES
# =============================================
print("10. EXERCISES")

print("Exercise 1: Temperature Converter")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

print("\nExercise 2: String Reverser")
def reverse_string(text):
    return text[::-1]

original = "Python"
reversed_text = reverse_string(original)
print(f"'{original}' reversed is '{reversed_text}'")
print()
