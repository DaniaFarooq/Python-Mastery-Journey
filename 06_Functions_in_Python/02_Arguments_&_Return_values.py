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

# =============================================
# 6. MULTIPLE RETURN VALUES
# =============================================
print("6. MULTIPLE RETURN VALUES")

def calculate_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

def get_student_data():
    name = "Alex"
    age = 20
    grades = [85, 92, 78]
    return name, age, grades

# Using multiple returns
scores = [10, 20, 30, 40, 50]
stats_total, stats_avg, stats_max, stats_min = calculate_statistics(scores)

student_name, student_age, student_grades = get_student_data()

print(f"Scores: {scores}")
print(f"Total: {stats_total}, Average: {stats_avg:.1f}")
print(f"Max: {stats_max}, Min: {stats_min}")

print(f"\nStudent: {student_name}, Age: {student_age}")
print(f"Grades: {student_grades}")
print()

# =============================================
# 7. PRACTICAL EXAMPLES
# =============================================
print("7. PRACTICAL EXAMPLES")

# Example 1: Grade Calculator
print("📊 GRADE CALCULATOR:")

def calculate_grade(score, max_score=100):
    percentage = (score / max_score) * 100
    return percentage
def get_grade_letter(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

student_score = 85
percent = calculate_grade(student_score)
grade_letter = get_grade_letter(percent)

print(f"Score: {student_score}/100")
print(f"Percentage: {percent:.1f}%")
print(f"Grade: {grade_letter}")

