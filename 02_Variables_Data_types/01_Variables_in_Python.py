"""
VARIABLES IN PYTHON
Variables are containers for storing data values.
Think of them as labeled boxes that hold information.
"""

print("=== MASTERING VARIABLES IN PYTHON ===\n")

# =============================================
# 1. WHAT ARE VARIABLES?
# =============================================
print("1. WHAT ARE VARIABLES?")
print("   - Named containers that store data")
print("   - Like labeled boxes holding information")
print("   - Can store different types of data")
print("   - Values can be changed (they're variable!)\n")

# =============================================
# 2. BASIC VARIABLE ASSIGNMENT
# =============================================
print("2. BASIC VARIABLE ASSIGNMENT")

# Creating variables
name = "Dania"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")
print()

# =============================================
# 3. VARIABLE NAMING RULES
# =============================================
print("3. VARIABLE NAMING RULES")

#  Valid variable names
first_name = "Alice"
last_name = "Smith"
age2 = 30
_user_id = 12345
total_score = 95

#  Invalid variable names (commented out to avoid errors)
# 2nd_place = "silver"    # Cannot start with number
# first-name = "John"     # No hyphens allowed
# class = "Python"        # Cannot use reserved words

print(" Valid: first_name, age2, _user_id, totalScore")
print(" Invalid: 2nd_place, first-name, class (reserved word)")
print()

# =============================================
# 4. PYTHON IS DYNAMICALLY TYPED
# =============================================
print("4. DYNAMIC TYPING - NO TYPE DECLARATIONS")

# Python figures out the type automatically
score = 95          # Integer
score = 95.5        # Now it's a float!
score = "A+"        # Now it's a string!

print(f"Score: {score} (type: {type(score)})")

# =============================================
# 5. MULTIPLE ASSIGNMENT
# =============================================
print("5. MULTIPLE ASSIGNMENT TRICKS")

# Assign multiple variables at once
x, y, z = 10, 20, 30
print(f"x = {x}, y = {y}, z = {z}")

# Assign same value to multiple variables
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")

# Swap values easily
name1, name2 = "Alice", "Bob"
print(f"Before swap: name1 = {name1}, name2 = {name2}")
name1, name2 = name2, name1  
print(f"After swap: name1 = {name1}, name2 = {name2}")
print()

# =============================================
# 6. VARIABLE REASSIGNMENT
# =============================================
print("6. CHANGING VARIABLE VALUES")

counter = 0
print(f"Counter: {counter}")

counter = 5        # Change the value
print(f"Counter: {counter}")

counter = counter + 3  # Increase by 3
print(f"Counter: {counter}")

counter += 2       # Shortcut for counter = counter + 2
print(f"Counter: {counter}")
