"""
CONTROL STATEMENTS IN PYTHON
Making decisions and controlling program flow
"""

print("=== CONTROL STATEMENTS IN PYTHON ===\n")
# =============================================
# 1. IF STATEMENT
# =============================================
print("1. IF STATEMENT")

age = 20
print(f"Age: {age}")

if age >= 18:
    print("You are an adult")
    print("You can vote!")

print("This always executes")
print()

# =============================================
# 2. IF-ELSE STATEMENT
# =============================================
print("2. IF-ELSE STATEMENT")

temperature = 25
print(f"Temperature: {temperature}°C")

if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")
print()

# =============================================
# 3. IF-ELIF-ELSE STATEMENT
# =============================================
print("3. IF-ELIF-ELSE STATEMENT")

score = 85
print(f"Score: {score}")

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
print()

# =============================================
# 4. NESTED IF STATEMENTS
# =============================================
print("4. NESTED IF STATEMENTS")

age = 25
has_license = True

print(f"Age: {age}, Has license: {has_license}")

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can drive legally")
    else:
        print("You need to get a license")
else:
    print("You are too young to drive")
print()

# =============================================
# 5. PRACTICAL EXAMPLES
# =============================================
print("5. PRACTICAL EXAMPLES")

# Example 1: Login System
print("LOGIN SYSTEM:")
username = "admin"
password = "12345"
input_username = "admin"
input_password = "12345"

if input_username == username and input_password == password:
    print("Login successful!")
    print("Welcome to the system")
else:
    print("Invalid username or password")
    print("Please try again")

# Example 2: Number Checker
print("\nNUMBER CHECKER:")
number = 15

print(f"Number: {number}")

if number > 0:
    print("Positive number")
    if number % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
elif number < 0:
    print("Negative number")
else:
    print("Number is zero")
print()

# =============================================
# 6. MULTIPLE CONDITIONS
# =============================================
print("6. MULTIPLE CONDITIONS")

# AND operator
age = 25
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("You cannot enter")

# OR operator
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")
else:
    print("Work day")

# NOT operator
is_raining = False

if not is_raining:
    print("Perfect weather for a walk")
else:
    print("Better stay inside")
print()

# =============================================
# 7. TRUTHY AND FALSY VALUES
# =============================================
print("7. TRUTHY AND FALSY VALUES")

name = "Python"
empty_string = ""
number = 10
zero = 0
if name:
    print("Non-empty string is True")

if not empty_string:
    print("Empty string is False")

if number:
    print("Non-zero number is True")

if not zero:
    print("Zero is False")
print()

# =============================================
# 8. KEY POINTS
# =============================================
print("8. KEY POINTS")

print("✓ Use if for single conditions")
print("✓ Use if-else for two outcomes")
print("✓ Use if-elif-else for multiple conditions")
print("✓ Indentation is crucial")
print("✓ Conditions can be combined with and, or, not")
print("✓ Empty values are False in conditions")

print("\n" + "="*50)
print("Complete! You learned Control Statements.")
