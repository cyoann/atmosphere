# Atmosphere

Atmosphere is a daemon that runs on your computer and provides a CLI to manage your computer.

It is only written for a personal use case, but feel free to use it if you want.

## Table of Contents


- [Atmosphere](#atmosphere)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Features](#features)
  - [Installation](#installation)
    - [Poetry](#poetry)
    - [Pip](#pip)
  - [Usage](#usage)
    - [CLI](#cli)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)

## Prerequisites

- Linux
- [Dunst](https://dunst-project.org/)
- [pamixer](https://github.com/cdemoulins/pamixer)
- Python 3.8.1 or higher
- [Poetry](https://python-poetry.org/) (optional)

## Features

- [x] Manage your computer's brightness
- [x] Manage your computer's volume using `pamixer`
- [x] Notify changes with `dunstify`

## Installation

### Poetry

```bash
poetry install
```

### Pip

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

## Usage

### CLI

```bash
.venv/bin/python3 src/atmosphere/cli.py --help
```


## Acknowledgments

- [pamixer](https://github.com/cdemoulins/pamixer)
- [dunst](https://dunst-project.org/)
- [click](https://click.palletsprojects.com/)
- [typer](https://typer.tiangolo.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
