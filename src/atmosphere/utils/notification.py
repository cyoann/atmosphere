"""
This module contains the notify function, which is used to send notifications
to the user.
"""

import logging
import subprocess

logger = logging.getLogger(__name__)


def notify(
    title: str = "",
    text: str = "",
    urgency: str = "normal",
    timeout: int = 5000,
    icon: str = "",
    progress: int = 0,
    stack_tag: str = "",
):
    """Send a notification to the user."""
    command = ["dunstify", "-u", urgency, "-a", title, text, "-t", str(timeout)]
    if icon:
        command += ["-i", icon]
    if progress:
        command += ["-h", f"int:value:{progress}"]
    if stack_tag:
        command += ["-h", f"string:x-dunst-stack-tag:{stack_tag}"]
    try:
        subprocess.check_output(command, universal_newlines=True)
    except subprocess.CalledProcessError as error:
        logger.error(error)
