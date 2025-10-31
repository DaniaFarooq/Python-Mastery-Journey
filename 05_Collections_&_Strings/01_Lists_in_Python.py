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

# Negative indexing
print(f"Last color: {colors[-1]}")
print(f"Second last: {colors[-2]}")

# Slicing
print(f"First three: {colors[0:3]}")
print(f"From index 2: {colors[2:]}")
print(f"Last two: {colors[-2:]}")
print()

# =============================================
# 3. MODIFYING LISTS
# =============================================
print("3. MODIFYING LISTS")

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# Change item
numbers[2] = 10
print(f"After numbers[2] = 10: {numbers}")

# Add items
numbers.append(6)
print(f"After append(6): {numbers}")

numbers.insert(1, 15)
print(f"After insert(1, 15): {numbers}")

# Remove items
numbers.remove(15)
print(f"After remove(15): {numbers}")

popped = numbers.pop()
print(f"After pop(): {numbers}, popped: {popped}")

del numbers[0]
print(f"After del numbers[0]: {numbers}")
print()
