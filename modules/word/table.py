from typing import Any
from modules.word.paragraph import Paragraph


class Table:
    def __init__(self, table) -> None:
        self.__table = table
        self.rows = self.__table.rows

    def remove_row(self, row_index: int) -> None:
        self.__table._tbl.remove(self.__table.rows[row_index]._tr)

    def add_row(self) -> Any:
        return self.__table.add_row()

    def to_paragraphs(self) -> list[Paragraph]:
        paragraphs = []
        for row in self.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    paragraphs.append(Paragraph(paragraph))
        return paragraphs
