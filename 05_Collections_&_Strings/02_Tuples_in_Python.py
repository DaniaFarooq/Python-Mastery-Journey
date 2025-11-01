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

# =============================================
# 2. ACCESSING TUPLE ITEMS
# =============================================
print("2. ACCESSING TUPLE ITEMS")

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Colors: {colors}")

# Positive indexing
print(f"First color: {colors[0]}")
print(f"Second color: {colors[1]}")

# Negative indexing
print(f"Last color: {colors[-1]}")
print(f"Second last: {colors[-2]}")

# Slicing
print(f"First three: {colors[0:3]}")
print(f"From index 2: {colors[2:]}")
print(f"Last two: {colors[-2:]}")
print()

# =============================================
# 3. TUPLE PROPERTIES
# =============================================
print("3. TUPLE PROPERTIES")

# Tuples are immutable
coordinates = (10, 20)
print(f"Coordinates: {coordinates}")

# This would cause an error:
# coordinates[0] = 15  # TypeError!

# But you can create new tuples
new_coordinates = (15, coordinates[1])
print(f"New coordinates: {new_coordinates}")

# Tuples can contain mutable objects
mixed_tuple = ([1, 2], [3, 4])
mixed_tuple[0].append(3)
print(f"Modified inner list: {mixed_tuple}")
print()
