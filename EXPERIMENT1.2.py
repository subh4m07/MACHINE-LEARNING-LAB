import pandas as pd

students = pd.DataFrame({
    "Student_Name": ["Pawan", "Ravi", "binod", "vicky", "akash"],
    "Roll_Number": [101, 102, 103, 104, 105],
    "Marks": [56, 67, 89, 78, 34],
    "Attendance": [67, 34, 89, 23, 90]
})

print("Complete Student Details")
print(students)

selected = students.loc[students["Marks"] > 80]

print("\nStudents with marks above 80")
print(selected)