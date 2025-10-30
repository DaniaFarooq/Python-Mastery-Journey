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
