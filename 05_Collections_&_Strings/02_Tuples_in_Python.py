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

# =============================================
# 4. TUPLE OPERATIONS
# =============================================
print("4. TUPLE OPERATIONS")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"tuple1 + tuple2: {combined}")

# Repetition
repeated = tuple1 * 2
print(f"tuple1 * 2: {repeated}")

# Membership
print(f"2 in tuple1: {2 in tuple1}")
print(f"7 in tuple1: {7 in tuple1}")

# Length
print(f"Length of tuple1: {len(tuple1)}")
print()

# =============================================
# 5. TUPLE METHODS
# =============================================
print("5. TUPLE METHODS")

numbers = (3, 1, 4, 1, 5, 9, 2, 1)
print(f"Numbers: {numbers}")

# Count
count_1 = numbers.count(1)
print(f"Count of 1: {count_1}")

# Index
index_4 = numbers.index(4)
print(f"Index of 4: {index_4}")

# Index with start position
index_1_after_2 = numbers.index(1, 2)
print(f"Index of 1 after position 2: {index_1_after_2}")
print()
