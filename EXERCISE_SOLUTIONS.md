# Solutions CI/CD

## ⚠️ Enseignant uniquement

---

## Solution du Bug

### Problème dans calculator.py

```python
# INCORRECT (ligne ~62):
def square_root(a):
    if a<0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt( a ) + 1  # BUG: +1 en trop!

# CORRECT:
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)
```

**Explication:**
- L'erreur: `return math.sqrt(a) + 1` ajoute 1 au résultat
- `square_root(4)` retourne `3.0` au lieu de `2.0`
- Le test `assert calculator.square_root(4) == 2` échoue

---

## Code Corrigé Complet

### mathutils/calculator.py (corrigé)

```python
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
    return math.factorial(n)
```

### mathutils/__init__.py (corrigé)

```python
"""Simple mathematical utilities for CI/CD learning."""

__version__ = "0.1.0"

from .calculator import (
    add,
    divide,
    factorial,
    multiply,
    power,
    square_root,
    subtract,
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
```

### tests/test_calculator.py (corrigé)

```python
"""Tests for calculator module."""

import pytest

from mathutils import calculator


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
    with pytest.raises(
        ValueError, match="Cannot calculate square root of negative number"
    ):
        calculator.square_root(-1)


def test_factorial():
    assert calculator.factorial(0) == 1
    assert calculator.factorial(1) == 1
    assert calculator.factorial(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        calculator.factorial(-1)
```

---

## Étapes de Correction

1. **Identifier le bug:**
```bash
pytest --cov=mathutils -v
# FAILED tests/test_calculator.py::test_square_root - AssertionError: assert 3.0 == 2
```

2. **Corriger le bug:**
```python
# Supprimer le +1 dans square_root()
return math.sqrt(a)  # Pas +1
```

3. **Corriger le style:**
```bash
black .
isort .
```

4. **Supprimer imports inutiles:**
```python
# Supprimer de calculator.py:
import os
import sys
```

5. **Vérifier tout:**
```bash
pytest --cov=mathutils
black --check .
isort --check .
flake8 .
```

---

## CI Workflow

### .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main, 'feature/**']
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.9', '3.10', '3.11', '3.12']

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        pip install -e .
        pip install -r requirements-dev.txt
    
    - name: Format check
      run: black --check .
    
    - name: Import sort check
      run: isort --check .
    
    - name: Lint
      run: flake8 . --max-line-length=88 --extend-ignore=E203
    
    - name: Test
      run: pytest --cov=mathutils --cov-report=term-missing --cov-fail-under=80
```

---

## CD Workflow

### .github/workflows/cd.yml

```yaml
name: CD

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'
    
    - name: Install build tools
      run: pip install build twine
    
    - name: Build
      run: python -m build
    
    - name: Check
      run: twine check dist/*
    
    - name: Publish
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.GITHUB_TOKEN }}
      run: twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

---

## Points Clés

### Simplicité (inspiré de pkgsample)
- Pas de classes inutiles → fonctions simples
- Pas de type hints complexes → plus accessible
- Docstrings courtes avec exemples
- Tests simples et directs
- Configuration minimale

### Tools de qualité
- **Black**: Formatage automatique du code
- **isort**: Tri automatique des imports (profile="black" pour compatibilité)
- **Flake8**: Linting et vérification du style
- **Pytest**: Tests avec couverture de code

### Feature Branching
```yaml
on:
  push:
    branches: [main, 'feature/**']  # Guillemets pour **
```

### Matrix Testing
```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11', '3.12']
```

### Permissions CD
```yaml
permissions:
  contents: read
  packages: write
```

---

## Workflow Complet

```bash
# 1. Feature branch
git checkout -b feature/my-feature

# 2. Dev local
pip install -e .
pytest

# 3. Push
git push origin feature/my-feature

# 4. PR → CI ✅ → Merge

# 5. Release
git checkout main
git pull
git tag v0.1.0
git push origin v0.1.0
```

---

## Grille d'Évaluation

| Critère | Points |
|---------|--------|
| **Correction du Bug** | |
| Bug identifié | 2 |
| Bug corrigé correctement | 2 |
| Tests passent | 1 |
| **CI - Configuration** | |
| Structure workflow | 1 |
| Triggers corrects | 2 |
| Matrix 4 versions | 2 |
| **CI - Qualité Code** | |
| Black | 2 |
| isort | 2 |
| Flake8 | 2 |
| Tests + coverage | 2 |
| **Git Workflow** | |
| Feature branch | 1 |
| Pull Request | 1 |
| **CD - Déploiement** | |
| Trigger tags | 1 |
| Build + publish | 2 |
| **Total** | **23** |

---

## Commandes Étudiants

```bash
# Setup
pip install -e .
pip install -r requirements-dev.txt

# Local checks
black .
isort .
flake8 . --max-line-length=88
pytest --cov=mathutils

# Build local
python -m build
twine check dist/*

# Git workflow
git checkout -b feature/setup-cicd
git add .github/workflows/
git commit -m "feat: add CI/CD"
git push origin feature/setup-cicd
# PR → Merge
git checkout main
git pull
git tag v0.1.0
git push origin v0.1.0
```

---

**Durée: 1h30**