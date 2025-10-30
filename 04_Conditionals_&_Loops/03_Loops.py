"""
LOOPS IN PYTHON
Repeating actions with for and while loops
"""

print("=== LOOPS IN PYTHON ===\n")

# =============================================
# 1. FOR LOOP BASICS
# =============================================
print("1. FOR LOOP BASICS")

print("→ Looping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  I like {fruit}")

print("\n→ Looping through a string:")
word = "Python"
for letter in word:
    print(f"  Letter: {letter}")

print("\n→ Looping with range():")
for i in range(5):
    print(f"  Number: {i}")
print()

# =============================================
# 2. WHILE LOOP BASICS
# =============================================
print("2. WHILE LOOP BASICS")

print("→ Basic while loop:")
count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1

print("\n→ While loop with condition:")
temperature = 30
while temperature > 20:
    print(f"  Temperature: {temperature}°C")
    temperature -= 2
print()

# =============================================
# 3. RANGE() FUNCTION
# =============================================
print("3. RANGE() FUNCTION")

print("→ range(stop):")
for i in range(5):
    print(f"  i = {i}")

print("\n→ range(start, stop):")
for i in range(2, 6):
    print(f"  i = {i}")

print("\n→ range(start, stop, step):")
for i in range(0, 10, 2):
    print(f"  i = {i}")

print("\n→ Counting backwards:")
for i in range(5, 0, -1):
    print(f"  i = {i}")
print()

# =============================================
# 4. LOOP CONTROL STATEMENTS
# =============================================
print("4. LOOP CONTROL STATEMENTS")

print("→ break - exit loop early:")
for i in range(10):
    if i == 5:
        break
    print(f"  i = {i}")
    
print("\n→ continue - skip current iteration:")
for i in range(5):
    if i == 2:
        continue
    print(f"  i = {i}")
    
print("\n→ pass - placeholder:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    print(f"  i = {i}")
print()

# =============================================
# 5. NESTED LOOPS
# =============================================
print("5. NESTED LOOPS")

print("→ Multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i * j}")
    print("  ---")
print()

# =============================================
# 6. PRACTICAL EXAMPLES
# =============================================
print("6. PRACTICAL EXAMPLES")

# Example 1: Number operations
print("NUMBER OPERATIONS:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(f"  {num}")

print("\nSum of numbers:")
total = 0
for num in numbers:
    total += num
print(f"  Total: {total}")

# Example 2: Shopping cart
print("\nSHOPPING CART:")
items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [1000, 25, 75, 300]

print("Shopping list:")
total_cost = 0
for i in range(len(items)):
    print(f"  {items[i]} - ${prices[i]}")
    total_cost += prices[i]

print(f"Total: ${total_cost}")
print()

# =============================================
# 7. LOOPING THROUGH DICTIONARIES
# =============================================
print("7. LOOPING THROUGH DICTIONARIES")

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print("→ Looping through keys:")
for key in student:
    print(f"  Key: {key}")

print("\n→ Looping through values:")
for value in student.values():
    print(f"  Value: {value}")

print("\n→ Looping through items:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# =============================================
# 8. COMMON LOOP PATTERNS
# =============================================
print("8. COMMON LOOP PATTERNS")

print("→ Accumulator pattern:")
numbers = [1, 2, 3, 4, 5]
sum_result = 0
for num in numbers:
    sum_result += num
print(f"  Sum: {sum_result}")

print("\n→ Search pattern:")
names = ["Alice", "Bob", "Charlie", "Diana"]
search_name = "Bob"
found = False
for name in names:
    if name == search_name:
        found = True
        break

print(f"  Found {search_name}: {found}")

print("\n→ Counter pattern:")
grades = ["A", "B", "A", "C", "B", "A"]
count_a = 0
for grade in grades:
    if grade == "A":
        count_a += 1
print(f"  Number of A grades: {count_a}")
print()

# =============================================
# 9. LOOP BEST PRACTICES
# =============================================
print("9. LOOP BEST PRACTICES")

print("✓ Use for loops when you know iteration count")
print("✓ Use while loops for conditional repetition")
print("✓ Avoid infinite loops with proper exit conditions")
print("✓ Use meaningful variable names in loops")
print("✓ Keep loop bodies focused and readable")
print("✓ Use break and continue sparingly")

print("\n" + "="*50)
print("Congrats! You mastered Loops in Python.")
