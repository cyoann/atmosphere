from .config import weather_format_values, weather_unit_values
from .enums import WeatherFormat, WeatherUnit


def get_weather_format_value(format: WeatherFormat) -> str:
    """Get the weather format value for a weather format."""
    if format == WeatherFormat.LOCATION:
        return weather_format_values["location"]
    if format == WeatherFormat.CONDITION:
        return weather_format_values["condition"]
    if format == WeatherFormat.TEMPERATURE:
        return weather_format_values["temperature"]
    if format == WeatherFormat.CONDITION_TEMPERATURE:
        return (
            weather_format_values["condition"]
            + weather_format_values["temperature"]
        )
    if format == WeatherFormat.FULL:
        return (
            weather_format_values["location"]
            + weather_format_values["condition"]
            + weather_format_values["temperature"]
        )
    return ""


def get_weather_unit_value(unit: WeatherUnit) -> str:
    """Get the weather unit value for a weather unit."""
    if unit == WeatherUnit.METRIC:
        return weather_unit_values["metric"]
    if unit == WeatherUnit.USCS:
        return weather_unit_values["uscs"]
    if unit == WeatherUnit.METRIC_WIND_SPEED_MS:
        return weather_unit_values["metric_wind_speed_ms"]
    return ""
