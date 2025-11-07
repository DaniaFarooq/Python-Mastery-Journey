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
