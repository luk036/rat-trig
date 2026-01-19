[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)
[![Documentation Status](https://readthedocs.org/projects/rat-trig/badge/?version=latest)](https://rat-trig.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/luk036/rat-trig/badge.svg?branch=main)](https://coveralls.io/github/luk036/rat-trig?branch=main)

# 📐 rat-trig

> Rational Trigonometry - A Python implementation of Wildberger's Rational Trigonometry

## What is Rational Trigonometry?

Rational Trigonometry is a revolutionary approach to classical trigonometry, developed by Norman Wildberger. It replaces the traditional notions of distance and angle with **quadrance** (squared distance) and **spread** (squared sine of angle), allowing for:

- **Exact calculations** using rational numbers
- **No irrational numbers or transcendental functions**
- **Simpler algebraic relationships**
- **Better suited for computational geometry and computer graphics**

## Installation

```bash
pip install rat-trig
```

For development:

```bash
git clone https://github.com/luk036/rat-trig.git
cd rat-trig
pip install -e .
```

## Quick Start

```python
from fractions import Fraction
from rat_trig import archimedes, spread, quad

# Calculate quadrance (squared distance)
vector = [3, 4]
print(f"Quadrance: {quad(vector)}")  # Output: 25

# Calculate spread between two vectors
v1 = [1, 2]
v2 = [3, 4]
print(f"Spread: {spread(v1, v2)}")  # Output: 4/125

# Apply Archimedes' formula to a triangle
q1, q2, q3 = Fraction(1, 2), Fraction(1, 4), Fraction(1, 6)
A = archimedes(q1, q2, q3)
print(f"Quadrea: {A}")  # Output: 23/144
```

## Core Functions

### Geometric Operations

- **`quad(vector)`** - Calculate quadrance (squared distance) of a vector
- **`dot(v1, v2)`** - Dot product of two vectors
- **`cross(v1, v2)`** - Cross product of two vectors

### Trigonometric Operations

- **`spread(v1, v2)`** - Calculate spread between two vectors (squared sine of angle)
- **`archimedes(q1, q2, q3)`** - Archimedes' formula for triangle quadrea
- **`spread_law(q1, q2, q3)`** - Law of spreads for triangles
- **`triple_quad_formula(q1, q2, s3)`** - Triple quad formula relating quadrances and spreads

## Features

- ✅ **Exact arithmetic** with `Fraction` support
- ✅ **Multiple numeric types** - works with `int`, `float`, or `Fraction`
- ✅ **99% test coverage** with comprehensive unit tests
- ✅ **Type hints** throughout the codebase
- ✅ **Well-documented** with docstrings and examples

## Documentation

Full documentation is available at [https://rat-trig.readthedocs.io](https://rat-trig.readthedocs.io/).

## Testing

Run tests:

```bash
pytest
```

With coverage:

```bash
pytest --cov rat_trig
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

This project was developed using [PyScaffold](https://pyscaffold.org/) and is based on Norman Wildberger's work on Rational Trigonometry.
