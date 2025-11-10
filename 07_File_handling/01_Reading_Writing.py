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

# =============================================
# 6. WORKING WITH MULTIPLE FILES
# =============================================
print("6. WORKING WITH MULTIPLE FILES")

# Create multiple data files
print("→ Creating project structure:")

# Data file 1: Courses
courses = ["Python Basics", "Data Science", "Web Development", "Machine Learning"]
with open("courses.txt", "w") as file:
    for course in courses:
        file.write(course + "\n")

# Data file 2: Skills  
skills = ["Programming", "Problem Solving", "Data Analysis", "Communication"]
with open("skills.txt", "w") as file:
    for skill in skills:
        file.write(skill + "\n")

print("✓ Created courses.txt and skills.txt")

# Read and combine data from multiple files
print("\n→ Combined learning plan:")
with open("courses.txt", "r") as courses_file, open("skills.txt", "r") as skills_file:
    courses = [line.strip() for line in courses_file]
    skills = [line.strip() for line in skills_file]
    
    for i, (course, skill) in enumerate(zip(courses, skills), 1):
        print(f"  {i}. Learn {course} → Develop {skill}")
print()

# =============================================
# 7. EXERCISES
# =============================================
print("7. PRACTICE EXERCISES")

print("Exercise 1: Create a Personal Notes File")
notes = [
    "Python is versatile and powerful",
    "File handling is essential for data persistence", 
    "Practice regularly to improve skills",
    "Build projects to apply knowledge"
]

with open("my_notes.txt", "w") as file:
    file.write("MY PROGRAMMING NOTES\n")
    file.write("=" * 20 + "\n")
    for note in notes:
        file.write(f"• {note}\n")

print("✓ Created personal notes file")

print("\nExercise 2: Read and Analyze File")
with open("my_notes.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
    line_count = content.count('\n') + 1
    
print(f"File analysis:")
print(f"  Words: {word_count}")
print(f"  Lines: {line_count}")

print("\nExercise 3: Update Learning Goals")
new_goals = [
    "Master Python OOP concepts",
    "Learn web framework (Django/Flask)",
    "Build a portfolio project",
    "Contribute to open source"
]

with open("goals.txt", "w") as file:
    file.write("FUTURE LEARNING GOALS\n")
    file.write("=" * 25 + "\n")
    for i, goal in enumerate(new_goals, 1):
        file.write(f"{i}. {goal}\n")

print("✓ Created learning goals file")
print()

# =============================================
# 8. FILE HANDLING BEST PRACTICES
# =============================================
print("8. BEST PRACTICES")

print("✓ Always use 'with' statement for automatic closing")
print("✓ Handle exceptions for missing files")
print("✓ Use meaningful file names")
print("✓ Organize files in proper directories")
print("✓ Backup important data regularly")
print("✓ Use appropriate file modes")
print("✓ Close files properly when not using 'with'")

print("\n" + "="*70)
print("🎉 OUTSTANDING! You've mastered File Handling in Python! 🎉")
print("You've successfully completed the Python Basics curriculum!")
print("From variables to functions to file handling - you've built a solid foundation!")
print("Ready to tackle the Practice Zone and advanced topics! 🌟")
print("✨" * 50)
