import os
import re

from modules.word.helper import WordHelper
from modules.word.style import Style


class Markdown:

    @staticmethod
    def generate_paragraphs(md_string: str, word: WordHelper, finding_path: str) -> None:
        heading1_regex = r"^#\s+(.*)"
        heading2_regex = r"^##\s+(.*)"
        bold_regex = r"\*\*(.*?)\*\*"
        image_regex = r"!\[(.*?)\]\((.*?)\)"
        block_regex = r"```(.*?)```"

        for line in md_string.split("\n"):
            if re.match(heading1_regex, line):
                word.add_paragraph(re.match(heading1_regex, line).group(
                    1)).set_style(Style.ParagraphStyle("Red title"))
            elif re.match(heading2_regex, line):
                word.add_paragraph(re.match(heading2_regex, line).group(
                    1)).set_style(Style.ParagraphStyle("Red title"))
            elif re.match(image_regex, line):
                title, link = re.match(image_regex, line).groups()
                image_filename = os.path.join(
                    os.path.dirname(finding_path), link)
                if os.path.isfile(image_filename):
                    p = word.add_paragraph("").add_picture(
                        image_filename, width=7.26)
            elif re.search(bold_regex, line):
                p = word.add_paragraph("")
                matches = re.finditer(bold_regex, line)
                index = 0
                for match in matches:
                    p.add_run(line[index:match.start()])
                    p.add_run(match.group(1)).set_style(
                        Style.ParagraphStyle("Strong"))
                    index = match.end()
                p.add_run(line[index:])
            else:
                word.add_paragraph(line)
