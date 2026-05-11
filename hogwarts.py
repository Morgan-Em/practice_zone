students = [
    {"name": "Hermione", "house": "Gryfffindor", "patronous": "Otter"},
    {"name": "Harry", "house": "Gryfffindor", "patronous": "Stag"},
    {"name": "Ron", "house": "Gryfffindor", "patronous": "Jack Rusell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", " )