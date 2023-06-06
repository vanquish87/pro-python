from myapp.student import get_topper
from datetime import datetime

"""
Creating Fixture Factory
"""


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_get_credits(dummy_student):
    assert dummy_student.credits == 20


def test_get_topper(make_dummy_student_factory):
    students = [
        make_dummy_student_factory("heao", 34),
        make_dummy_student_factory("raj", 55),
        make_dummy_student_factory("shinchan", 88),
    ]

    topper = get_topper(students)
    assert topper == students[2]
