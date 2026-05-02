# manager.py
# Main program for Student Grade Manager

import json
from student import Student

FILE_NAME = "data.json"


# Load students from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Student(s["name"], s["grades"]) for s in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠ Error reading file. Starting fresh.")
        return []


# Save students to file
def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump([s.to_dict() for s in students], file, indent=4)
    except Exception as e:
        print("⚠ Error saving data:", e)


# Add student
def add_student(students):
    try:
        name = input("Enter student name: ").strip()
        grades = list(map(int, input("Enter grades (space separated): ").split()))

        students.append(Student(name, grades))
        print("✅ Student added successfully!")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")


# View students
def view_students(students):
    if not students:
        print("📭 No students found.")
        return

    print("\n📊 Student Records:")
    for s in students:
        print(f"{s.name} | Grades: {s.grades} | Avg: {s.average():.2f}")


# Main program
def main():
    students = load_students()

    while True:
        print("\n===== Student Grade Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            save_students(students)
            print("💾 Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
