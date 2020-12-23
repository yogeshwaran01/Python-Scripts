from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Image, ListItem
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


class PdfGenerator:
    """
    Class help to generate pdf
    """

    def __init__(self, filename: str):
        self.filename = filename
        self.report = SimpleDocTemplate(self.filename)
        self.styles = getSampleStyleSheet()
        
    def set_title(self, heading_text):
        return Paragraph(heading_text, self.styles['Title'])

    def add_italict_text(self, text):
        return Paragraph(text, self.styles['Italic'])
    
    def set_definition(self, text):
        return Paragraph(text, self.styles['Definition'])
    
    def insert_code(self, text):
        return Paragraph(text, self.styles['Code'])
    
    def set_heading(self, heading_text: str, tag=None):
        if tag:
            report = Paragraph(heading_text, self.styles[tag])
        else:
            report = Paragraph(heading_text, self.styles["h1"])

        return report

    def set_paragragh(self, paragraph: str):

        report = Paragraph(paragraph, self.styles["BodyText"])

        return report

    def insert_table(self, table_data: list):
        report = Table(
            data=table_data,
            style=[
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ],
            hAlign="CENTER",
        )

        return report

    def insert_image(self, path, width=None, height=None, hAlign="CENTER"):

        report = Image(path, width=width, height=height, hAlign=hAlign)

        return report
    
    def done(self, *kwgs):

        return self.report.build(list(kwgs))


if __name__ == "__main__":

    pdf = PdfGenerator("python.pdf")
    a = pdf.set_title("Python")
    b = pdf.set_paragragh("Python is Super")
    c = pdf.set_heading("Uses of Python", "h3")
    table_data = [
        ["Modules", "Uses"],
        ["Requests", "Talk to http protocol"],
        ["Flask", "Web framework"],
        ["Pygame", "Build Game for life"],
        ["Bs4", "Scarpe the Website"],
        ["Matplotlib", "Plot the data"],
        ["Pandas", "Frame the Data"],
    ]
    d = pdf.insert_table(table_data)
    e = pdf.set_heading("Some sample code", "h3")
    f = pdf.set_definition("Python is a Vera Level;")
    pdf.done(a, b, c, d, e, f)
