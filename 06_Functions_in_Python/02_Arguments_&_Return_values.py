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
