"""Simple mathematical utilities for CI/CD learning."""

__version__ = "0.1.0"

from .calculator import add, subtract
from .calculator import multiply, divide
from .calculator import (
    power,
    square_root,
    factorial,
)

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "square_root",
    "factorial",
]
