class Student:
    def __init__(self, name, subject, score, average, grade):
        self.name = name
        self.subject = subject
        self.score = float(score)
        self.average = average
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "subject": self.subject,
            "score": self.score,
            "average": self.average,
            "grade": self.grade
        }

    def from_dict(data):
        return Student(
            name=data['name'],
            subject=data['subject'],
            score=data['score'],
            average=data['average'],
            grade=data['grade']
        )
class StudentUnion:
    def __init__(self):
        self.student = []
        self.history = []

    def add_students(self, name, subject, score):
        average = total = 0
        grade = ""
        try:
            score = float(score)
            student = Student(name, subject, score, average, grade)
            self.student.append(student)
            total += sum(student.score for student in self.student)
            average = total / len(self.student)
            if average < 40:
                grade = "fail"
            elif average > 39 and average < 60:
                grade = "Pass"
            else:
                grade = "Good"
            for i in range(len(subject)):
                print(f' - {name} | {score} | {i} | {average} | {grade}')
        except ValueError:
            print("Invalid score input. Please enter a valid number")
            self.history = ({
                "name": name,
                "subject": subject,
                "score": score,
                "average": average,
                "grade": grade
            })
            self.students.clear()
            print("Report Card updated!\n")

    def view_students(self):
        if not self.student:
            print("No students in the union")
        for student in self.student:
            print(f' - {student.name} | {student.subject} | {student.grade}')

    def update_students(self, name):
        found = False
        for student in self.history:
            if name in student.name:
                print(f'found - {student.name} | {student.subject} | {student.grade}')
                found = True
                break
        if not found:
            print("No student with that name")

    def history_records(self):
        if not self.history:
            print("No previous records.")
            return
        for item, records in enumerate(self.history, 1):
            print(f'\nReport Card {item} | record["name"]')
            print(f'Grade {records["grade"]}')
            for student in records['name']:
                print(f'{student["name"]} | {student["subject"]} | {student["grade"]}')

    def to_dict_list(self):
        return self.history

    def from_dict_list(self, dict_list):
        self.history = dict_list if dict_list else []
