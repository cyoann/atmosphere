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

- [x] Manage your computer's brightness using `light`
- [x] Manage your computer's volume using `pamixer`
- [x] Fetch weather information from [wttr.in](https://wttr.in)
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
$ .venv/bin/python3 src/atmosphere/cli.py --help
```

## Acknowledgments

- [pamixer](https://github.com/cdemoulins/pamixer) - pulseaudio mixer
- [dunst](https://dunst-project.org/) - notification daemon
- [click](https://click.palletsprojects.com/) - CLI framework
- [typer](https://typer.tiangolo.com/) - CLI framework built on top of click
- [requests](https://requests.readthedocs.io/) - HTTP library
- [wttr.in](https://wttr.in) - weather service
- [light](https://github.com/haikarainen/light) - brightness manager

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
