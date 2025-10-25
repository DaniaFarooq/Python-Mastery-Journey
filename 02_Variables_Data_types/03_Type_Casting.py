"""
TYPE CONVERSION & TYPE CASTING IN PYTHON
Converting between different data types is essential for data processing.
"""

print("=== MASTERING TYPE CONVERSION IN PYTHON ===\n")

# =============================================
# 1. WHAT IS TYPE CONVERSION?
# =============================================
print("1. WHAT IS TYPE CONVERSION?")
print("   - Converting from one data type to another")
print("   - Also called 'type casting'")
print("   - Essential for data processing and calculations")
print("   - Two types: Implicit & Explicit\n")

# =============================================
# 2. IMPLICIT CONVERSION (AUTOMATIC)
# =============================================
print("2. IMPLICIT CONVERSION - PYTHON DOES IT AUTOMATICALLY")

# Integer to Float
integer_num = 5
float_num = 2.5
result = integer_num + float_num  # int → float automatically
print(f"Integer + Float: {integer_num} + {float_num} = {result}")
print(f"  Types: {type(integer_num)} + {type(float_num)} → {type(result)}")

# Boolean to Integer
true_value = True
false_value = False
num = 10
result1 = num + true_value   # True becomes 1
result2 = num + false_value  # False becomes 0
print(f"\nBoolean to Integer:")
print(f"  10 + True = {result1}  (True → 1)")
print(f"  10 + False = {result2} (False → 0)")

# =============================================
# 3. EXPLICIT CONVERSION (MANUAL)
# =============================================
print("3. EXPLICIT CONVERSION - WE DO IT MANUALLY")

# int() - Convert to integer
print("→ int() - Convert to Integer:")
number_str = "123"
number_int = int(number_str)
print(f"  int('123') = {number_int} (type: {type(number_int)})")

# float() - Convert to float
print("\n→ float() - Convert to Float:")
number_str = "3.14"
number_float = float(number_str)
print(f"  float('3.14') = {number_float} (type: {type(number_float)})")

# str() - Convert to string
print("\n→ str() - Convert to String:")
number = 100
number_str = str(number)
print(f"  str(100) = '{number_str}' (type: {type(number_str)})")

# =============================================
# 4. CONVERSION BETWEEN SEQUENCE TYPES
# =============================================
print("4. SEQUENCE TYPE CONVERSIONS")

# list() - Convert to list
print("→ list() - Convert to List:")
tuple_data = (1, 2, 3, 4, 5)
tuple_to_list = list(tuple_data)
print(f"  list((1, 2, 3, 4, 5)) = {tuple_to_list}")

# tuple() - Convert to tuple
print("\n→ tuple() - Convert to Tuple:")
list_data = [1, 2, 3, 4, 5]
list_to_tuple = tuple(list_data)
print(f"  tuple([1, 2, 3, 4, 5]) = {list_to_tuple}")

# =============================================
# 5. PRACTICAL CONVERSION EXAMPLES
# =============================================
print("5. PRACTICAL REAL-WORLD EXAMPLES")

# Example 1: User Input Processing
print("USER INPUT PROCESSING")
# Simulating user input (usually comes as string)
user_age = "25"           # From input field
user_height = "5.6"       # From input field
user_score = "95"         # From input field
# Convert to appropriate types
age_int = int(user_age)
height_float = float(user_height)
score_int = int(user_score)

print(f"Raw input - Age: '{user_age}' (type: {type(user_age)})")
print(f"Converted - Age: {age_int} (type: {type(age_int)})")
print(f"Raw input - Height: '{user_height}' (type: {type(user_height)})")
print(f"Converted - Height: {height_float} (type: {type(height_float)})")
print(f"Can vote: {age_int >= 18}")
print(f"Average: {(age_int + height_float + score_int) / 3:.2f}")
print()
# set() - Convert to set (removes duplicates)
print("\n→ set() - Convert to Set:")
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_to_set = set(list_with_duplicates)
print(f"  set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) = {list_to_set}")

# Example 2: String Manipulation with Numbers
print("STRING MANIPULATION WITH NUMBERS")
product_price = 29.99
quantity = 3
tax_rate = 0.08  # 8%

# Calculations with numbers
subtotal = product_price * quantity
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount
# Convert to strings for display
receipt = f"""
 RECEIPT
Item: Python Book
Price: ${product_price}
Quantity: {quantity}
Subtotal: ${subtotal:.2f}
Tax (8%): ${tax_amount:.2f}
Total: ${total:.2f}
"""

print(receipt)
print()

# =============================================
# 6. COMMON CONVERSION ERRORS
# =============================================
print("6. COMMON CONVERSION ERRORS")

print("❌ Error: Converting invalid string to number")
# int("hello")  # ValueError: invalid literal for int()

print("\n❌ Error: Converting None or empty values")
# int(None)  # TypeError
# int("")    # ValueError

# =============================================
# 7. TYPE CONVERSION EXERCISES
# =============================================
print("7. PRACTICE EXERCISES")

print("Exercise 1: Temperature Converter")
# Convert Celsius to Fahrenheit
celsius_str = "25"  # User input as string
celsius = float(celsius_str)
fahrenheit = (celsius * 9/5) + 32

print(f"  TEMPERATURE CONVERSION")
print(f"  Celsius: {celsius}°C")
print(f"  Fahrenheit: {fahrenheit}°F")
print(f"  Types: {type(celsius_str)} → {type(celsius)} → {type(fahrenheit)}")
print()

print("Exercise 2: String to List Processing")
# Process a string of numbers
numbers_str = "10,20,30,40,50"
# Split into list of strings, then convert to integers
numbers_list = numbers_str.split(",")
numbers_int = [int(num) for num in numbers_list]
total = sum(numbers_int)
average = total / len(numbers_int)

print(f" NUMBER PROCESSING")
print(f"  Input string: '{numbers_str}'")
print(f"  Split list: {numbers_list}")
print(f"  Integer list: {numbers_int}")
print(f"  Total: {total}, Average: {average:.1f}")
print()
