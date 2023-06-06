from myapp.sample import validate_age
import pytest


def test_validate_age_with_valid_age():
    validate_age(22)


# raising ValueError test
def test_validate_age_with_invalid_age():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-3)

    assert str(exc_info.value) == "Age cannot be less than 0"


def test_validate_age_with_invalid_age_another_way():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-3)
