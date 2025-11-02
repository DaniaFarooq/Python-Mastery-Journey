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

# =============================================
# 5. MORE STRING METHODS
# =============================================
print("5. MORE STRING METHODS")

text = "Python is awesome!"
print(f"Text: '{text}'")

# Checking methods
print(f"Starts with 'Python': {text.startswith('Python')}")
print(f"Ends with 'awesome!': {text.endswith('awesome!')}")
print(f"Is alphabetic: {'Python'.isalpha()}")
print(f"Is numeric: {'123'.isdigit()}")
print(f"Is alphanumeric: {'Python123'.isalnum()}")

# Finding and counting
print(f"Find 'is': {text.find('is')}")
print(f"Count 'o': {text.count('o')}")

# =============================================
# 6. STRING FORMATTING
# =============================================
print("6. STRING FORMATTING")

name = "Alice"
age = 25
score = 95.5

# f-strings (Python 3.6+)
message1 = f"{name} is {age} years old and scored {score}"
print(f"f-string: {message1}")

# format() method
message2 = "{} is {} years old and scored {}".format(name, age, score)
print(f"format(): {message2}")

# =============================================
# 7. PRACTICAL EXAMPLES
# =============================================
print("7. PRACTICAL EXAMPLES")

# Example 1: User Input Processing
print("USER INPUT PROCESSING:")
username = "  python_user  "
clean_username = username.strip().lower()
print(f"Original: '{username}'")
print(f"Cleaned: '{clean_username}'")

# Example 2: Email Validation
print("\nEMAIL VALIDATION:")
email = "user@example.com"
print(f"Email: {email}")
print(f"Valid email: {'@' in email and '.' in email}")
print(f"Domain: {email.split('@')[1]}")

# =============================================
# 8. STRING ESCAPE SEQUENCES
# =============================================
print("8. STRING ESCAPE SEQUENCES")

print("Newline: Line 1\\nLine 2")
print("Tab: Name\\tAge")
print("Backslash: C:\\\\Users")
print("Quote: She said, \\\"Hello!\\\"")
print("Raw string: r\"C:\\\\Users\"")
print()

# =============================================
# 9. EXERCISES
# =============================================
print("9. EXERCISES")

print("Exercise 1: Name Formatter")
name = "john doe"
formatted = name.title()
print(f"Original: {name}")
print(f"Formatted: {formatted}")

print("\nExercise 2: Palindrome Checker")
word = "radar"
is_palindrome = word == word[::-1]
print(f"'{word}' is palindrome: {is_palindrome}")

# =============================================
# 10. ADVANCED STRING OPERATIONS
# =============================================
print("10. ADVANCED STRING OPERATIONS")

# String reversal
text = "Python"
reversed_text = text[::-1]
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

# Checking prefixes/suffixes
filename = "document.pdf"
print(f"Filename: {filename}")
print(f"Is PDF: {filename.endswith('.pdf')}")
print(f"Is document: {filename.startswith('document')}")

# =============================================
# 11. STRING PROPERTIES
# =============================================
print("11. STRING PROPERTIES")

print("✓ Immutable - cannot be changed after creation")
print("✓ Ordered - characters maintain their position")
print("✓ Indexable - can access characters by position")
print("✓ Iterable - can loop through characters")
print("✓ Supports slicing - extract substrings easily")

print("\n" + "="*65)
print("PHENOMENAL! You've mastered Strings in Python!")
