import pandas as pd

students = pd.DataFrame({
    "Student_Name": ["Pawan", "Ravi", "binod", "vicky", "akash"],
    "Roll_Number": [101, 102, 103, 104, 105],
    "Marks": [56, 67, 89, 78, 34],
    "Attendance": [67, 34, 89, 23, 90]
})

grades = []

for mark in students["Marks"]:
    if mark >= 90:
        grades.append("A")
    elif mark >= 80:
        grades.append("B")
    elif mark >= 70:
        grades.append("C")
    else:
        grades.append("D")

students["Grade"] = grades

print("Student Details with Grades:")
print(students)