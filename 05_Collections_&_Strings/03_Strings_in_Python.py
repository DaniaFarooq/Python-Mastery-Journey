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
