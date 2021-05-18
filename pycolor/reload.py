"""
Reload programs.
"""
import logging
import os
import shutil
import subprocess

from .settings import CACHE_DIR, MODULE_DIR, OS
from . import utils



def tty(tty_reload):
    """Load color in tty."""
    tty_script = os.path.join(CACHE_DIR, "colors-tty.sh")
    term = os.environ.get("TERM")

    if tty_reload and term == "linux":
        subprocess.Popen(["sh", tty_script])
