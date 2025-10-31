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

# =============================================
# 4. LIST OPERATIONS
# =============================================
print("4. LIST OPERATIONS")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"list1 + list2: {combined}")

# Repetition
repeated = list1 * 3
print(f"list1 * 3: {repeated}")

# Membership
print(f"2 in list1: {2 in list1}")
print(f"7 in list1: {7 in list1}")

# Length
print(f"Length of list1: {len(list1)}")
print()

# =============================================
# 5. LIST METHODS
# =============================================
print("5. LIST METHODS")

numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"Original: {numbers}")

# Sort
numbers.sort()
print(f"After sort(): {numbers}")

# Reverse
numbers.reverse()
print(f"After reverse(): {numbers}")

# Count
count_1 = numbers.count(1)
print(f"Count of 1: {count_1}")

# Index
index_4 = numbers.index(4)
print(f"Index of 4: {index_4}")

# =============================================
# 6. LIST COMPREHENSIONS
# =============================================
print("6. LIST COMPREHENSIONS")

# Create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase words: {uppercase}")
print()

# Clear
numbers.clear()
print(f"After clear(): {numbers}")
print()

# =============================================
# 7. PRACTICAL EXAMPLES
# =============================================
print("7. PRACTICAL EXAMPLES")

# Example 1: Student Grades
print("STUDENT GRADES:")
grades = [85, 92, 78, 96, 88]
print(f"Grades: {grades}")

average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Example 2: Shopping List
print("\nSHOPPING LIST:")
shopping_list = ["milk", "bread", "eggs", "butter"]
print(f"Shopping list: {shopping_list}")

shopping_list.append("cheese")
print(f"After adding cheese: {shopping_list}")

shopping_list.remove("eggs")
print(f"After removing eggs: {shopping_list}")

# =============================================
# 8. COMMON LIST OPERATIONS
# =============================================
print("8. COMMON LIST OPERATIONS")

data = [5, 2, 8, 1, 9]
print(f"Original data: {data}")

print(f"Sorted: {sorted(data)}")
print(f"Sum: {sum(data)}")
print(f"Maximum: {max(data)}")
print(f"Minimum: {min(data)}")

# Copying lists
original = [1, 2, 3]
copy1 = original.copy()
copy2 = original[:]

print(f"Original: {original}")
print(f"Copy: {copy1}")
print()

# =============================================
# 9. LIST PROPERTIES
# =============================================
print("9. LIST PROPERTIES")

print("✓ Ordered - items maintain their position")
print("✓ Mutable - can change after creation")
print("✓ Allows duplicates")
print("✓ Can contain different data types")
print("✓ Dynamic size - grows and shrinks as needed")

print("\n" + "="*50)
print("Congratulations, Your Python foundation is getting stronger every day!")
