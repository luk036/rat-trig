# Changelog

## Version 0.2 (Upcoming)

- Improve documentation and examples
- Add comprehensive README with installation and usage instructions
- Fix import warnings in package initialization
- Add GitHub Actions CI/CD pipeline

## Version 0.1 (2024)

### Initial Release

- Core rational trigonometry functions implemented:
  - `quad()` - Quadrance calculation
  - `dot()` - Dot product
  - `cross()` - Cross product
  - `spread()` - Spread calculation
  - `archimedes()` - Archimedes' formula
  - `spread_law()` - Law of spreads
  - `triple_quad_formula()` - Triple quad formula

### Features

- Support for multiple numeric types: `int`, `float`, `Fraction`
- Comprehensive type hints throughout
- 99% test coverage with 36 unit tests
- Property-based testing with Hypothesis
- Documentation with Sphinx and MyST parser
- SVG diagrams in docstrings using svgbob

### Testing

- All core functions thoroughly tested
- Edge cases covered (zero vectors, degenerate triangles, etc.)
- Property-based tests for mathematical invariants
- Vector operation properties verified (commutativity, distributivity, etc.)

### Development Tools

- Code formatting with Black (120 character line length)
- Import sorting with isort
- Linting with flake8
- Type checking with mypy (Python 3.12)
- Pre-commit hooks configured
- Tox for testing automation
