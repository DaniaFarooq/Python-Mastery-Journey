"""
CONDITIONAL STATEMENTS IN PYTHON
Deep dive into if, elif, else for decision making
"""

print("=== CONDITIONAL STATEMENTS IN PYTHON ===\n")

# =============================================
# 1. BASIC IF STATEMENT
# =============================================
print("1. BASIC IF STATEMENT")

number = 10
print(f"Number: {number}")

if number > 0:
    print("The number is positive")
    print("This is inside the if block")

print("This is outside the if block")
print()

# =============================================
# 2. IF-ELSE STATEMENT
# =============================================
print("2. IF-ELSE STATEMENT")

age = 16
print(f"Age: {age}")

if age >= 18:
    print("You are eligible to vote")
    print("You can participate in elections")
else:
    print("You are not eligible to vote")
    print("Wait until you are 18 years old")
print()
