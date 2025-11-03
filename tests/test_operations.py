# tests/test_operations.py
from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3
    try:
        divide(1, 0)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"
