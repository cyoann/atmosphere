from enum import Enum


class WeatherFormat(str, Enum):
    """The weather format."""

    LOCATION = "location"
    CONDITION = "condition"
    TEMPERATURE = "temperature"
    CONDITION_TEMPERATURE = "condition_temperature"
    FULL = "full"


class WeatherUnit(str, Enum):
    """The weather unit."""

    METRIC = "metric"
    USCS = "uscs"
    METRIC_WIND_SPEED_MS = "metric_wind_speed_ms"
