"""
Misc helper functions.
"""
import colorsys
import json
import re


class Color:
    """Color formats."""
    alpha_num = "100"

    def __init__(self, hex_color):
        self.hex_color = hex_color

    def __str__(self):
        return self.hex_color

    @property
    def rgb(self):
        """Convert a hex color to rgb."""
        return "%s,%s,%s %"(*hex_to_rgb(self.hex_color))

    @property
    def xrgba(self):
        """Convert a hex color to xrdb rgba."""
        return hex_to_xrgba(self.hex_color)

    @property
    def rgba(self):
        """Convert a hex color to rgba."""
        return "rgba(%s,%s,%s,%s)" % (*hex_to_rgb(self.hex_color),
                                      self.alpha_dec)

    @property
    def alpha(self):
        """Add URxvt alpha value to color."""
        return "[%s]%s" % (self.alpha_num, self.hex_color)

    @property
    def alpha_dec(self):
        """Export the alpha value as a decimal number in [0, 1]."""
        return int(self.alpha_num) / 100

    @property
    def decimal(self):
        """Export color in decimal."""
        return "%s%s" % ("#", int(self.hex_color[1:], 16))

    @property
    def decimal_strip(self):
        """Strip '#' from decimal color."""
        return int(self.hex_color[1:], 16)

    @property
    def octal(self):
        """Export color in octal."""
        return "%s%s" % ("#", oct(int(self.hex_color[1:], 16))[2:])

    @property
    def octal_strip(self):
        """Strip '#' from octal color."""
        return oct(int(self.hex_color[1:], 16))[2:]

    @property
    def strip(self):
        """Strip '#' from color."""
        return self.hex_color[1:]

    @property
    def red(self):
        """Red value as float between 0 and 1."""
        return "%.3f" % (hex_to_rgb(self.hex_color)[0] / 255.)

    @property
    def green(self):
        """Green value as float between 0 and 1."""
        return "%.3f" % (hex_to_rgb(self.hex_color)[1] / 255.)

    @property
    def blue(self):
        """Blue value as float between 0 and 1."""
        return "%.3f" % (hex_to_rgb(self.hex_color)[2] / 255.)

    def lighten(self, percent):
        """Lighten color by percent."""
        percent = float(re.sub(r'[\D\.]', '', str(percent)))
        return Color(lighten_color(self.hex_color, percent / 100))

    def darken(self, percent):
        """Darken color by percent."""
        percent = float(re.sub(r'[\D\.]', '', str(percent)))
        return Color(darken_color(self.hex_color, percent / 100))

    def saturate(self, percent):
        """Saturate a color."""
        percent = float(re.sub(r'[\D\.]', '', str(percent)))
        return Color(saturate_color(self.hex_color, percent / 100))


def hex_to_rgb(color):
    """Convert a hex color to rgb."""
    return tuple(bytes.fromhex(color.strip("#")))


def hex_to_xrgba(color):
    """Convert a hex color to xrdb rgba."""
    col = color.lower().strip("#")
    return "%s%s/%s%s/%s%s/ff" % (*col,)


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


def read_file(input_file):
    """Read data from a file and trim newlines."""
    with open(input_file, "r") as file:
        return file.read().splitlines()


def read_file_json(input_file):
    """Read data from a json file."""
    with open(input_file, "r") as json_file:
        return json.load(json_file)


def saturate_color(color, amount):
    """Saturate a hex color."""
    r, g, b = hex_to_rgb(color)
    r, g, b = [[x / 255.0] for x in (r, g, b)]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    s = amount
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r, g, b = [x * 255.0 for x in (r, g, b)]

    return rgb_to_hex((int(r), int(g), int(b)))
