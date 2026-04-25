import pytest
from main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(10, -5) == 5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 10) == 0
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(10, -2) == -20

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5
    assert divide(0, 5) == 0

def test_divide_by_zero():
    assert divide(10, 0) == 'Error: Division by zero'
    assert divide(0, 0) == 'Error: Division by zero'