from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Image
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

    def set_title(self, main_title: str, tag=None):
        if tag:
            report = Paragraph(main_title, self.styles[tag])
        else:
            report = Paragraph(main_title, self.styles["h1"])

        return report

    def set_paragragh(self, paragraph: str):

        report = Paragraph(paragraph, self.styles["BodyText"])

        return report

    def set_table(self, table_data: list):
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
    c = pdf.set_title("Uses of Python", tag="h3")
    table_data = [
        ["Modules", "Uses"],
        ["Requests", "Talk to http protocol"],
        ["Flask", "Web framework"],
        ["Pygame", "Build Game for life"],
        ["Bs4", "Scarpe the Website"],
        ["Matplotlib", "Plot the data"],
        ["Pandas", "Frame the Data"],
    ]
    d = pdf.set_table(table_data)
    pdf.done(a, b, c, d)
