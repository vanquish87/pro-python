from myapp.sample import add
import pytest

"""
Parametrizing Unit Tests
"""


# def test_add():
#     assert add(1, 2) == 3


# def test_add_str():
#     assert add("a", "c") == "ac"


# def test_add_list():
#     assert add([1], [2]) == [1, 2]


# rather than writing multiple test to do same thing use parametrize :)
@pytest.mark.parametrize("a, b, c", [(1, 3, 4), ("a", "b", "ab"), ([1], [5], [1, 5])], ids=["num", "str", "list"])
def test_add_str(a, b, c):
    assert add(a, b) == c
