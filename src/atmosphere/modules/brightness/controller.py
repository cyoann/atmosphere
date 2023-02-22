"""
Brightness Controller
"""

import logging
import subprocess

logger = logging.getLogger(__name__)

brightness_control = "/usr/bin/light"


def get_brightness() -> int:
    """Get the current brightness."""
    try:
        brightness = subprocess.check_output(
            [brightness_control, "-G"], universal_newlines=True
        )
        return int(float(brightness.rstrip())) if brightness else 0
    except subprocess.CalledProcessError as error:
        logger.error(error)
        return 0


def set_brightness(brightness: int):
    """Set the brightness."""
    try:
        subprocess.check_output(
            [brightness_control, "-S", str(brightness)], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def increase_brightness(amount: int = 5):
    """Increase the brightness."""
    try:
        subprocess.check_output(
            [brightness_control, "-A", str(amount)], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def decrease_brightness(amount: int = 5):
    """Decrease the brightness."""
    try:
        subprocess.check_output(
            [brightness_control, "-U", str(amount)], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)
