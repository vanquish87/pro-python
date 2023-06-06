from myapp.sample import add
import pytest
import sys

"""
Introduction to pytest Markers
"""


# skipping this test
@pytest.mark.skip(reason="Just moode tha isiliye :)")
def test_add():
    assert add(1, 2) == 3


# conditional skipping as I am using python 3.10.11
@pytest.mark.skipif(sys.version_info > (3, 7), reason="Use less than 3.7 version")
def test_add_str():
    assert add("a", "c") == "ac"


# your code can throw some Exception but you are OK with that
@pytest.mark.xfail(sys.platform == 'win32', reason='Will only run on windows')
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
