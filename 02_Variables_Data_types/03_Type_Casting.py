"""
TYPE CONVERSION & TYPE CASTING IN PYTHON
Converting between different data types is essential for data processing.
"""

print("=== MASTERING TYPE CONVERSION IN PYTHON ===\n")

# =============================================
# 1. WHAT IS TYPE CONVERSION?
# =============================================
print("1. WHAT IS TYPE CONVERSION?")
print("   - Converting from one data type to another")
print("   - Also called 'type casting'")
print("   - Essential for data processing and calculations")
print("   - Two types: Implicit & Explicit\n")

# =============================================
# 2. IMPLICIT CONVERSION (AUTOMATIC)
# =============================================
print("2. IMPLICIT CONVERSION - PYTHON DOES IT AUTOMATICALLY")

# Integer to Float
integer_num = 5
float_num = 2.5
result = integer_num + float_num  # int → float automatically
print(f"Integer + Float: {integer_num} + {float_num} = {result}")
print(f"  Types: {type(integer_num)} + {type(float_num)} → {type(result)}")

# Boolean to Integer
true_value = True
false_value = False
num = 10
result1 = num + true_value   # True becomes 1
result2 = num + false_value  # False becomes 0
print(f"\nBoolean to Integer:")
print(f"  10 + True = {result1}  (True → 1)")
print(f"  10 + False = {result2} (False → 0)")
