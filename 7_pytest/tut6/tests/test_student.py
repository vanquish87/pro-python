import pytest
from myapp.student import Student, SuperStudent
from datetime import datetime

"""
Creating Custom Fixtures
"""


# scope is used because dummy student will not be created again n again
@pytest.fixture(scope="module")
def dummy_student():
    return Student("Joo hoo", datetime(2005, 3, 15), "coe")


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_add_credits(dummy_student):
    assert dummy_student.credits == 0
    dummy_student.add_credits(15)
    assert dummy_student.credits == 15


def test_get_credits(dummy_student):
    assert dummy_student.credits == 15


@pytest.fixture(scope="function")
def dummy_super_student():
    return SuperStudent(name="Data Boy", date_of_birth=datetime(1999, 3, 28), branch_of_study="python")


def test_super_student_get_age(dummy_super_student):
    dummy_super_student_age = (datetime.now() - dummy_super_student.date_of_birth).days // 365
    assert dummy_super_student.get_age() == dummy_super_student_age


def test_super_student_add_credits(dummy_super_student):
    assert dummy_super_student.credits_scored == 0
    dummy_super_student.add_credits(4)
    assert dummy_super_student.credits_scored == 4


# because scope of fixture is 'function' hence dummy_super_student is created everytime it is called
def test_super_get_credits(dummy_super_student):
    assert dummy_super_student.credits_scored == 0
