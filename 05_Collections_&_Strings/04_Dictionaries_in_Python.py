"""
DICTIONARIES IN PYTHON
Key-value pairs for storing and organizing data
"""

print("=== DICTIONARIES IN PYTHON ===\n")

# =============================================
# 1. CREATING DICTIONARIES
# =============================================
print("1. CREATING DICTIONARIES")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(f"Person: {person}")

# Using dict() constructor
student = dict(name="Bob", age=22, grade="A")
print(f"Student: {student}")

# Mixed data types
mixed_dict = {
    "string": "hello",
    "number": 42,
    "boolean": True,
    "list": [1, 2, 3]
}
print(f"Mixed dictionary: {mixed_dict}")
print()
