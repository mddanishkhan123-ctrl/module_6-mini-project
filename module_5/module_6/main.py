import json
import csv
import os
from datetime import datetime

JSON_FILE = "students.json"
CSV_FILE = "students.csv"
LOG_FILE = "activity_log.txt"

def load_students():
    if not os.path.exists(JSON_FILE):
        return {}

    try:
        with open(JSON_FILE, "r") as file:
            students = json.load(file)

        if not isinstance(students, dict):
            print("Invalid student data in JSON file.")
            return None

        return students

    except json.JSONDecodeError:
        print("Invalid JSON file. Please correct it before continuing.")
        return None

def save_students(students):
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)

def log_activity(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(time + " - " + message + "\n")

def add_student(students):
    student_id = input("Student ID: ")

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Name: ")
    department = input("Department: ")

    marks = {}

    for subject in ["Python", "Maths", "DBMS"]:
        while True:
            try:
                mark = float(input(subject + " marks: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter numeric marks.")

    students[student_id] = {
        "name": name,
        "department": department,
        "marks": marks
    }

    save_students(students)
    log_activity("Added student " + student_id)

    print("Record saved to students.json.")

def search_student(students):
    student_id = input("Enter student ID: ")

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("Student ID:", student_id)
    print("Name:", student["name"])
    print("Department:", student["department"])

    for subject, mark in student["marks"].items():
        print(subject + ":", mark)

def display_students(students):
    if not students:
        print("No student records found.")
        return

    for student_id, student in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", student["name"])
        print("Department:", student["department"])

        for subject, mark in student["marks"].items():
            print(subject + ":", mark)

def export_csv(students):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student ID", "Name", "Department",
            "Python", "Maths", "DBMS"
        ])

        for student_id, student in students.items():
            marks = student["marks"]

            writer.writerow([
                student_id,
                student["name"],
                student["department"],
                marks["Python"],
                marks["Maths"],
                marks["DBMS"]
            ])

    log_activity("Exported student records to CSV")
    print("CSV export completed:", CSV_FILE)

def read_log():
    try:
        with open(LOG_FILE, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

def read_first_log_line():
    try:
        with open(LOG_FILE, "r") as file:
            return file.readline()
    except FileNotFoundError:
        return ""

def read_all_log_lines():
    try:
        with open(LOG_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def json_string_demo(students):
    if students:
        student_id = next(iter(students))

        json_text = json.dumps(students[student_id])
        student_data = json.loads(json_text)

        return student_data

def write_log_lines():
    lines = [
        "Student Records System\n",
        "Activity log\n"
    ]

    with open(LOG_FILE, "a") as file:
        file.writelines(lines)

def main():
    students = load_students()

    if students is None:
        return

    while True:
        print("\n===== STUDENT RECORDS SYSTEM =====")
        print("1. Add student")
        print("2. Search student")
        print("3. Display all students")
        print("4. Export records to CSV")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            display_students(students)

        elif choice == "4":
            export_csv(students)

        elif choice == "0":
            break

        else:
            
    
            print("Invalid choice.")


if __name__ == "__main__":
    main()