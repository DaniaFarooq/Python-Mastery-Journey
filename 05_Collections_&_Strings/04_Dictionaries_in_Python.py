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

# =============================================
# 2. ACCESSING VALUES
# =============================================
print("2. ACCESSING VALUES")

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "year": 2024,
    "pages": 350
}

print(f"Book: {book}")

# Access with get() method
print(f"Year: {book.get('year')}")
print(f"Publisher: {book.get('publisher', 'Not specified')}")

# Get all keys and values
print(f"Keys: {list(book.keys())}")
print(f"Values: {list(book.values())}")
print(f"Items: {list(book.items())}")
print()
# Access with square brackets
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
