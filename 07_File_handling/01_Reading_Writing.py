"""
FILE HANDLING IN PYTHON
Reading from and writing to files
"""

print("=== FILE HANDLING IN PYTHON ===\n")

# =============================================
# 1. WRITING TO FILES
# =============================================
print("1. WRITING TO FILES")

# Write to a new file
print("→ Creating and writing to a new file:")
with open("learning_journal.txt", "w") as file:
    file.write("My Python Learning Journal\n")
    file.write("Today I learned about file handling!\n")
   
print("✓ Created 'learning_journal.txt' with content")

# Append to existing file
print("\n→ Appending to the file:")
with open("learning_journal.txt", "a") as file:
    file.write("Appended: Practice makes perfect!\n")
    file.write("Next goal: Master data structures.\n")

print("✓ Appended new content to the file")
print()

# =============================================
# 2. READING FROM FILES
# =============================================
print("2. READING FROM FILES")

# Read entire file
print("→ Reading entire file:")
with open("learning_journal.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Read line by line
print("→ Reading line by line:")
with open("learning_journal.txt", "r") as file:
    print("Each line:")
    for line in file:
        print(f"  {line.strip()}")
print()

# =============================================
# 3. FILE MODES EXPLAINED
# =============================================
print("3. FILE MODES")

print("✓ 'r' - Read mode (default)")
print("✓ 'w' - Write mode (creates new file)")
print("✓ 'a' - Append mode (adds to existing)")
print("✓ 'x' - Create mode (fails if file exists)")
print("✓ 'b' - Binary mode (for images, etc.)")
print("✓ 't' - Text mode (default)")
print()

# =============================================
# 4. PRACTICAL EXAMPLE
# =============================================
print("4. PRACTICAL EXAMPLE")

# Example : Student Records
print("STUDENT RECORDS SYSTEM:")

# Write student data
students = [
    "Alice,20,Computer Science",
    "Bob,22,Data Science", 
    "Charlie,21,AI Engineering"
]

with open("students.csv", "w") as file:
    file.write("Name,Age,Major\n")
    for student in students:
        file.write(student + "\n")
print("✓ Created students.csv file")

# Read and display student data
print("\n→ Student records:")
with open("students.csv", "r") as file:
    for line in file:
        name, age, major = line.strip().split(",")
        print(f"  {name}: {age} years, {major}")

# =============================================
# 5. ERROR HANDLING WITH FILES
# =============================================
print("5. ERROR HANDLING")

# Safe file reading with try-except
print("→ Safe file operations:")

def read_safe(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except Exception as e:
        return f"Error: {str(e)}"

# Test with existing and non-existing files
result1 = read_safe("learning_journal.txt")
result2 = read_safe("nonexistent.txt")

print("Existing file: Read successfully!")
print("Non-existing file: Handled gracefully")
print()
