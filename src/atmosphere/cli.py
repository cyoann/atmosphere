"""
Main module for the atmosphere package.
"""

from __future__ import annotations

import typer

import atmosphere.modules as modules
from atmosphere import __version__

cli = typer.Typer(
    help="Atmosphere is a tool for managing your computer's environment.",
    no_args_is_help=True,
)

modules.register(cli)


@cli.command()
def version():
    """Get the version of the atmosphere package."""
    typer.echo(f"Atmosphere version: {__version__}")


def main():
    """Entry point for the atmosphere package."""
    cli()


if __name__ == "__main__":
    main()
