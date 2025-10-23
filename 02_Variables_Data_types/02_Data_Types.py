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

# =============================================
# 4. BOOLEAN TYPE
# =============================================
print("4. BOOLEANS (bool) - TRUE/FALSE")

is_python_fun = True
is_learning = False
result = 10 > 5  # This evaluates to True

print(f"is_python_fun: {is_python_fun} (type: {type(is_python_fun)})")
print(f"is_learning: {is_learning} (type: {type(is_learning)})")
print(f"10 > 5: {result} (type: {type(result)})")

# Boolean conversion
print("\n→ Boolean Conversion:")
print(f"bool(0): {bool(0)}")           # False
print(f"bool(1): {bool(1)}")           # True
print(f"bool(''): {bool('')}")         # False (empty string)
print(f"bool('Hello'): {bool('Hello')}") # True (non-empty string)
print(f"bool([]): {bool([])}")         # False (empty list)
print(f"bool([1,2]): {bool([1,2])}")   # True (non-empty list)
print()

# =============================================
# 5. SEQUENCE TYPES (INTRODUCTION)
# =============================================
print("5. SEQUENCE TYPES (BASIC INTRODUCTION)")

# List - mutable, ordered collection
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

print("→ Lists (list) - Mutable:")
print(f"fruits: {fruits} (type: {type(fruits)})")
print(f"numbers: {numbers} (type: {type(numbers)})")
print(f"mixed: {mixed} (type: {type(mixed)})")

# Tuple - immutable, ordered collection
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (5,)  # Comma required for single item

print("\n→ Tuples (tuple) - Immutable:")
print(f"coordinates: {coordinates} (type: {type(coordinates)})")
print(f"colors: {colors} (type: {type(colors)})")
print(f"single_item: {single_item} (type: {type(single_item)})")

# =============================================
# 6. MAPPING TYPE: DICTIONARY
# =============================================
print("6. DICTIONARIES (dict) - KEY-VALUE PAIRS")

# Dictionary - unordered, key-value pairs
person = {
    "name": "Dania",
    "age": 25,
    "city": "Pythonville",
    "is_student": True
}

scores = {
    "math": 95,
    "science": 88,
    "english": 92
}
print("→ Dictionaries (dict):")
print(f"person: {person} (type: {type(person)})")
print(f"scores: {scores} (type: {type(scores)})")
print(f"Person's name: {person['name']}")
print(f"Math score: {scores['math']}")
print()
