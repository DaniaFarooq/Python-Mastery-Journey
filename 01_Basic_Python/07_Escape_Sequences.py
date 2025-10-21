"""
ESCAPE SEQUENCES IN PYTHON
Special characters that allow you to format strings and use special symbols.
"""

print("=== MASTERING ESCAPE SEQUENCES IN PYTHON ===\n")

# =============================================
# 1. WHAT ARE ESCAPE SEQUENCES?
# =============================================
print("1. WHAT ARE ESCAPE SEQUENCES?")
print("   Special combinations starting with backslash \\")
print("   Used to represent characters that are hard to type")
print("   Or to format text in specific ways\n")

# =============================================
# 2. COMMON ESCAPE SEQUENCES
# =============================================
print("2. COMMON ESCAPE SEQUENCES DEMONSTRATION")

# Newline: \n
print("→ Newline (\\n):")
print("Line 1\nLine 2\nLine 3")
print()

# Tab: \t
print("→ Tab (\\t):")
print("Name:\tDania")
print("Age:\t25")
print("City:\tPythonville")
print()

# Backslash: \\
print("→ Backslash (\\\\):")
print("File path: C:\\\\Users\\\\Dania\\\\Documents")
print("Regular expression: \\\\d+")
print()

# Quotes: \" and \'
print("→ Quotes (\\\" and \\'):")
print("She said, \"Hello World!\"")
print('He replied, \'Python is awesome!\'')
print("It's a beautiful day!")
print()

# Backspace: \b
print("→ Backspace (\\b):")
print("Hello\b\b\bHey")  # Removes 'llo', adds 'Hey'
print("Python\b\b\b\b1234")  # Removes 'thon', adds '1234'
print()

# =============================================
# 3. PRACTICAL EXAMPLES
# =============================================
print("3. PRACTICAL REAL-WORLD EXAMPLES")

# Example 1: File paths
print("FILE PATHS:")
print("Windows path: C:\\\\Users\\\\Dania\\\\python_scripts\\\\main.py")
print("Unix path: /home/dania/python_scripts/main.py")
print()

# Example 2: JSON-like output
print("FORMATTED DATA OUTPUT:")
print("{\n\t\"name\": \"Dania\",\n\t\"age\": 25,\n\t\"city\": \"Pythonville\"\n}")
print()
