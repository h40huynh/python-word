from __future__ import annotations

import os

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from io import StringIO


class ImageGenerator:
    def __init__(self, image_path: str) -> None:
        with open(image_path, "r") as f:
            self.__svg_string = f.read()

    def replace(self, find: str, replacement: str) -> ImageGenerator:
        self.__svg_string = self.__svg_string.replace(
            find, replacement)
        return self

    def to_png(self, output: str, scale: float) -> str:
        drawing = svg2rlg(StringIO(self.__svg_string))
        drawing.width, drawing.height = drawing.minWidth(
        ) * scale, drawing.height * scale
        drawing.scale(scale, scale)
        try:
            renderPM.drawToFile(drawing, output, "png")
        except:
            pass
        self.output = output
        return output

    def remove(self) -> None:
        if os.path.exists(self.output):
            os.remove(self.output)

    @staticmethod
    def clear_png(output: str) -> None:
        try:
            os.remove(output)
        except:
            pass
