# basics_concepts.py
# Day 4 - OOP + File Handling + Error Handling (Concept Practice)

# =========================
# 1. CLASS & OBJECT
# =========================

class Student:
    school = "NHCE"  # class variable

    def __init__(self, name, marks):
        self.name = name      # instance variable
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Priyanka", [80, 90, 85])
print("Average:", s1.average())


# =========================
# 2. INHERITANCE
# =========================

class Person:
    def greet(self):
        print("Hello from Person")


class Child(Student, Person):
    pass


c = Child("Asha", [70, 75, 80])
c.greet()


# =========================
# 3. FILE HANDLING
# =========================

# Writing to file
with open("sample.txt", "w") as f:
    f.write("Hello, this is file handling.")

# Reading from file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File Content:", content)


# =========================
# 4. JSON HANDLING
# =========================

import json

data = {"name": "Priyanka", "marks": [80, 90]}

# Write JSON
with open("sample.json", "w") as f:
    json.dump(data, f)

# Read JSON
with open("sample.json", "r") as f:
    loaded = json.load(f)
    print("JSON Data:", loaded)


# =========================
# 5. ERROR HANDLING
# =========================

# ValueError example
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid number!")

# FileNotFoundError example
try:
    with open("missing.txt", "r") as f:
        f.read()
except FileNotFoundError:
    print("File not found!")

# TypeError example
try:
    result = "2" + 3
except TypeError:
    print("Type error occurred!")

# finally block
try:
    x = 10
finally:
    print("This always runs.")


# =========================
# 6. PYTHONIC IMPROVEMENT
# =========================

marks = [10, 20, 30]

# Normal way
if len(marks) > 0:
    print("Has values")

# Pythonic way
if marks:
    print("Pythonic: Has values")
