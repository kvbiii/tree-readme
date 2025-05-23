# readme-generator

## Overview
This is a sample README generated by the script.

## Folder Structure
```
┣━ 📁 .github
┃  ┗━ 📁 workflows
┃     ┗━ ⚙️ python-publish.yml
┣━ 📁 readme_generator
┃  ┣━ 🐍 __init__.py
┃  ┣━ 🐍 emoji_map.py
┃  ┣━ 🐍 generate_readme.py
┃  ┣━ 🐍 readme_builder.py
┃  ┗━ 🐍 repo_structure.py
┣━ 📄 .gitignore
┣━ 📄 pyproject.toml
┣━ 📝 README.md
┗━ 📃 requirements.txt
```

## Files Description
* 📁 `.github`: Contains configuration files for GitHub-specific workflows and actions.
	- 📁 `workflows`: Contains GitHub Actions workflows for automating tasks.
		- ⚙️ `python-publish.yml`: Contains GitHub Actions workflow configuration for automating Python package publishing.
* 📁 `readme_generator`: Contains the main Python package for the project.
	- 🐍 `__init__.py`: Marks the folder as a Python package.
	- 🐍 `emoji_map.py`: Maps file types to corresponding emojis for visual representation.
	- 🐍 `generate_readme.py`: Main script for generating the README file.
	- 🐍 `readme_builder.py`: Handles the logic for constructing the README content.
	- 🐍 `repo_structure.py`: Defines the repository structure for the README.
* 📄 `.gitignore`: Specifies files and directories to be ignored by Git.
* 📄 `pyproject.toml`: Configuration file for Python project dependencies and build system.
* 📝 `README.md`: The generated README file for the project.
* 📃 `requirements.txt`: Lists the Python dependencies required for the project.

## Installation

To install the package, run the following command:

```bash
pip install readme-generator
```

## Usage

To generate a README file, run the following command:

```bash
python -m readme_generator.generate_readme \
	--repo_path "path/to/your/repository" \
	--overview "This is a sample README generated by the script." \
	--exclude_dirs venv __pycache__ .egg-info \
	--exclude_files .jpg .png .txt
```

### Parameters

- `--repo_path`: Specifies the path to the repository for which the README will be generated.
	- Example: `"C:\path\to\your\repository"`

- `--overview`: Provides a brief description of the project to include in the README.
	- Example: `"This is a sample README generated by the script."`

- `--exclude_dirs`: Lists directories to exclude from the repository structure in the README.
	- Example: `venv __pycache__ .egg-info`

- `--exclude_files`: Lists file extensions or specific files to exclude from the repository structure in the README.
	- Example: `.jpg .png .txt`

### Python Version

It can also be run using the following python code:

```python
from pathlib import Path
from readme_generator.generate_readme import generate_readme

repo_path = Path(__file__).resolve().parent
generate_readme(
	repo_path,
	overview="This is a sample README generated by the script.",
	exclude_dirs={"venv", "__pycache__", ".egg-info"},
	exclude_files={".jpg", ".png", "txt"}
)
```

-------------------------------------------
**Last updated on 2025-05-09 23:09**
