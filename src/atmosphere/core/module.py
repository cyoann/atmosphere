from typer import Typer


class AtmosphereModule:
    """Base class for Atmosphere modules.

    Atmosphere modules are defined by subclasses of this class. Each module
    defines a set of periodic tasks that are executed by background threads.

    """

    def __init__(self, name: str, cli: Typer):
        """Initialize the module.
        :param name: The name of the module.
        :param cli: The Typer application.
        """
        self.name = name
        self.cli = cli

    def register(self, main_cli: Typer):
        """Register the CLI commands in the Typer application."""
        main_cli.add_typer(self.cli, name=self.name)
