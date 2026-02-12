"""
picascii_ansi.py

Converts an input image to a text representation using ANSI escape sequences.
Each pixel is rendered as a colored space (background color) so the output file can be
displayed in a terminal that supports 24‑bit true‑color.

Usage (similar to the other scripts in this package):
    from picascii.picascii_ansi import process
    process(input_file, output_file, max_size)

Parameters
----------
input_file: str
    Path to the source image.
output_file: str
    Path where the ANSI‑colored text will be written.
max_size: int
    Desired maximum dimension (width or height) for the resized image. The image
    will be scaled proportionally so that the larger side equals ``max_size``.

The implementation mirrors ``picascii_color.py`` but replaces the emoji palette
with true‑color ANSI background codes.
"""

import math
import io
import PIL.Image


def _scale_dimensions(original_size, max_dim):
    """Return new (width, height) scaled proportionally so that the larger
    side equals ``max_dim``."""
    width, height = original_size
    larger = max(width, height)
    if larger == 0:
        return (0, 0)
    scale = max_dim / larger
    return (int(math.floor(width * scale)), int(math.floor(height * scale)))


def process(input_file: str, output_file: str, max_size: int):
    """
    Convert ``input_file`` into an ANSI‑colored text file.

    The output consists of lines of spaces where each space's background color
    matches the corresponding pixel in the resized image.
    """
    # Load and resize the image
    img = PIL.Image.open(input_file)
    new_width, new_height = _scale_dimensions(img.size, max_size)
    img = img.resize((new_width, new_height))

    # Ensure we have RGB data (quantization is unnecessary for true‑color)
    img = img.convert("RGB")

    # Build the ANSI string line by line
    lines = []
    for y in range(img.height):
        line_parts = []
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            # 24‑bit background color, a space character, then reset.
            line_parts.append(f"\x1b[48;2;{r};{g};{b}m \x1b[0m")
        lines.append("".join(line_parts))
    txt = "\n".join(lines) + "\n"

    # Write the result to the output file using UTF‑8 encoding
    with io.TextIOWrapper(io.FileIO(file=output_file, mode="w"), encoding="utf8") as bf:
        bf.write(txt)


# ----------------------------------------------------------------------
# Author: Charles "chazz_the_intrepid" Timothy Montgomery 2023
# License: MIT (see repository root)
# ----------------------------------------------------------------------