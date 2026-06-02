students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student.append(f"{name} is in {house}")


for students in sorted(students):
    print(student)