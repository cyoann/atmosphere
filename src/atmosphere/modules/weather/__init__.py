from atmosphere.core.module import AtmosphereModule

from .cli import weather_cli

module = AtmosphereModule(name="weather", cli=weather_cli)
