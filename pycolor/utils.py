"""
Misc helper functions.
"""
import colorsys


def hex_to_rgb(color):
    """Convert a hex color to rgb."""
    return tuple(bytes.fromhex(color.strip("#")))


def rgb_to_hex(color):
    """Convert an rgb color to hex."""
    return "#%02x%02x%02x" % (*color,)


def rbg_to_yiq(color):
    """Sort a ist of colors."""
    return colorsys.rgb_to_yiq(*hex_to_rgb(color))


def darken_color(color, amount):
    """Darken a hex color."""
    color = [int(col * (1 - amount)) for col in hex_to_rgb(color)]
    return rgb_to_hex(color)


def lighten_color(color, amount):
    """Lighten a hex color."""
    color = [int(col + (255 - col) * amount) for col in hex_to_rgb(color)]
    return rgb_to_hex(color)
