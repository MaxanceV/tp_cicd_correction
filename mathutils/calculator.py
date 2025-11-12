"""Basic mathematical operations."""

import math


def add(a, b):
    """Add two numbers.

    >>> add(2, 3)
    5
    """
    return a + b


def subtract(a, b):
    """Subtract b from a.

    >>> subtract(5, 3)
    2
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers.

    >>> multiply(2, 3)
    6
    """
    result = a * b
    return result


def divide(a, b):
    """Divide a by b.

    >>> divide(6, 2)
    3.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b.

    >>> power(2, 3)
    8.0
    """
    return math.pow(a, b)


def square_root(a):
    """Calculate square root of a.

    >>> square_root(4)
    2.0
    """
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


def factorial(n):
    """Calculate factorial of n.

    >>> factorial(5)
    120
    """
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    x = math.factorial(n)
    return x
