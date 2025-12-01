import pytest
from lib.password_checker import PasswordChecker   # make sure your file is lib/password_checker.py

def test_valid_password_returns_true():
    checker = PasswordChecker()
    # exactly 8 characters
    assert checker.check("abcdefgh") is True

def test_long_password_returns_true():
    checker = PasswordChecker()
    # longer than 8 characters
    assert checker.check("supersecurepassword") is True

def test_short_password_raises_error():
    checker = PasswordChecker()
    # shorter than 8 characters should raise an error
    with pytest.raises(Exception) as error:
        checker.check("short")
    assert str(error.value) == "Invalid password, must be 8+ characters."
