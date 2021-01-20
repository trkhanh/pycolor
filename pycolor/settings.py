import os
import platform

__version__ = "0.0.1"
__cache_version__ = "1.1.0"

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
XDG_CACHE_DIR = os.getenv("XDG_CACHE_HOME", os.path.join(HOME, ".cache"))
XDG_CONF_DIR = os.getenv("XDG_CONFIG_HOME", os.path.join(HOME, ".config"))

CACHE_DIR = os.getenv("PYCOLOR_CACHE_DIR", os.path.join(XDG_CACHE_DIR, "pyc"))
CONF_DIR = os.path.join(XDG_CONF_DIR, "pyc")
MODULE_DIR = os.path.dirname(__file__)

OS = platform.uname()[0]