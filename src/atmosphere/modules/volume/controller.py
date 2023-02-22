"""
Volume Controller
"""

import logging
import subprocess

from atmosphere.modules.volume.config import DEFAULT_VOLUME_STEP

logger = logging.getLogger(__name__)

volume_control = "/usr/bin/pamixer"


def get_volume() -> int:
    """Get the current volume."""
    try:
        volume = subprocess.check_output(
            [volume_control, "--get-volume"], universal_newlines=True
        )
        return int(volume)
    except subprocess.CalledProcessError as error:
        logger.error(error)
        return 0


def set_volume(volume: int):
    """Set the volume."""
    try:
        subprocess.check_output(
            [volume_control, "--set-volume", str(volume)], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def increase_volume(amount: int = DEFAULT_VOLUME_STEP):
    """Increase the volume."""
    try:
        subprocess.check_output(
            [volume_control, "--increase", str(amount)], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def decrease_volume(amount: int = DEFAULT_VOLUME_STEP):
    """Decrease the volume."""
    try:
        subprocess.check_output(
            [volume_control, "--decrease", str(amount)], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def mute_volume():
    """Mute the volume."""
    try:
        subprocess.check_output(
            [volume_control, "--mute"], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def unmute_volume():
    """Unmute the volume."""
    try:
        subprocess.check_output(
            [volume_control, "--unmute"], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def toggle_mute():
    """Toggle mute."""
    try:
        subprocess.check_output(
            [volume_control, "--toggle-mute"], universal_newlines=True
        )
    except subprocess.CalledProcessError as error:
        logger.error(error)


def is_muted() -> bool:
    """Check if the volume is muted."""
    try:
        muted = subprocess.check_output(
            [volume_control, "--get-mute"], universal_newlines=True
        ).rstrip()
        return muted == "true"
    except subprocess.CalledProcessError as error:
        logger.error(error)
        return False


def get_volume_icon(volume: int, muted: bool = False) -> str:
    """Get the volume icon."""
    if muted:
        return ""
    if volume == 0:
        return ""
    if volume < 50:
        return ""
    return ""
