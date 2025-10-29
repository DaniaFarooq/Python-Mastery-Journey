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

# =============================================
# 3. IF-ELIF-ELSE CHAIN
# =============================================
print("3. IF-ELIF-ELSE CHAIN")

marks = 78
print(f"Marks: {marks}")

if marks >= 90:
    print("Excellent! Grade: A+")
elif marks >= 80:
    print("Very Good! Grade: A")
elif marks >= 70:
    print("Good! Grade: B")
elif marks >= 60:
    print("Average! Grade: C")
elif marks >= 50:
    print("Pass! Grade: D")
else:
    print("Fail! Grade: F")
print()

# =============================================
# 4. MULTIPLE CONDITIONS
# =============================================
print("4. MULTIPLE CONDITIONS")

# Using AND
temperature = 25
is_sunny = True
print(f"Temperature: {temperature}°C, Sunny: {is_sunny}")

if temperature > 20 and is_sunny:
    print("Perfect weather for picnic")
else:
    print("Maybe stay indoors today")

# Using OR
has_coupon = False
is_member = True
print(f"\nHas coupon: {has_coupon}, Is member: {is_member}")

if has_coupon or is_member:
    print("You qualify for discount")
else:
    print("No discount available")

# Using NOT
is_raining = False
print(f"\nIs raining: {is_raining}")

if not is_raining:
    print("No umbrella needed")
else:
    print("Take an umbrella")
print()

# =============================================
# 5. NESTED CONDITIONALS
# =============================================
print("5. NESTED CONDITIONALS")

age = 22
has_license = True
has_car = False

print(f"Age: {age}, License: {has_license}, Car: {has_car}")

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You have a valid license")
        if has_car:
            print("You can drive your car")
        else:
            print("You need to get a car")
    else:
        print("You need to get a driving license")
else:
    print("You are too young to drive")
print()

# =============================================
# 7. COMPARISON OPERATORS IN CONDITIONS
# =============================================
print("7. COMPARISON OPERATORS")

a = 15
b = 10

print(f"a = {a}, b = {b}")

if a == b:
    print("a equals b")
elif a != b:
    print("a does not equal b")

if a > b:
    print("a is greater than b")

if a < b:
    print("a is less than b")
if a >= b:
    print("a is greater than or equal to b")

if a <= b:
    print("a is less than or equal to b")
print()
