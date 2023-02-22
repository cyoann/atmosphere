from typer import Argument, Option, Typer, echo

from atmosphere.modules.brightness import controller
from atmosphere.modules.brightness.config import DEFAULT_BRIGHTNESS_STEP
from atmosphere.utils.notification import notify


def notify_brightness(brightness: int | None = None):
    """Notify the user of the new brightness."""
    if brightness is None:
        brightness = controller.get_brightness()
    notify(
        title="Brightness",
        text=f"{brightness}%",
        stack_tag="brightness",
        progress=brightness,
    )


brightness_cli = Typer(
    help="Manage your computer's brightness.",
    no_args_is_help=True,
)


@brightness_cli.command()
def get(
    percent: bool = Argument(
        True, help="Show the brightness as a percentage.", show_default=False
    )
):
    """Get the brightness."""
    echo(
        f"{controller.get_brightness()}%"
        if percent
        else controller.get_brightness()
    )


@brightness_cli.command()
def set(
    brightness: int = Argument(
        ..., help="The brightness to set the brightness to.", min=0
    ),
    show_notification: bool = Argument(
        True, help="Show a notification when the brightness is set."
    ),
    verbose: bool = Argument(False, help="Show the new brightness."),
):
    """Set the brightness."""
    controller.set_brightness(brightness)
    if show_notification:
        notify_brightness(brightness)
    if verbose:
        echo(
            f"Set brightness to {brightness}%.\n"
            + f"New brightness: {controller.get_brightness()}%"
        )


@brightness_cli.command()
def increase(
    amount: int = Option(
        DEFAULT_BRIGHTNESS_STEP,
        help="The amount to increase the brightness by.",
    ),
    show_notification: bool = Argument(
        True, help="Show a notification when the brightness is increased."
    ),
    verbose: bool = Argument(False, help="Show the new brightness."),
):
    """Increase the brightness."""
    brightness = controller.increase_brightness(amount)
    if show_notification:
        notify_brightness(brightness)
    if verbose:
        echo(f"Increased brightness by {amount}%. New brightness: {brightness}%")


@brightness_cli.command()
def decrease(
    amount: int = Option(
        DEFAULT_BRIGHTNESS_STEP,
        help="The amount to decrease the brightness by.",
    ),
    show_notification: bool = Argument(
        True, help="Show a notification when the brightness is decreased."
    ),
    verbose: bool = Argument(False, help="Show the new brightness."),
):
    """Decrease the brightness."""
    brightness = controller.decrease_brightness(amount)
    if show_notification:
        notify_brightness(brightness)
    if verbose:
        echo(f"Decreased brightness by {amount}%. New brightness: {brightness}%")
