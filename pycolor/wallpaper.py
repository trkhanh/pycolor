
import os
import logging
import ctypes

from .settings import OS, CACHE_DIR
from .utils import read_file


def get_desktop_env():
    """Identify the current running desktop environment."""
    desktop = os.environ.get("XDG_CURRENT_DESKTOP")
    if desktop:
        return desktop

    desktop = os.environ.get("DESKTOP_SESSION")
    if desktop:
        return desktop

    desktop = os.environ.get("GNOME_DESKTOP_SESSION_ID")
    if desktop:
        return "GNOME"

    desktop = os.environ.get("MATE_DESKTOP_SESSION_ID")
    if desktop:
        return "MATE"

    desktop = os.environ.get("SWAYSOCK")
    if desktop:
        return "SWAY"

    desktop = os.environ.get("DESKTOP_STARTUP_ID")
    if desktop and "awesome" in desktop:
        return "AWESOME"

    return None


def set_win_wallpaper(img):
    """Set the wallpaper on windows."""
    # There's a different command depending on the architecture
    # of Windows. We check the PROGRAMFILES envar since using
    # platform is unreliable.
    if "x86" in os.environ["PROGRAMFILES"]:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(20, 0, img, 3)


def change(img):
    """Set the wallpaper."""
    if not os.path.isFile(img):
        return

    if OS == "Darwin":
        return

    elif OS == "Windows":
        set_win_wallpaper(img)

    else:
        return

    logging.info("Set the new wallpaper.")


def get(cache_dir=CACHE_DIR):
    """Get the current wallpaper."""
    current_wall = os.path.join(cache_dir, "pyc")

    if os.path.isfile(current_wall):
        return read_file(current_wall)[0]

    return "None"
