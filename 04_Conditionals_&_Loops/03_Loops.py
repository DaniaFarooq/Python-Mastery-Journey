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
