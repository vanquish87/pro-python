from myapp.sample import add


def test_add():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "c") == "ac"


# inside a Class
class TestSample:
    def test_add(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "c") == "ac"
