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
