# Task 1: Dictionary of Student Marks

# Step 1: Create a dictionary with student names and marks
student_marks = {
    "Amit": 85,
    "Muskan": 92,
    "Rahul": 78,
    "Priya": 88,
    "Sneha": 95
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show not found message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"Student '{name}' not found in the record.")
