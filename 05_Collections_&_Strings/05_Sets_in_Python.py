"""
SETS IN PYTHON
Unordered collections of unique elements
"""

print("=== SETS IN PYTHON ===\n")

# =============================================
# 1. CREATING SETS
# =============================================
print("1. CREATING SETS")

# Empty set
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with items
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# From list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(f"Numbers from list: {numbers}")

# Mixed data types
mixed_set = {1, "hello", 3.14, True}
print(f"Mixed set: {mixed_set}")

# String to set (unique characters)
word_set = set("programming")
print(f"String to set: {word_set}")
print()
