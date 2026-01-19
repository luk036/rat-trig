# Contributing

Welcome to `rat-trig` contributor's guide.

This document focuses on getting any potential contributor familiarized with
development processes. All kinds of contributions are appreciated, including bug reports, documentation, and code improvements.

If you are new to using [git] or have never collaborated in a project previously,
please have a look at [contribution-guide.org]. Other resources are also listed in the excellent [guide created by FreeCodeCamp].

Please notice, all users and contributors are expected to be **open, considerate, reasonable, and respectful**. When in doubt, [Python Software Foundation's Code of Conduct] is a good reference in terms of behavior guidelines.

## Issue Reports

If you experience bugs or have general issues with `rat-trig`, please have a look at the [issue tracker]. If you don't see anything useful there, please feel free to create an issue report.

:::{tip}
Please don't forget to include closed issues in your search.
Sometimes a solution was already reported, and the problem is considered **solved**.
:::

New issue reports should include information about your programming environment (e.g., operating system, Python version) and steps to reproduce the problem. Please try to simplify reproduction steps to a minimal example that still illustrates the problem you're facing. By removing other factors, you help us identify the root cause of the issue.

## Documentation Improvements

You can help improve `rat-trig` docs by making them more readable and coherent, or by adding missing information and correcting mistakes.

`rat-trig` documentation uses [Sphinx] with [MyST] extensions. Documentation is kept in the same repository as the project code, and documentation updates are done the same way as code contributions.

When working on documentation changes in your local machine, you can compile them using [tox]:

```bash
tox -e docs
```

and use Python's built-in web server for a preview in your web browser (`http://localhost:8000`):

```bash
python -m http.server --directory docs/_build/html
```

## Code Contributions

### Submit an Issue

Before you work on any non-trivial code contribution, it's best to first create a report in the [issue tracker] to start a discussion. This often provides additional considerations and avoids unnecessary work.

### Create an Environment

Before you start coding, we recommend creating an isolated [virtual environment] to avoid problems with your installed Python packages.

Using [Miniconda]:

```bash
conda create -n rat-trig python=3.11
conda activate rat-trig
```

Or using [virtualenv]:

```bash
virtualenv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Clone the Repository

1. Create a user account on GitHub if you do not already have one.

2. Fork the [repository]: click on the _Fork_ button near the top of the page. This creates a copy of the code under your account on GitHub.

3. Clone this copy to your local disk:

```bash
git clone https://github.com/YourLogin/rat-trig.git
cd rat-trig
```

4. Install the package in development mode:

```bash
pip install -e .
```

5. Install development dependencies and [pre-commit]:

```bash
pip install -r requirements/test.txt
pip install pre-commit
pre-commit install
```

`rat-trig` comes with pre-commit hooks configured to automatically check code quality. These will run:
- **flake8** - code style and linting
- **black** - code formatting
- **isort** - import sorting
- **mypy** - type checking (Python 3.12)

### Implement Your Changes

1. Create a branch to hold your changes:

```bash
git checkout -b my-feature
```

and start making changes. Never work on the main branch!

2. Start your work on this branch. Don't forget to add [docstrings] to new functions, modules, and classes, especially if they're part of public APIs. Include usage examples with `>>>` for doctests.

3. When you're done editing, do:

```bash
git add <MODIFIED FILES>
git commit
```

to record your changes in [git].

Make sure to address any validation messages from [pre-commit]. The hooks will automatically use [flake8], [black], and [isort] to check/fix code style.

:::{important}
Don't forget to add unit tests for new features or bugfixes.

Moreover, writing a [descriptive commit message] is highly recommended. Use conventional commit format (e.g., `feat: add new function`, `fix: correct spread calculation`, `docs: update README`). Check the commit history with:

```bash
git log --graph --decorate --pretty=oneline --abbrev-commit --all
```

to look for recurring communication patterns.
:::

5. Please check that your changes don't break any unit tests with:

```bash
pytest
```

Or run the full test suite with coverage:

```bash
pytest --cov rat_trig
```

You can also use [tox] to run several other pre-configured tasks:

```bash
tox -av  # List all available tox environments
```

### Submit Your Contribution

1. If everything works fine, push your local branch to the remote server:

```bash
git push -u origin my-feature
```

2. Go to the web page of your fork and click "Create Pull Request" to send your changes for review.

### Review Process

- Automated CI/CD tests will run on your PR (linting, tests, type checking)
- Maintainers will review your code for:
  - Mathematical correctness
  - Code quality and style
  - Test coverage
  - Documentation
- Address review comments in follow-up commits
- Once approved, your PR will be merged into main

### Troubleshooting

The following tips can help when facing problems building or testing the package:

1. **Tag issues**: Make sure to fetch all tags from upstream. The command `git describe --abbrev=0 --tags` should return the expected version. If you're trying to run CI scripts in a fork, make sure to push all tags.

2. **Clean builds**: Sometimes tox misses out when new dependencies are added. Try recreating the tox environment with the `-r` flag:

```bash
tox -r -e docs  # Instead of tox -e docs
```

3. **Python version**: Ensure you have a reliable tox installation using the correct Python version (3.11+). Check with:

```bash
tox --version
```

4. **Debugging tests**: Pytest can drop you in an interactive session in case an error occurs. To do this, pass a `--pdb` option:

```bash
pytest --k <NAME_OF_FAILING_TEST> --pdb
```

## Maintainer Tasks

### Releases

If you're part of the maintainer group with PyPI permissions, follow these steps to release a new version:

1. Make sure all unit tests are successful.
2. Update `CHANGELOG.md` with version details.
3. Tag the current commit on main branch with a release tag, e.g., `v1.2.3`.
4. Push the new tag to the upstream repository:

```bash
git push upstream v1.2.3
```

5. Clean up `dist` and `build` folders:

```bash
tox -e clean
```

6. Build the package:

```bash
tox -e build
```

Check that files in `dist` have the correct version (no `.dirty` or git hash) and reasonable sizes.

7. Publish to PyPI:

```bash
tox -e publish -- --repository pypi
```

[black]: https://pypi.org/project/black/
[myst]: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
[contribution-guide.org]: http://www.contribution-guide.org/
[descriptive commit message]: https://www.conventionalcommits.org/
[docstrings]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[flake8]: https://flake8.pycqa.org/en/stable/
[git]: https://git-scm.com
[guide created by freecodecamp]: https://github.com/firstcontributions/how-to-contribute
[isort]: https://pycqa.github.io/isort/
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[other kinds of contributions]: https://opensource.guide/how-to-contribute
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/
[python software foundation's code of conduct]: https://www.python.org/psf/conduct/
[sphinx]: https://www.sphinx-doc.org/en/master/
[tox]: https://tox.readthedocs.io/en/stable/
[virtual environment]: https://realpython.com/python-virtual-environments-a-primer/
[virtualenv]: https://virtualenv.pypa.io/en/stable/

[repository]: https://github.com/luk036/rat-trig
[issue tracker]: https://github.com/luk036/rat-trig/issues
