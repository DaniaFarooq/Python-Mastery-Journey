"""
LISTS IN PYTHON
Ordered, mutable collections of items
"""

print("=== LISTS IN PYTHON ===\n")

# =============================================
# 1. CREATING LISTS
# =============================================
print("1. CREATING LISTS")

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# Mixed data types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# List with duplicate items
numbers = [1, 2, 2, 3, 3, 3]
print(f"Numbers with duplicates: {numbers}")
print()

# =============================================
# 2. ACCESSING LIST ITEMS
# =============================================
print("2. ACCESSING LIST ITEMS")

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors: {colors}")

# Positive indexing
print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")
print(f"Third color: {colors[2]}")
