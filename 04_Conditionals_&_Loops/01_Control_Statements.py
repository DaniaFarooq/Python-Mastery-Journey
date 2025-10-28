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
