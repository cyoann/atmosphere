from typer import Typer

from atmosphere.core.module import AtmosphereModule
from atmosphere.modules.brightness import module as brightness_module
from atmosphere.modules.volume import module as volume_module

__all__: list[str] = [
    "brightness_module",
    "volume_module",
]


def register(cli: Typer) -> None:
    """Register all modules to the CLI."""
    for module_name in __all__:
        module: AtmosphereModule = globals()[module_name]
        module.register(cli)
