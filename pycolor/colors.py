"""
Generate a palette using various backends.
"""
from .utils import saturate_color, darken_color, lighten_color


def generic_adjust(colors, light):
    """Generic color adjustment for themes."""
    if light:
        for color in colors:
            color = saturate_color(color, 0.60)
            color = darken_color(color, 0.5)

        colors[0] = lighten_color(colors[0], 0.95)
        colors[7] = darken_color(colors[0], 0.75)
        colors[8] = darken_color(colors[0], 0.25)
        colors[15] = colors[7]
    else:
        colors[0] = darken_color(colors[0], 0.80)
        colors[7] = lighten_color(colors[0], 0.75)
        colors[8] = lighten_color(colors[0], 0.25)
        colors[15] = colors[7]

    return colors


def saturate_colors(colors, amount):
    """Saturate all colors"""
    if amount and float(amount) <= 1.0:
        for i, _ in enumerate(colors):
            if i not in [0, 7, 8, 15]:
                colors[i] = saturate_color(colors[i], float(amount))

    return colors


