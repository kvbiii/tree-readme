from pathlib import Path

EMOJI_MAPPING: dict[str, str] = {
    "folder": "📁",
    ".py": "🐍",
    ".sas": "📶",
    ".ipynb": "📓",
    ".sh": "🐚",
    ".pkl": "🥒",
    ".txt": "📃",
    ".json": "📙",
    ".j2": "🔖",
    ".gitignore": "👻",
    ".git": "😺",
    ".md": "📖",
    ".toml": "⚙️",
    ".yaml": "📜",
    ".yml": "📜",
    "Dockerfile": "🐳",
    ".png": "🖼️",
    ".jpg": "🖼️",
    ".csv": "📊",
    "default": "📄",
}


def get_emoji(path: Path) -> str:
    """
    Returns emoji for file/folder.

    Args:
        path (Path): Path to the file or folder.

    Returns:
        str: Corresponding emoji.
    """
    if path.is_dir():
        return EMOJI_MAPPING["folder"]
    return EMOJI_MAPPING.get(
        path.name, EMOJI_MAPPING.get(path.suffix, EMOJI_MAPPING["default"])
    )
