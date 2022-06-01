from __future__ import annotations
from docx.shared import Inches


class Run:
    def __init__(self, run) -> None:
        self.__run = run
        self.text = run.text

    def add_picture(self, filename: str, width: float, height: float) -> Run:
        self.__run.add_picture(filename, width=Inches(
            width), height=Inches(height))
        return self

    def set_style(self, style: str) -> Run:
        self.__run.style = style
        return self
