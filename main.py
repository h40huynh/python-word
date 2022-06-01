from modules.word.helper import WordHelper
from modules.word.paragraph import Paragraph

word = WordHelper("template.docx")

# Add heading
word.add_heading("Heading 1", 1)
word.add_heading("Heading 2", 2)

# Add paragraph
word.add_paragraph("This is a paragraph")
word.add_paragraph("This is another paragraph").set_style(
    "Heading 2").set_alignment("center")

# Working with run
paragraph = word.add_paragraph("This is a paragraph")
paragraph.add_run("This is a run").set_style("Heading 2 Char")
paragraph.add_run("This is another run").set_style("Heading 1 Char")

# Replace text
for paragraph in word.paragraphs:
    if "Customer_Name" in paragraph.text:
        paragraph.replace_str("Customer_Name", "John Doe")

# Replace text in tables
for table in word.tables:
    paragraphs = table.to_paragraphs()
    for paragraph in paragraphs:
        if "Table_Key" in paragraph.text:
            paragraph.replace_str("Table_Key", "John Doe")

# Add table row
table = word.tables[0]
row = table.add_row()
cell = row.cells[0]
paragraph = Paragraph(cell.paragraphs[0])
paragraph.add_run("New Row")
paragraph = Paragraph(cell.add_paragraph("Text"))
paragraph.add_run("New Row")

cell = row.cells[1]
paragraph = Paragraph(cell.paragraphs[0])
paragraph.add_run("New Row")
paragraph = Paragraph(cell.add_paragraph(""))
paragraph.add_run("New Row")

word.save("output.docx")
