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

# =============================================
# 2. SET PROPERTIES
# =============================================
print("2. SET PROPERTIES")

# Sets are unordered
random_set = {"a", "b", "c", "d", "e"}
print(f"Set (unordered): {random_set}")

# Sets contain unique elements
duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(f"With duplicates: {duplicates}")

# Sets are mutable
colors = {"red", "green", "blue"}
colors.add("yellow")
print(f"After adding yellow: {colors}")

# But sets can only contain immutable elements
# This would cause an error:
# invalid_set = {[1, 2], [3, 4]}  # TypeError!
valid_set = {(1, 2), (3, 4)}  # Tuples are allowed
print(f"Set with tuples: {valid_set}")
print()

# =============================================
# 3. SET OPERATIONS
# =============================================
print("3. SET OPERATIONS")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union
union_set = set_a | set_b
print(f"Union (A | B): {union_set}")

# Intersection
intersection_set = set_a & set_b
print(f"Intersection (A & B): {intersection_set}")

# Difference
difference_set = set_a - set_b
print(f"Difference (A - B): {difference_set}")

# Symmetric Difference
symmetric_diff = set_a ^ set_b
print(f"Symmetric Difference (A ^ B): {symmetric_diff}")
print()

# =============================================
# 4. SET METHODS
# =============================================
print("4. SET METHODS")

numbers = {1, 2, 3, 4, 5}
print(f"Original set: {numbers}")

# Adding elements
numbers.add(6)
print(f"After add(6): {numbers}")

numbers.update([7, 8, 9])
print(f"After update([7,8,9]): {numbers}")

# Removing elements
numbers.remove(9)
print(f"After remove(9): {numbers}")

numbers.discard(8)  # Safe remove (no error if not found)
print(f"After discard(8): {numbers}")

popped = numbers.pop()  # Remove random element
print(f"After pop(): {numbers}, popped: {popped}")

# Clear set
numbers.clear()
print(f"After clear(): {numbers}")
print()

# =============================================
# 5. SET COMPARISONS
# =============================================
print("5. SET COMPARISONS")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2, 3}

print(f"Set X: {set_x}")
print(f"Set Y: {set_y}")
print(f"Set Z: {set_z}")

print(f"X is subset of Y: {set_x.issubset(set_y)}")
print(f"Y is superset of X: {set_y.issuperset(set_x)}")
print(f"X equals Z: {set_x == set_z}")
print(f"X is disjoint with {{6,7}}: {set_x.isdisjoint({6, 7})}")
print()
