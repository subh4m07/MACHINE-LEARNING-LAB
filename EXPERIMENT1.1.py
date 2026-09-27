import numpy as np

student_marks = np.array([62, 95, 97, 69, 77, 78, 90, 74, 49, 83])

average = np.mean(student_marks)
middle_value = np.median(student_marks)
spread = np.std(student_marks)
highest = np.max(student_marks)
lowest = np.min(student_marks)

print("Student Marks:", student_marks)
print("Mean =", average)
print("Median =", middle_value)
print("Standard Deviation =", spread)
print("Maximum Marks =", highest)
print("Minimum Marks =", lowest)

