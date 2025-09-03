"""
readme_generator package.

Lazy-load submodules to avoid RuntimeWarning when executing:
python -m readme_generator.generate_readme
"""

from __future__ import annotations
import importlib

__all__ = ["generate_readme", "emoji_map", "readme_builder", "repo_structure"]


def __getattr__(name: str):
    if name in __all__:
        return importlib.import_module(f"{__name__}.{name}")
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
