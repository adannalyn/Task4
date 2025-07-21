class Student:
    def __init__(self, name, subjects_scores):
        self.name = name
        self.subjects_scores = subjects_scores
        self.average = 0.0
        self.grade = ""
        self.calculate_average_and_grade()

    def calculate_average_and_grade(self):
        total_score = sum(self.subjects_scores.values())
        number_of_subjects = len(self.subjects_scores)

        if number_of_subjects > 0:
            self.average = total_score / number_of_subjects
        else:
            self.average = 0.0

        if self.average >= 90:
           self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
           self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def to_dict(self):
        return {
            "name": self.name,
            "subjects_scores": self.subjects_scores,
            "average": self.average,
            "grade": self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(data["name"], data["subjects_scores"])
