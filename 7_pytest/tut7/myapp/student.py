from datetime import datetime


class Student:
    def __init__(self, name, dob, branch, credit):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credit

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def get_credits(self):
        return self.credits


def get_topper(students):
    return max(students, key=lambda student: student.get_credits())


