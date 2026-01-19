import sys

from .trigonom import archimedes as archimedes
from .trigonom import cross as cross
from .trigonom import dot as dot
from .trigonom import quad as quad
from .trigonom import spread as spread
from .trigonom import spread_law as spread_law
from .trigonom import triple_quad_formula as triple_quad_formula

__all__ = [
    "archimedes",
    "cross",
    "dot",
    "quad",
    "spread",
    "spread_law",
    "triple_quad_formula",
    "__version__",
]

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.9`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "rat-trig"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
