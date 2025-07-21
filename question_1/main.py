import os
from report import save_goods, load_goods
from student_utils import StudentUnion

student = StudentUnion()
DATA_FILE = "student.json"

if os.path.exists(DATA_FILE):
    dict_list = load_goods(DATA_FILE)
    student.from_dict_list(dict_list)
    print("Previous student records loaded.")
else:
    print("Fresh start.")

while True:
    print("\n---- Report Card Records ----")
    print("1. Add student")
    print("2. View all students")
    print("3. Update Student")
    print("4. History")
    print("5. Exit\n")
    choice = input("Enter your choice (1 - 4) ").strip()

    if choice == '1':
        subject = ""
        name = input("Enter your name: ").strip().title()
        number = int(input("How many subjects do you wish to enter (1 - 6) "))
        for subjects in range(number):
            subject = input("Enter your subject: ").strip().title()
            score = input("Enter your score: ").strip()
        student.add_students(name, subject, score)

    elif choice == '2':
        student.view_students()

    elif choice == '3':
        name = input("Enter student's name: ").strip().title()
        student.update_students(name)

    elif choice == '4':
        student.history_records()

    elif choice == '5':
        save_goods(DATA_FILE, student.to_dict_list())
        print("Records saved! Goodbye.\n")
        break
    else:
        print("Please enter a valid number between 1 and 4.")
