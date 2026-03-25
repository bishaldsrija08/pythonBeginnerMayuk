import matplotlib.pyplot as plt
# Student grades dictionary

student_grades = { # key: value pair
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 90,
    'Eve': 88,
    'Frank': 95,
    'Grace': 80,
    'Heidi': 91,
    'Ivan': 87
    }

# names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan"]
# grades = [85, 92, 78, 90, 88, 95, 80, 91, 87]

names = list(student_grades.keys())
grades = list(student_grades.values())

# Create a bar chart
plt.bar(names, grades, color='blue')
plt.xlabel('Students')
plt.ylabel('Grades')
plt.title('Student Grades')
plt.show()