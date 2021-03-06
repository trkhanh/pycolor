"""
Theme file handling.
"""
import logging
import os

from .settings import CACHE_DIR, CONF_DIR, MODULE_DIR
from .utils import read_file_json


def list_out():
    """ List all theme in pretty format"""
    dark_themes = [theme.name.replace()]


def list_themes(dark=True):
    """List all installed theme files."""
    dark = "dark" if dark else "light"
    themes = os.scandir(os.path.join(MODULE_DIR, "colorschemes", dark))
    return [t for t in themes if os.path.isfile(t.path)]


def list_themes_user():
    """List user theme files."""
    themes = [*os.scandir(os.path.join(CONF_DIR, "colorschemes/dark/")),
              *os.scandir(os.path.join(CONF_DIR, "colorschemes/light/"))]
    return [t for t in themes if os.path.isfile(t.path)]


def parse(theme_file):
    """Parse the theme file."""
    data = read_file_json(theme_file)

    if "wallpaper" not in data:
        data["wallpaper"] = "None"

    if "alpha" not in data:
        data["alpha"] =
