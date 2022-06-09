"""Top-level package for crypto-currency-price."""

from .cli import cli
from .version import __author__, __email__, __timestamp__, __version__

__all__ = ["cli", __version__, __timestamp__, __author__, __email__]
