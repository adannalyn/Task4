import json
from student import Student

DATA_FILE = "student.json"

def load_goods():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            students = [Student.from_dict(item) for item in data]
            return students
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_goods(students):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump([student.to_dict() for student in students], f, indent=4)
    except IOError:
        print("Failed to save file")
