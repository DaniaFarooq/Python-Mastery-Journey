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
