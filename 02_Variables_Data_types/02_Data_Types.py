"""
DATA TYPES IN PYTHON
Data types define the type of data a variable can hold.
Python has several built-in data types for different purposes.
"""

print("=== MASTERING DATA TYPES IN PYTHON ===\n")

# =============================================
# 1. BUILT-IN DATA TYPES OVERVIEW
# =============================================
print("1. PYTHON BUILT-IN DATA TYPES")
print("   - Text: str (string)")
print("   - Numeric: int, float, complex")
print("   - Boolean: bool (True/False)")
print("   - Sequence: list, tuple, range")
print("   - Mapping: dict")
print("   - Set: set, frozenset")
print("   - Binary: bytes, bytearray, memoryview")
print("   - None: NoneType\n")

# =============================================
# 2. TEXT TYPE: STRINGS
# =============================================
print("2. STRINGS (str) - TEXT DATA")

# Creating strings
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This can span
multiple lines"""
f_string = f"Formatted: {single_quotes} {double_quotes}"

print(f"Single quotes: {single_quotes}")
print(f"Double quotes: {double_quotes}")
print(f"Triple quotes: {triple_quotes}")
print(f"F-string: {f_string}")
print(f"Type: {type(single_quotes)}")
print()
