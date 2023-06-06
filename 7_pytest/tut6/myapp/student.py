from datetime import datetime


class Student:
    def __init__(self, name, dob, branch):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = 0

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits


# -----------------
from dataclasses import dataclass


@dataclass
class SuperStudent:
    name: str
    date_of_birth: datetime
    branch_of_study: str
    credits_scored: int = 0

    def get_age(self):
        return (datetime.now() - self.date_of_birth).days // 365

    def add_credits(self, value):
        self.credits_scored += value

    def get_credit_scored(self):
        return self.credits_scored
