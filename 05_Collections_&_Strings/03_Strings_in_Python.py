"""
STRINGS IN PYTHON
Working with text data in Python
"""

print("=== STRINGS IN PYTHON ===\n")

# =============================================
# 1. CREATING STRINGS
# =============================================
print("1. CREATING STRINGS")

# Single quotes
single = 'Hello World'
print(f"Single quotes: {single}")

# Double quotes
double = "Python Programming"
print(f"Double quotes: {double}")

# Triple quotes for multi-line
multi_line = """This is a
multi-line
string"""
print(f"Multi-line:\n{multi_line}")

# Escape sequences
escaped = "Line 1\nLine 2\tTabbed"
print(f"With escapes: {escaped}")
print()

# =============================================
# 2. STRING INDEXING
# =============================================
print("2. STRING INDEXING")

text = "Python"
print(f"Text: {text}")

print(f"First character: {text[0]}")
print(f"Second character: {text[1]}")
print(f"Last character: {text[-1]}")
print(f"Second last: {text[-2]}")

# Slicing
print(f"First three: {text[0:3]}")
print(f"From index 2: {text[2:]}")
print(f"Last three: {text[-3:]}")
print(f"Every second character: {text[::2]}")
print()

# =============================================
# 3. STRING OPERATIONS
# =============================================
print("3. STRING OPERATIONS")

str1 = "Hello"
str2 = "World"

# Concatenation
combined = str1 + " " + str2
print(f"Concatenation: {combined}")

# Repetition
repeated = "Python " * 3
print(f"Repetition: {repeated}")

# Membership
print(f"'Hello' in '{combined}': {'Hello' in combined}")
print(f"'Python' in '{combined}': {'Python' in combined}")

# Length
print(f"Length of '{text}': {len(text)}")
print()

# =============================================
# 4. STRING METHODS
# =============================================
print("4. STRING METHODS")

sample = "  python programming  "
print(f"Original: '{sample}'")

# Case conversion
print(f"Upper: '{sample.upper()}'")
print(f"Lower: '{sample.lower()}'")
print(f"Title: '{sample.title()}'")
print(f"Capitalize: '{sample.capitalize()}'")

# Whitespace handling
print(f"Stripped: '{sample.strip()}'")
print(f"Left stripped: '{sample.lstrip()}'")
print(f"Right stripped: '{sample.rstrip()}'")

# Replacement
print(f"Replace 'python' with 'Java': '{sample.replace('python', 'Java')}'")
print()
