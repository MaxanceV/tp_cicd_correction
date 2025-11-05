"""Tests for calculator module."""

import pytest
from mathutils import calculator
import sys


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0


def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5
    assert calculator.subtract(-1, -1) == 0


def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 100) == 0


def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(-10, 2) == -5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)


def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(2, -1) == 0.5


def test_square_root():
    assert calculator.square_root(4) == 2
    assert calculator.square_root(9) == 3
    assert calculator.square_root(0) == 0


def test_square_root_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        calculator.square_root(-1)


def test_factorial():
    assert calculator.factorial(0) == 1
    assert calculator.factorial(1) == 1
    assert calculator.factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        calculator.factorial(-1)
