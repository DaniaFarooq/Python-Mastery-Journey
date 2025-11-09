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
