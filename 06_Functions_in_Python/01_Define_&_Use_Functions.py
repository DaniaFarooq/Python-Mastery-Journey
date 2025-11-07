"""
DEFINING & USING FUNCTIONS IN PYTHON
Creating and calling reusable code blocks
"""

print("=== DEFINING & USING FUNCTIONS ===\n")

# =============================================
# 1. WHAT ARE FUNCTIONS?
# =============================================
print("1. WHAT ARE FUNCTIONS?")

print("✓ Reusable blocks of code")
print("✓ Perform specific tasks")
print("✓ Make code organized and readable")
print("✓ Avoid repetition")
print()

# =============================================
# 2. DEFINING FUNCTIONS
# =============================================
print("2. DEFINING FUNCTIONS")

# Basic function definition
def welcome_message():
    print("Welcome to Python Programming!")
    print("Let's learn about functions!")

# Function with one parameter
def greet_student(name):
    print(f"Hello, {name}! Ready to learn Python?")

# Function with multiple parameters
def student_info(name, age, course):
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")
print()

# =============================================
# 3. CALLING FUNCTIONS
# =============================================
print("3. CALLING FUNCTIONS")

print("→ Calling welcome_message():")
welcome_message()

print("\n→ Calling greet_student():")
greet_student("Alice")
greet_student("Bob")

print("\n→ Calling student_info():")
student_info("Dania", 20, "Data Science")
student_info("Yasir", 22, "AI Engineering")
print()

# =============================================
# 4. FUNCTION STRUCTURE
# =============================================
print("4. FUNCTION STRUCTURE")

def demonstrate_structure():
    """
    This function shows the basic structure of a Python function.
    It has a docstring, function body, and print statements.
    """
    print("1. Function definition starts with 'def'")
    print("2. Function name follows naming conventions")
    print("3. Parentheses for parameters")
    print("4. Colon to start the function body")
    print("5. Indented code block")
    print("6. Optional docstring for documentation")
    
# Call the function
demonstrate_structure()
print()

# =============================================
# 5. FUNCTION NAMING RULES
# =============================================
print("5. FUNCTION NAMING RULES")

print("✓ Use descriptive names")
print("✓ Use lowercase with underscores")
print("✓ Be consistent with naming style")
print("✓ Avoid reserved keywords")

# Good function names
def calculate_average():
    pass  # placeholder

def get_user_input():
    pass

