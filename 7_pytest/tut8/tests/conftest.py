import pytest
from myapp.student import Student
from datetime import datetime

"""
Parametrizing Fixtures
"""


@pytest.fixture(params=[19, 21], ids=["inelegible", "eligible"])
def dummy_student(request):
    return Student("Joo hoo", datetime(2005, 3, 15), "coe", request.param)


@pytest.fixture
def make_dummy_student_factory():
    def _make_dummy_student_factory(name, credits):
        return Student(name, datetime(2005, 3, 15), "coe", credits)

    return _make_dummy_student_factory
