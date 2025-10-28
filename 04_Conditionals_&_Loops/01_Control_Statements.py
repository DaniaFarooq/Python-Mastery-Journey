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
