import csv
from student import Student

students = []
for i in range (3):
    name = input("Name: ")
    dorm = input("Dorm: ")
    students.append(Student(name,dorm))
file = open("students.csv", "w")
s = csv.writer(file)
for student in students:
    s.writerow((student.name,student.dorm))
file.close()
