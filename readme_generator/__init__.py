from __future__ import annotations
import importlib
from importlib.metadata import PackageNotFoundError, version

__version__ = "0+unknown"
try:
    __version__ = version("tree-readme")
except PackageNotFoundError:
    pass

__all__ = [
    "__version__",
    "generate_readme",
    "emoji_map",
    "readme_builder",
    "repo_structure",
]


def __getattr__(name: str):
    if name in __all__:
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
