import os
from student import Student
from report import load_goods, save_goods

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add_students(students):
    name = input("Enter your name: ").strip().title()
    try:
        number = int(input("How many subjects do you wish to enter (1 - 6) "))
    except ValueError:
        print("Invalid score input. Please enter a valid number")
        return

    subjects_scores = {}

    for subjects in range(number):
        subject = input(f"Enter subject #{subjects+1}: ").strip().title()
        score_input = input(f"Enter score for {subject}: ").strip()

        try:
            score = float(score_input)
            subjects_scores[subject] = score
        except ValueError:
            print("Invalid score input. Please enter a valid number")
    student = Student(name, subjects_scores)
    students.append(student)
    print(f'\nStudent "{name}" added successfully')

def view_students(students):
    if not students:
        print(f'No students found.')
        return
    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name: {student.name}")
        print("Subjects and Scores:")
        for subject, score in student.subjects_scores.items():
            print(f" {subject}: {score}")
        print(f"Average: {student.average:.2f}")
        print(f"Grade: {student.grade}")

def update_students(students):
    name = input("Enter student name to update: ").strip().title()

    for student in students:
        if student.name == name:
            subject = input("Enter subject to update: ").strip().title()
            if subject in student.subjects_scores:
                try:
                    new_score = float(input(f"Enter new score for {subject}: ").strip())
                    student.subjects_scores[subject] = new_score
                    student.calculate_average_and_grade()
                    print("Score updated successfully.")
                    return
                except ValueError:
                    print("Invalid number entered.")
                    return
            else:
                print("Subject not found.")
                return
    print("Student not found.")

students = load_goods()
while True:
    print("\n---- Report Card Records ----")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Update Student")
    print("4. Save & Exit\n")
    choice = input("Enter your choice (1 - 4) ").strip()

    if choice == '1':
        add_students(students)

    elif choice == '2':
        view_students(students)

    elif choice == '3':
        update_students(students)

    elif choice == '4':
        save_goods(students)
        print("Records saved! Goodbye.\n")
        break
    else:
        print("Please enter a valid number between 1 and 4.")
