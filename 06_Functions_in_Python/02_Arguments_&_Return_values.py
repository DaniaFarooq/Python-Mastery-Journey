"""
ARGUMENTS & RETURN VALUES IN PYTHON
Passing data to functions and getting results back
"""

print("=== ARGUMENTS & RETURN VALUES ===\n")

# =============================================
# 1. FUNCTION PARAMETERS VS ARGUMENTS
# =============================================
print("1. PARAMETERS VS ARGUMENTS")

def student_profile(name, grade, subject):  # Parameters
    print(f"Name: {name}")
    print(f"Grade: {grade}")
    print(f"Subject: {subject}")

# Calling with arguments
student_profile("Alice", "A", "Math")      # Arguments
student_profile("Bob", "B+", "Science")    # Arguments

print("\n✓ Parameters: Variables in function definition")
print("✓ Arguments: Actual values passed to function")
print()

# =============================================
# 2. POSITIONAL ARGUMENTS
# =============================================
print("2. POSITIONAL ARGUMENTS")

def book_info(title, author, year):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")

print("→ Position matters:")
book_info("Python Basics", "John Smith", 2024)
book_info("Data Science", "Jane Doe", 2023)

print("\n✓ Values assigned based on position")
print("✓ Order must match parameter order")
print()

# =============================================
# 3. KEYWORD ARGUMENTS
# =============================================
print("3. KEYWORD ARGUMENTS")

def course_details(name, duration, level):
    print(f"Course: {name}")
    print(f"Duration: {duration} weeks")
    print(f"Level: {level}")

print("→ Using keyword arguments:")
course_details(name="Python", duration=8, level="Beginner")
course_details(level="Advanced", name="Machine Learning", duration=12)

print("\n✓ Specify parameter names")
print("✓ Order doesn't matter")
print("✓ Makes code more readable")
print()

# =============================================
# 4. DEFAULT ARGUMENTS
# =============================================
print("4. DEFAULT ARGUMENTS")

def enroll_student(name, course="Python Basics", status="Active"):
    print(f"Student: {name}")
    print(f"Course: {course}")
    print(f"Status: {status}")

print("→ With default values:")
enroll_student("Alice")                           # Uses defaults
enroll_student("Bob", "Data Science")            # Override course
enroll_student("Charlie", "Web Dev", "Pending")  # Override both

print("\n✓ Provide fallback values")
print("✓ Make parameters optional")
print("✓ Must come after required parameters")
print()

# =============================================
# 5. RETURN STATEMENTS
# =============================================
print("5. RETURN STATEMENTS")

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b
        
# Using return values
sum_result = add_numbers(5, 3)
product_result = multiply_numbers(4, 7)
max_result = find_maximum(10, 15)

print(f"5 + 3 = {sum_result}")
print(f"4 × 7 = {product_result}")
print(f"Maximum of 10 and 15: {max_result}")
print()
