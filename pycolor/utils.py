"""
Misc helper functions.
"""
import colorsys
import json


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


def read_file_json(input_file):
    """Read data from a json file."""
    with open(input_file, "r") as json_file:
        return json.load(json_file)


def saturate_color(color, amount):
    """Saturate a hex color."""
    r, g, b = hex_to_rgb(color)
    r, g, b = [[x/255.0] for x in (r, g, b)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    s = amount
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r, g, b = [x * 255.0 for x in (r, g, b)]

    return rgb_to_hex((int(r), int(g), int(b)))
