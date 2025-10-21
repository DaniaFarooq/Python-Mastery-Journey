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

# =============================================
# 4. COMBINING ESCAPE SEQUENCES
# =============================================
print("4. COMBINING MULTIPLE ESCAPE SEQUENCES")

# Table formatting
print("EMPLOYEE DIRECTORY")
print("=" * 40)
print("Name\t\tDepartment\t\tEmail")
print("----\t\t----------\t\t-----")
print("Alice\t\tEngineering\t\talice@company.com")
print("Bob\t\tMarketing\t\tbob@company.com")
print("Charlie\t\tSales\t\t\tcharlie@company.com")
print()

# Formatted address
print("ADDRESS FORMATTING:")
address = "123 Main Street\\nSuite 4B\\nPythonville, PY 12345"
print("Formatted Address:")
print(address)
print()

# =============================================
# 5. ESCAPE SEQUENCES IN USER INPUT
# =============================================
print("5. HANDLING ESCAPE SEQUENCES IN INPUT")

# Example: Processing user input with potential escapes
user_input = "Hello\\nWorld\\tTabbed"
print(f"User input: {user_input}")
print(f"Interpreted: {user_input}")  # Shows as literal
print()

# =============================================
# 6. INTERACTIVE EXERCISES
# =============================================
print("6. PRACTICE EXERCISES")

print("Exercise 1: Create a formatted receipt")
# Your code here:
print("🛍️  SUPERMARKET RECEIPT")
print("=" * 30)
print("Item\t\tPrice\tQty\tTotal")
print("----\t\t-----\t---\t-----")
print("Apple\t\t$1.20\t3\t$3.60")
print("Bread\t\t$2.50\t1\t$2.50")
print("Milk\t\t$3.00\t2\t$6.00")
print("=" * 30)
print("Total:\t\t\t\t$12.10")
print()

print("Exercise 2: Display a multi-line poem")
# Your code here:
poem = """Roses are red,\nViolets are blue,\nPython is awesome,\nAnd so are you!"""
print("📜 POEM:")
print(poem)
print()

print("🎉 FANTASTIC! You've mastered Escape Sequences!")
print("You can now format text like a pro!")
