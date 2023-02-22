"""
This module contains the controller for the weather module.
"""

import logging
import subprocess

import requests

from atmosphere.modules.weather.utils import (
    get_weather_format_value,
    get_weather_unit_value,
)

from .enums import WeatherFormat, WeatherUnit

logger = logging.getLogger(__name__)

weather_api = "wttr.in"


def get_location() -> str:
    """Get the location."""
    try:
        location = subprocess.check_output(
            ["curl", "-s", "ipinfo.io/city"], universal_newlines=True
        )
        return location.strip()
    except subprocess.CalledProcessError as error:
        logger.error(error)
        return ""


def get_weather(
    location: str | None = None,
    format: WeatherFormat = WeatherFormat.CONDITION_TEMPERATURE,
    unit: WeatherUnit = WeatherUnit.METRIC,
) -> str:
    """Get the weather for a location."""
    if not location:
        location = get_location()
    try:
        format_value = get_weather_format_value(format)
        unit_value = get_weather_unit_value(unit)
        response = requests.get(
            f"https://{weather_api}/{location}?{unit_value}&format={format_value}"
        )
        return response.text
    except requests.RequestException as error:
        logger.error(error)
        return ""
