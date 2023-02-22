from atmosphere.core.module import AtmosphereModule
from atmosphere.modules.volume.cli import volume_cli

module = AtmosphereModule(name="volume", cli=volume_cli)
