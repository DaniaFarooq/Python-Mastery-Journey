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

# =============================================
# 3. NUMERIC TYPES
# =============================================
print("3. NUMERIC TYPES")

# Integer (int) - whole numbers
age = 25
score = -100
print("→ Integers (int):")
print(f"age: {age} (type: {type(age)})")
print(f"score: {score} (type: {type(score)})")

# Float (float) - decimal numbers
price = 19.99
temperature = -5.5
scientific = 2.5e3  # 2.5 × 10³ = 2500.0

print("\n→ Floats (float):")
print(f"price: {price} (type: {type(price)})")
print(f"temperature: {temperature} (type: {type(temperature)})")
print(f"scientific: {scientific} (type: {type(scientific)})")

# Complex (complex) - imaginary numbers
complex_num = 3 + 4j
another_complex = 2j

print("\n→ Complex (complex):")
print(f"complex_num: {complex_num} (type: {type(complex_num)})")
print(f"another_complex: {another_complex} (type: {type(another_complex)})")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")
print()
