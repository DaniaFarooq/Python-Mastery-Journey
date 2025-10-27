"""
OPERATORS IN PYTHON
Symbols that perform operations on variables and values
"""

print("=== OPERATORS IN PYTHON ===\n")

# =============================================
# 1. ARITHMETIC OPERATORS
# =============================================
print("1. ARITHMETIC OPERATORS")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")
print()

# =============================================
# 4. ASSIGNMENT OPERATORS
# =============================================
print("4. ASSIGNMENT OPERATORS")

count = 5
print(f"Initial count = {count}")

count += 3  # count = count + 3
print(f"After count += 3 → {count}")

count -= 2  # count = count - 2
print(f"After count -= 2 → {count}")

count *= 4  # count = count * 4
print(f"After count *= 4 → {count}")

count /= 2  # count = count / 2
print(f"After count /= 2 → {count}")
print()
# =============================================
# 2. COMPARISON OPERATORS
# =============================================
print("2. COMPARISON OPERATORS")

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"Equal: {x} == {y} → {x == y}")
print(f"Not Equal: {x} != {y} → {x != y}")
print(f"Greater Than: {x} > {y} → {x > y}")
print(f"Less Than: {x} < {y} → {x < y}")
print(f"Greater or Equal: {x} >= {y} → {x >= y}")
print(f"Less or Equal: {x} <= {y} → {x <= y}")
print()

# =============================================
# 3. LOGICAL OPERATORS
# =============================================
print("3. LOGICAL OPERATORS")

has_license = True
has_car = False
age = 25

print(f"has_license = {has_license}, has_car = {has_car}, age = {age}")
print(f"AND: has_license AND has_car → {has_license and has_car}")
print(f"OR: has_license OR has_car → {has_license or has_car}")
print(f"NOT: NOT has_car → {not has_car}")
print(f"Combined: age >= 18 AND has_license → {age >= 18 and has_license}")
print()

# =============================================
# 5. IDENTITY OPERATORS
# =============================================
print("5. IDENTITY OPERATORS")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2 → {list1 is list2}")  # Different objects
print(f"list1 is list3 → {list1 is list3}")  # Same object
print(f"list1 is not list2 → {list1 is not list2}")
print()

# =============================================
# 6. MEMBERSHIP OPERATORS
# =============================================
print("6. MEMBERSHIP OPERATORS")

fruits = ["apple", "banana", "cherry"]
name = "Python"

print(f"fruits = {fruits}")
print(f"'apple' in fruits → {'apple' in fruits}")
print(f"'mango' not in fruits → {'mango' not in fruits}")
print(f"'P' in '{name}' → {'P' in name}")
print(f"'z' not in '{name}' → {'z' not in name}")
print()

# =============================================
# 7. PRACTICAL EXAMPLES
# =============================================
print("7. PRACTICAL EXAMPLES")

# Example 1: Age verification
print("AGE VERIFICATION:")
user_age = 20
can_vote = user_age >= 18
can_drive = user_age >= 16
is_senior = user_age >= 65

print(f"Age: {user_age}")
print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")
print(f"Is senior: {is_senior}")
