# AGENTS.md - Agent Guide for rat-trig

## Build, Test, and Lint Commands

### Testing
```bash
# Run all tests
pytest

# Run single test file
pytest tests/test_trigonom.py

# Run specific test function
pytest tests/test_trigonom.py::test_archimedes

# Run tests matching pattern
pytest -k "test_archimedes"

# Run with coverage (default in setup.cfg)
pytest --cov rat_trig --cov-report term-missing

# Using tox
tox                    # Run default tests
tox -e clean          # Remove build artifacts
tox -e build          # Build package
```

### Linting and Formatting
```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Individual tools
black .                # Format code (max line length: 120)
isort .                # Sort imports
flake8 .               # Lint (max line length: 120, ignores E203/W503)
mypy .                 # Type check (Python 3.12)
```

### Documentation
```bash
# Build docs
tox -e docs

# Run doctests
tox -e doctests

# Check links
tox -e linkcheck
```

## Code Style Guidelines

### Project Structure
- **Layout**: `src/` layout with package in `src/rat_trig/`
- **Tests**: All tests in `tests/` directory, `test_*.py` naming
- **Documentation**: Sphinx docs in `docs/` with MyST parser

### Import Style
- **Order**: Standard library → Third-party → Local (enforced by isort)
- **No relative imports**: Use absolute imports from package root
```python
from fractions import Fraction
from typing import Sequence, TypeVar, Union
from rat_trig.trigonom import archimedes
```

### Type Hints
- **Required**: All function signatures must have type hints
- **Custom types**: Define type aliases and TypeVars for clarity
```python
NumType = TypeVar("NumType", int, Fraction, float)
Numeric = Union[int, Fraction, float]

def archimedes(q_1: Numeric, q_2: Numeric, q_3: Numeric) -> Numeric:
    ...
```
- **Tests**: Type hints optional in test files (mypy ignores tests/)

### Naming Conventions
- **Functions/variables**: `snake_case` (e.g., `archimedes`, `cross`, `dot`)
- **Type variables**: `PascalCase` (e.g., `NumType`, `Numeric`)
- **Mathematical params**: Use underscores for subscripts: `q_1`, `v_2`, `s_3`
- **Constants**: `UPPER_CASE` (not commonly used in this codebase)

### Docstring Format
- **Style**: reStructuredText with Napoleon-style Google/NumPy docstrings
- **Required sections**: `:param`, `:type`, `:return`, `:rtype`
- **Examples**: Include `>>>` doctest examples in docstrings
```python
def archimedes(q_1: Numeric, q_2: Numeric, q_3: Numeric) -> Numeric:
    r"""
    The function `archimedes` calculates the quadrea of a triangle...

    :param q_1: The first quadrance
    :type q_1: Numeric
    :return: The quadrea value
    :rtype: Numeric

    Example:
        >>> archimedes(1, 4, 9)
        0
    """
```
- **Diagrams**: Use `.. svgbob::` for ASCII art diagrams in math functions
- **Module docs**: Start with `"""` explaining the module's purpose

### Code Formatting
- **Formatter**: Black (configured to max line length 120)
- **Import sorter**: isort (compatible with Black)
- **Line length**: 120 characters (enforced by flake8)
- **Indentation**: 4 spaces (no tabs)

### Error Handling
- **Preconditions**: Use `assert` for function preconditions
- **Minimal try/except**: Only when necessary, avoid empty catch blocks
- **Docstrings**: Document expected exceptions in docstrings
```python
def fib(number: int) -> int:
    """Fibonacci example function

    Args:
        number (int): integer

    Returns:
        int: n-th Fibonacci number
    """
    assert number > 0  # Precondition check
    ...
```

### Testing Guidelines
- **Framework**: pytest
- **Coverage**: Aim for high coverage (pytest-cov configured)
- **Test structure**: Each function has a corresponding `test_*.py` file
- **Naming**: Test functions use `test_` prefix and describe what's tested
```python
def test_archimedes() -> None:
    """Test Archimedes' formula"""
    # Test with integers
    assert archimedes(2, 4, 6) == 32

    # Test with floats
    assert archimedes(2.0, 4.0, 6.0) == 32

    # Test with fractions
    assert archimedes(Fraction(1, 2), Fraction(1, 4), Fraction(1, 6)) == Fraction(23, 144)
```
- **Multiple types**: Test with `int`, `float`, and `Fraction` for numeric functions
- **Edge cases**: Test zero, negative values, and degenerate cases

### Pre-commit Hooks (Active)
- trailing-whitespace
- check-added-large-files
- check-ast (valid Python syntax)
- check-json / check-yaml / check-xml
- end-of-file-fixer
- mixed-line-ending (auto-fix)
- isort
- black
- flake8

### Configuration Files
- **setup.cfg**: Package metadata, pytest config, flake8 settings
- **pyproject.toml**: Build system (setuptools_scm)
- **tox.ini**: Test environments (default, build, clean, docs, doctests)
- **.pre-commit-config.yaml**: Pre-commit hooks configuration
- **mypy.ini**: Type checking (Python 3.12, ignores errors in tests/)
- **.coveragerc**: Coverage reporting (excludes `__repr__`, debug code, assertions)

### Version Control
- **SCM**: setuptools_scm for automatic versioning from git tags
- **Version scheme**: `no-guess-dev` (from pyproject.toml)
- **Branch**: Main development on `main` branch

### Mathematical Conventions
- **Rational trigonometry**: Uses rational numbers, avoid irrational values
- **Quadrance**: Squared distance (q), not traditional distance
- **Spread**: Squared sine of angle (s), not traditional angle
- **Type support**: Functions accept `int`, `float`, or `Fraction` for precision
- **Formulas**: Follow Wildberger's Rational Trigonometry formulas

## Notes for Agents

1. **Always run tests** after making changes to verify functionality
2. **Use type hints** in all new functions (mypy will warn if missing)
3. **Add docstrings** with examples for all public functions
4. **Test with multiple numeric types** (int, float, Fraction) for mathematical functions
5. **Run pre-commit** before committing: `pre-commit run --all-files --show-diff-on-failure`
6. **Build package** with `tox -e build` before releasing
7. **Check coverage** with `pytest --cov` to ensure tests are comprehensive
