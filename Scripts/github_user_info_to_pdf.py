"""
Python script generate pdf of given Github user info
"""

import requests
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
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

    def insert_image(self, path: str, width=None, height=None, hAlign="CENTER"):

        report = Image(path, width=width, height=height, hAlign=hAlign)

        return report

    def done(self, *kwgs):

        return self.report.build(list(kwgs))


def get_user_info(username: str) -> dict:
    """
    Function to call api of GitHub
    """
    api = f"https://api.github.com/users/{username}"

    return requests.get(api).json()


if __name__ == "__main__":
    username = input("Enter the username: ")
    data = get_user_info(username)
    pdf = PdfGenerator(f"{username}.pdf")
    a = pdf.set_title(data["login"])
    b = pdf.set_title(data["name"], tag="h3")
    c = pdf.insert_image(data["avatar_url"], width=100, height=100, hAlign="RIGHT")
    table = [
        ["Location", data["location"]],
        ["Hireable", data["hireable"]],
        ["Bio", data["bio"]],
        ["Twitter", data["twitter_username"]],
        ["Repos", str(data["public_repos"])],
        ["Gists", str(data["public_gists"])],
        ["Followers", str(data["followers"])],
        ["Followings", str(data["following"])],
    ]
    d = pdf.set_table(table)
    pdf.done(a, b, c, d)
