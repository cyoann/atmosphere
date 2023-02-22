from atmosphere.core.module import AtmosphereModule
from atmosphere.modules.brightness.cli import brightness_cli

module = AtmosphereModule(name="brightness", cli=brightness_cli)
