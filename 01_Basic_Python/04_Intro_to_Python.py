"""
INTRODUCTION TO PYTHON 🐍
A comprehensive beginner's guide to Python programming
"""

print("=== WELCOME TO PYTHON PROGRAMMING! ===\n")

# =============================================
# 1. WHAT IS PYTHON?
# =============================================
print("1. WHAT IS PYTHON?")
print("   - High-level, interpreted programming language")
print("   - Known for simplicity and readability")
print("   - Perfect for beginners and professionals")
print("   - Used in: Web Dev, Data Science, AI, Automation\n")

# =============================================
# 2. WHY PYTHON FOR DATA SCIENCE?
# =============================================
print("2. WHY PYTHON FOR DATA SCIENCE?")
print("   ✓ Easy to learn - reads like English")
print("   ✓ Versatile - multiple applications")
print("   ✓ Large community support")
print("   ✓ Industry standard (Google, NASA, Netflix)\n")

# =============================================
# 3. PYTHON FEATURES DEMONSTRATION
# =============================================
print("3. PYTHON FEATURES IN ACTION")

# Feature 1: Interpreted Language - run directly
print("   → Interpreted: No compilation needed")
print("     Just write code and run!\n")

# Feature 2: Dynamic Typing
print("   → Dynamic Typing: No type declarations")
name = "Dania"      # Python knows it's string
age = 25            # Python knows it's integer
height = 5.6        # Python knows it's float
is_learning = True  # Python knows it's boolean

print(f"     name = {name} (type: {type(name)})")
print(f"     age = {age} (type: {type(age)})")
print(f"     height = {height} (type: {type(height)})")
print(f"     is_learning = {is_learning} (type: {type(is_learning)})\n")

# Feature 3: Cross-Platform
print("   → Cross-Platform: Works on Windows, Mac, Linux")
print("     Same code runs everywhere!\n")

# =============================================
# 4. BASIC SYNTAX RULES
# =============================================
print("4. BASIC SYNTAX RULES")

# Rule 1: Indentation Matters
print("   → Indentation: Uses 4 spaces (no tabs mixing)")
if True:
    print("     This is properly indented")
    print("     This block belongs to the if statement")

# Rule 2: Case Sensitivity
Name = "Dania"
name = "Farooq"
NAME = "Python"
print(f"\n   → Case Sensitivity:")
print(f"     Name = {Name}, name = {name}, NAME = {NAME}")

# Rule 3: Comments
print("\n   → Comments: Use # for single line")
print("     ''' for multi-line comments '''")

# =============================================
# 5. COMPREHENSIVE PYTHON DEMO
# =============================================
print("\n5. COMPREHENSIVE PYTHON DEMO")
print("=" * 40)

# 5.1 Personal Learning Tracker
print("\n PERSONAL LEARNING TRACKER")
student_name = "Data Science Student"
months_learning = 3
daily_practice_hours = 2.5
total_hours = months_learning * 30 * daily_practice_hours

print(f"   Student: {student_name}")
print(f"   Months learning: {months_learning}")
print(f"   Daily practice: {daily_practice_hours} hours")
print(f"   Total practice: {total_hours} hours! ")

# 5.2 String Operations Showcase
print("\n STRING OPERATIONS")
message = "python programming is amazing"
print(f"   Original: {message}")
print(f"   Title Case: {message.title()}")
print(f"   UPPERCASE: {message.upper()}")
print(f"   Capitalized: {message.capitalize()}")
print(f"   Length: {len(message)} characters")

# 5.3 Math Operations
print("\n MATH OPERATIONS")
a, b = 15, 4
print(f"   {a} + {b} = {a + b}")
print(f"   {a} - {b} = {a - b}")
print(f"   {a} * {b} = {a * b}")
print(f"   {a} / {b} = {a / b:.2f}")  # 2 decimal places
print(f"   {a} % {b} = {a % b}")     # Modulus
print(f"   {a} ** {b} = {a ** b}")   # Exponentiation

# 5.4 User Interaction
print("\n INTERACTIVE DEMO")
try:
    user_topic = input("   What Python topic excites you most? ")
    print(f"   Great choice! '{user_topic}' is fascinating! 🌟")
except:
    print("   (Input skipped - running in non-interactive mode)")

# 5.5 Boolean Logic
print("\n🔍 BOOLEAN LOGIC")
python_is_easy = True
requires_practice = True
is_fun = True

print(f"   Python is easy: {python_is_easy}")
print(f"   Requires practice: {requires_practice}")
print(f"   Is fun: {is_fun}")
print(f"   All true? {python_is_easy and requires_practice and is_fun}")

# =============================================
# 6. REAL-WORLD APPLICATIONS
# =============================================
print("\n6. REAL-WORLD APPLICATIONS")
print("    Data Science: pandas, numpy, matplotlib")
print("    Artificial Intelligence: TensorFlow, PyTorch")
print("    Web Development: Django, Flask")
print("    Automation: File processing, web scraping")
print("    Game Development: Pygame")
print("    Mobile Apps: Kivy, BeeWare")

# =============================================
# 7. SUCCESS TIPS
# =============================================
print("\n7. SUCCESS TIPS FOR BEGINNERS")
tips = [
    "💡 Practice daily (consistency > intensity)",
    "💡 Build small projects weekly", 
    "💡 Read others' code to learn",
    "💡 Don't memorize - understand concepts",
    "💡 Use official Python documentation",
    "💡 Join Python communities for support",
    "💡 Celebrate small victories!"
]

for tip in tips:
    print(f"   {tip}")

# Bonus: Run this script (as instructed in previous lesson) to see Python in action!
