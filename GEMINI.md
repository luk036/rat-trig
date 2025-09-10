# GEMINI.md

## Project Overview

This project, `rat-trig`, is a Python library for Rational Trigonometry, a reformulation of trigonometry that avoids the use of transcendental functions and square roots. The library provides a set of functions for performing trigonometric calculations using only rational numbers. The project is structured as a standard Python library and was bootstrapped using PyScaffold.

The main logic is contained in `src/rat_trig/trigonom.py`, which includes functions like `archimedes`, `cross`, `dot`, `quad`, `spread`, `triple_quad_formula`, and `spread_law`. These functions are well-documented with docstrings that include examples.

## Building and Running

### Dependencies

The project's dependencies are listed in `requirements/default.txt` and `requirements/test.txt`.

*   **Core:** `decorator`
*   **Testing:** `pytest`, `pytest-benchmark`, `pytest-cov`, `coverage`

### Building the Project

To build the project, you can use the `build` package:

```bash
python -m build
```

This will create a `dist` directory with the wheel and sdist packages.

### Running Tests

Tests are located in the `tests` directory and can be run using `pytest`:

```bash
pytest
```

Alternatively, you can use `tox` to run tests in different environments:

```bash
tox
```

The `tox.ini` file defines several test environments, including `default` for running pytest, `lint` for static analysis, and `docs` for building the documentation.

## Development Conventions

*   **Project Structure:** The project follows the PyScaffold layout, with the source code in the `src` directory.
*   **Coding Style:** The project uses `flake8` for code style checking. The configuration is in the `setup.cfg` file.
*   **Testing:** The project uses `pytest` for unit testing and `doctest` for testing examples in docstrings.
*   **Documentation:** The documentation is located in the `docs` directory and is built using Sphinx.

## Code Optimizations

I have performed the following code optimizations:

*   **`archimedes` function:** Inlined the `temp` variable to avoid an unnecessary variable assignment.
*   **`spread` function:** Inlined the `cross` and `quad` functions to avoid the overhead of function calls.