"""
MASTERING THE PRINT() FUNCTION IN PYTHON
The print() function is your gateway to displaying output in Python.
"""

print("=== MASTERING PYTHON PRINT() FUNCTION ===\n")

# =============================================
# 1. BASIC PRINT USAGE
# =============================================
print("1. BASIC PRINT USAGE")
print("Hello, World!")  # Simple text
print(42)               # Numbers
print(3.14)             # Decimals
print(True)             # Boolean values
print()

# =============================================
# 2. PRINTING VARIABLES
# =============================================
print("2. PRINTING VARIABLES")

name = "Dania"
age = 25
score = 95.5
is_active = True

print("Name:", name)
print("Age:", age)
print("Score:", score)
print("Active:", is_active)
print()

# =============================================
# 3. STRING CONCATENATION IN PRINT
# =============================================
print("3. STRING CONCATENATION")

first_name = "Python"
last_name = "Programmer"

print("Full name: " + first_name + " " + last_name)
print("I am " + str(age) + " years old")  # Note: convert numbers to string
print()

# =============================================
# 4. F-STRINGS (MODERN WAY - RECOMMENDED!)
# =============================================
print("4. F-STRINGS (MODERN FORMATTING)")

language = "Python"
version = 3.11
rating = 9.8

print(f"I love {language} version {version}!")
print(f"My rating: {rating}/10")
print(f"Next year I'll be {age + 1} years old")
print(f"Uppercase name: {name.upper()}")
print()

# =============================================
# 5. SEPARATOR PARAMETER
# =============================================
print("5. CUSTOM SEPARATORS")

print("Apple", "Banana", "Cherry")  # Default: space separator
print("Apple", "Banana", "Cherry", sep=", ")
print("Apple", "Banana", "Cherry", sep=" -> ")
print("Apple", "Banana", "Cherry", sep="")
print("2023", "12", "25", sep="-")
print()

# =============================================
# 6. END PARAMETER
# =============================================
print("6. CUSTOM LINE ENDINGS")

print("Hello", end=" ")      # No newline, just space
print("World!", end="!!!")   # Custom ending
print()  # Add a newline
print("Loading", end="")
print("...", end="")
print(" Complete!")
print()

print("Countdown:", end=" ")
for i in range(3, 0, -1):
    print(i, end="... ")
print("Go!")
print()

# =============================================
# 7. MULTIPLE ITEMS AND FORMATTING
# =============================================
print("7. ADVANCED FORMATTING")

# Multiple items with different types
item = "Python Book"
price = 29.99
quantity = 3

print("Item:", item, "| Price: $", price, "| Quantity:", quantity)
print(f"Item: {item} | Price: ${price} | Quantity: {quantity}")
print(f"Total: ${price * quantity:.2f}")  # 2 decimal places
print()

# =============================================
# 8. PRINTING SPECIAL CHARACTERS
# =============================================
print("8. SPECIAL CHARACTERS & ESCAPE SEQUENCES")

print("This is a tab:\t-> See the space?")
print("This is a newline:\n-> See the new line?")
print("This shows quotes: \"Python\" is awesome!")
print('This shows apostrophe: It\'s easy!')
print("Backslash: C:\\Users\\Documents")
print()

# =============================================
# 9. MULTI-LINE PRINTING
# =============================================
print("9. MULTI-LINE OUTPUTS")

# Method 1: Multiple print statements
print("Line 1")
print("Line 2")
print("Line 3")

# Method 2: Multi-line string
print("\nShopping List:")
print("""- Apples
- Bananas
- Milk
- Bread""")

# Method 3: Using \n
print("\nDaily Routine:\n1. Wake up\n2. Code Python\n3. Learn Data Science\n4. Repeat!")
print()
