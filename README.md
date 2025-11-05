# TP CI/CD - GitHub Actions

Un exercice pratique pour apprendre le CI/CD avec GitHub Actions et le packaging Python moderne

## 📦 Le Package

`mathutils` - Fonctions mathématiques simples utilisant le module `math` de Python

```python
from mathutils import add, factorial, square_root

print(add(2, 3))          # 5
print(factorial(5))       # 120
print(square_root(16))    # 4.0
```

## 🎯 Objectifs

- Créer un workflow CI/CD avec GitHub Actions
- Utiliser le feature branching (feature → main)
- Automatiser: tests, linting, formatage, déploiement
- Publier sur GitHub Packages
- **Corriger les problèmes de qualité de code**

## 🚀 Quick Start

```bash
# Clone
git clone <repo-url>
cd tp-cicd

# Virtualenv
python -m venv .venv (check for windows)
source .venv/bin/activate

# Install
pip install -e .
pip install -r requirements-dev.txt

# Test (attention: le code a des problèmes de style!)
pytest --cov=mathutils
black --check mathutils          # ❌ Va échouer
isort --check mathutils          # ❌ Va échouer
flake8 mathutils                 # ❌ Va échouer
```

## ⚠️ Note Importante

**Le code fourni contient volontairement des problèmes !**

Vous devez:
1. ✅ Identifier les problèmes de style avec `black`, `isort` et `flake8`
2. ✅ Identifier et corriger le bug dans le code (un test échoue!)
3. ✅ Les corriger avant de créer votre CI/CD
4. ✅ Vérifier que tout passe localement
5. ✅ Proposer une solution qui permettra d'executer les checks avant le push vers le remote repository !!

```bash
# Pour identifier les problèmes:
pytest --cov=mathutils   # ❌ Un test va échouer!
black --check mathutils          # ❌ Va échouer
isort --check mathutils          # ❌ Va échouer
flake8 mathutils                 # ❌ Va échouer

# Pour corriger:
# 1. Trouver et corriger le bug dans le code
pytest --cov=mathutils   # Doit passer maintenant
```

## 📝 L'Exercice

### Étape 1: CI Workflow

Créer `.github/workflows/ci.yml`:

**Déclencheurs:**
- Push sur `main` et `feature/**`
- Pull requests vers `main`

**Jobs:**
- Tester sur Python 3.9, 3.10, 3.11, 3.12
- Formatter avec `black --check`
- Trier les imports avec `isort --check`
- Linter avec `flake8`
- Tests avec `pytest --cov` (>= 80%)

**Exemple:**
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
      # À vous de compléter!
```

### Étape 2:

Créer `.github/workflows/cd.yml`:

**Déclencheur:**
- Tags `v*.*.*` uniquement

**Jobs:**
- Build avec `python -m build`
- Check avec `twine check dist/*`
- Publish sur GitHub Packages

**Configuration:**
```yaml
permissions:
  packages: write

env:
  TWINE_USERNAME: __token__
  TWINE_PASSWORD: ${{ secrets.GITHUB_TOKEN }}
```

## 📚 Structure

```
tp-cicd/
├── mathutils/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── .github/workflows/
│   ├── ci.yml          # À créer
│   └── cd.yml          # À créer
├── pyproject.toml
├── requirements-dev.txt
└── README.md
```

## 🛠️ Commandes Utiles

```bash
# Install en mode dev
pip install -e .

# Tests
pytest                                    # Run tests
pytest --cov=mathutils                   # With coverage
pytest --cov=mathutils --cov-report=html # HTML report

# Quality
black .                          # Format code
black --check .                  # Check only
isort .                          # Sort imports
isort --check .                  # Check only
flake8 .                        # Lint

# Build
python -m build                 # Build package
twine check dist/*              # Check
ls dist/                        # Voir les fichiers
```

## 🎓 Ressources

- [GitHub Actions](https://docs.github.com/en/actions)
- [Python Packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [GitHub Packages](https://docs.github.com/en/packages)

---

**Bon courage! 🚀**