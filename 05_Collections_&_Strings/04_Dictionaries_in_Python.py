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

# =============================================
# 3. MODIFYING DICTIONARIES
# =============================================
print("3. MODIFYING DICTIONARIES")

car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022
}
print(f"Original car: {car}")

# Add new key-value pair
car["color"] = "blue"
print(f"After adding color: {car}")

# Update existing value
car["year"] = 2023
print(f"After updating year: {car}")

# Update multiple values
car.update({"model": "Corolla", "price": 25000})
print(f"After update: {car}")

# Remove items
removed_value = car.pop("price")
print(f"After pop('price'): {car}, removed: {removed_value}")

del car["color"]
print(f"After del car['color']: {car}")

# Clear dictionary
car.clear()
print(f"After clear(): {car}")
print()

# =============================================
# 4. DICTIONARY OPERATIONS
# =============================================
print("4. DICTIONARY OPERATIONS")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Copy dictionary
dict_copy = dict1.copy()
print(f"Original: {dict1}")
print(f"Copy: {dict_copy}")

# Merge dictionaries
dict1.update(dict2)
print(f"After update with dict2: {dict1}")

# Membership testing
print(f"'a' in dict1: {'a' in dict1}")
print(f"'z' in dict1: {'z' in dict1}")

# Length
print(f"Length of dict1: {len(dict1)}")
print()

# =============================================
# 5. LOOPING THROUGH DICTIONARIES
# =============================================
print("5. LOOPING THROUGH DICTIONARIES")

inventory = {
    "apples": 10,
    "bananas": 15,
    "oranges": 8,
    "grapes": 20
}

print("Loop through keys:")
for key in inventory:
    print(f"  {key}: {inventory[key]}")

print("\nLoop through values:")
for value in inventory.values():
    print(f"  {value}")

print("\nLoop through items:")
for key, value in inventory.items():
    print(f"  {key}: {value}")
print()

# =============================================
# 6. NESTED DICTIONARIES
# =============================================
print("6. NESTED DICTIONARIES")

company = {
    "employee1": {
        "name": "Alice",
        "age": 30,
        "position": "Developer"
    },
    "employee2": {
        "name": "Bob",
        "age": 25,
        "position": "Designer"
    }
}
print("Company employees:")
for emp_id, details in company.items():
    print(f"  {emp_id}:")
    print(f"    Name: {details['name']}")
    print(f"    Age: {details['age']}")
    print(f"    Position: {details['position']}")

# Access nested values
print(f"Employee1 name: {company['employee1']['name']}")
print(f"Employee2 position: {company['employee2']['position']}")
print()
