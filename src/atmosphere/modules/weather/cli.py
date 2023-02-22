from typer import Option, Typer, echo

from . import controller
from .enums import WeatherFormat, WeatherUnit

weather_cli = Typer(
    help="Get the weather for a location.",
    no_args_is_help=True,
)


@weather_cli.command(
    short_help="Get the current weather.",
    help="Get the current weather.",
)
def current(
    location: str = Option(
        None,
        "--location",
        "-l",
        help="The location to get the weather for.",
    ),
    format: WeatherFormat = Option(
        WeatherFormat.CONDITION_TEMPERATURE,
        "--format",
        "-f",
        help="The format to get the weather in.",
    ),
    unit: WeatherUnit = Option(
        WeatherUnit.METRIC,
        "--unit",
        "-u",
        help="The unit to get the weather in.",
    ),
):
    """Get the current weather."""
    weather = controller.get_weather(location, format, unit)
    echo(weather)
