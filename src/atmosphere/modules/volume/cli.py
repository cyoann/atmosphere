from typer import Argument, Option, Typer, echo, secho

from atmosphere.modules.volume import controller
from atmosphere.modules.volume.config import (
    DEFAULT_VOLUME_MUTED_TEXT,
    DEFAULT_VOLUME_STEP,
)
from atmosphere.utils.notification import notify


def get_volume_text(volume: int, muted: bool) -> str:
    """Get the volume text."""
    return f"{volume}%" if not muted else DEFAULT_VOLUME_MUTED_TEXT


def notify_volume(
    volume: int | None = None,
    muted: bool | None = None,
):
    """Notify the user of the new volume."""
    if volume is None:
        volume = controller.get_volume()
    if muted is None:
        muted = controller.is_muted()
    notify(
        title="Volume",
        text=get_volume_text(volume, muted),
        stack_tag="volume",
        progress=volume,
    )


volume_cli = Typer(
    help="Manage your computer's volumes.",
    no_args_is_help=True,
)


@volume_cli.command(
    short_help="Set the volume.",
    help="Set the volume to a specific value.",
)
def set(
    volume: int = Argument(..., help="The volume to set the volume to.", min=0),
    show_notification: bool = Option(
        True, help="Show a notification when the volume is set."
    ),
    verbose: bool = Option(False, help="Show the new volume."),
):
    """Set the volume."""
    controller.set_volume(volume)
    if show_notification:
        notify_volume(volume)
    if verbose:
        secho(
            f"Set volume to {volume}%.\n"
            + f"New volume: {controller.get_volume()}%",
            fg="green",
        )


@volume_cli.command(
    short_help="Get the volume.",
    help="Get the volume of the computer.",
)
def get(
    percent: bool = Option(
        True, help="Show the volume as a percentage.", show_default=False
    )
):
    """Get the volume."""
    volume = str(controller.get_volume())
    if percent:
        volume += "%"
    echo(volume)


@volume_cli.command(
    short_help="Increase the volume.",
    help="Increase the volume by a specific amount.",
)
def increase(
    amount: int = Option(
        DEFAULT_VOLUME_STEP,
        help="The amount to increase the volume by.",
    ),
    verbose: bool = Option(False, help="Show the new volume."),
    show_notification: bool = Option(
        True, help="Show a notification when the volume is set."
    ),
):
    """Increase the volume."""
    controller.increase_volume(amount)
    if show_notification:
        notify_volume()
    if verbose:
        secho(
            "Increased volume by {amount}%.\n"
            + f"New volume: {controller.get_volume()}%",
            fg="green",
        )


@volume_cli.command(
    short_help="Decrease the volume.",
    help="Decrease the volume by a specific amount.",
)
def decrease(
    amount: int = Option(
        DEFAULT_VOLUME_STEP,
        help="The amount to decrease the volume by.",
    ),
    verbose: bool = Option(False, help="Show the new volume."),
    show_notification: bool = Option(
        True, help="Show a notification when the volume is set."
    ),
):
    """Decrease the volume."""
    controller.decrease_volume(amount)
    if show_notification:
        notify_volume()
    if verbose:
        secho(
            "Decreased volume by {amount}%.\n"
            + f"New volume: {controller.get_volume()}%",
            fg="green",
        )


@volume_cli.command(
    short_help="Mute the volume.",
    help="Mute the volume.",
)
def mute(
    verbose: bool = Option(False, help="Show the new state of the volume."),
    show_notification: bool = Option(
        True, help="Show a notification when the volume is set."
    ),
):
    """Mute the volume."""
    controller.mute_volume()
    if show_notification:
        notify_volume(muted=True)
    if verbose:
        secho("Muted volume", fg="green")


@volume_cli.command(
    short_help="Unmute the volume.",
    help="Unmute the volume.",
)
def unmute(
    verbose: bool = Option(False, help="Show the new state of the volume."),
    show_notification: bool = Option(
        True, help="Show a notification when the volume is set."
    ),
):
    """Unmute the volume."""
    controller.unmute_volume()
    if show_notification:
        notify_volume(muted=False)
    if verbose:
        secho("Unmuted volume", fg="green")


@volume_cli.command(
    short_help="Toggle the mute state of the volume.",
    help="Toggle the mute state of the volume.",
)
def toggle_mute(
    verbose: bool = Option(False, help="Show the new state of the volume."),
    show_notification: bool = Option(
        True, help="Show a notification when the volume is set."
    ),
):
    """Toggle the mute state of the volume."""
    controller.toggle_mute()
    if show_notification:
        notify_volume()
    if verbose:
        secho(
            f"{'Muted' if controller.is_muted() else 'Unmuted'} volume",
            fg="green",
        )
