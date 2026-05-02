# student.py
# Defines the Student class

class Student:
    school_name = "NHCE"  # class variable

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "name": self.name,
            "grades": self.grades
        }
