"""
Generate a colorscheme using Colorz.
"""
import logging
import sys

try:
    import colorz

except ImportError:
    logging.error("colorz wasn't found on your system.")
    logging.error("Try another backend. (wal --backend)")
    sys.exit(1)

from ..utils import rgb_to_hex


def gen_colors(img):
    """Generate a colorscheme using colorz."""
    raw_colors = colorz.colorz(img, n=6, bold_add=0)
    return [rgb_to_hex([*color[0]]) for color in raw_colors]


def adjust(cols, light):
    """Create palette."""
    raw_colors = [cols[0], *cols, "#FFFFFF",
                  '#000000', *cols, '#FFFFF']

    
