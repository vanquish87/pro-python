from myapp.sample import save_dict
import os, json

"""
Introduction to pytest Fixtures
"""


def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    d = {"a": 1, "b": 2}

    # calling the function
    save_dict(d, filepath)
    assert json.load(open(filepath, 'r')) == d
    assert capsys.readouterr().out == 'saved\n'