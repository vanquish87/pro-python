import pytest
from myapp.student import Student
from datetime import datetime


@pytest.fixture
def dummy_student():
    return Student("Joo hoo", datetime(2005, 3, 15), "coe", 20)


@pytest.fixture
def make_dummy_student_factory():
    def _make_dummy_student_factory(name, credits):
        return Student(name, datetime(2005, 3, 15), "coe", credits)

    return _make_dummy_student_factory
