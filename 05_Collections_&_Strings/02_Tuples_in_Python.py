"""
TUPLES IN PYTHON
Ordered, immutable collections of items
"""

print("=== TUPLES IN PYTHON ===\n")

# =============================================
# 1. CREATING TUPLES
# =============================================
print("1. CREATING TUPLES")

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with items
fruits = ("apple", "banana", "cherry")
print(f"Fruits: {fruits}")

# Single item tuple (comma required)
single_item = ("python",)
print(f"Single item: {single_item}")

# Without parentheses
numbers = 1, 2, 3, 4, 5
print(f"Without parentheses: {numbers}")

# Mixed data types
mixed = (1, "hello", 3.14, True)
print(f"Mixed tuple: {mixed}")
print()
