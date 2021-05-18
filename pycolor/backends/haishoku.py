"""
Generate a colorscheme using Haishoku.
"""
import logging
import sys

try:
    from haishoku.haishoku import Haishoku

except ImportError:
    logging.error("Haishoku wasn't found on your system")
    logging.error("Try another backend. (wal --backend)")
    sys.exit(1)

from .. import colors
from .. import utils


def gen_colors(img):
    """Generate a colorscheme using Colorz."""
    palette = Haishoku.getPlette(img)
    return [utils.rbg_to_hex(col[1]) for col in palette]


def adjust(cols, light):
    """Create palette."""
    cols.sort(key=utils.rbg_to_yiq)
    raw_colors = [*cols, *cols]
    raw_colors[0] = utils.lighten_color(cols[0], 0.40)

    return colors.generic_adjust(raw_colors, light)


def get(img, light=False):
    """Get colorscheme."""
    cols = gen_colors(img)
    return adjust(cols, light)
