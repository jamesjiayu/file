# Chapter 11: Testing Your Code
# Name: James W.
# Date: 04/11/2025

import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    result = add(1, 2)
    assert result == 3.0
    # 3 . assert isinstance(add(-1, 0), float), "Result should be a float"
    assert isinstance(result, float)
    assert type(result) is float
    assert add(-1, -3) == -4.0
    assert add(-1, 0) == -1.0


def test_subtract():
    assert subtract(1, 1) == 0.0  # 0
    assert subtract(1, 2) == -1.0
    assert subtract(2, 1) == 1.0


def test_multiply():
    assert multiply(1, 1) == 1.0
    assert multiply(1, -1) == -1.0
    assert multiply(-1, -1) == 1.0


def test_divide():
    assert divide(1, 1) == 1.0
    assert divide(-1, -1) == 1.0
    assert divide(-1, 1) == -1.0
    assert divide(1, 0) is None


"""
def test_add_error_handling(capsys):
    # Test invalid input: string
    result = add("a", 3)
    captured = capsys.readouterr()  # Capture printed output
    assert result is None, "Non-number input should return None"
    assert "Error: could not convert string to float: 'a'" in captured.out, "Should print error for invalid string"

    # Test invalid input: None
    result = add(None, 5)
    captured = capsys.readouterr()
    assert result is None, "None input should return None"
    assert "Error: float() argument must be a string or a number, not 'NoneType'" in captured.out, "Should print error for None"

    # Test invalid input: list
    result = add([1, 2], 3)
    captured = capsys.readouterr()
    assert result is None, "List input should return None"
    assert "Error: float() argument must be a string or a number, not 'list'" in captured.out, "Should print error for list"

"""
