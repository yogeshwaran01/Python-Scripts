import re

import requests


def is_valid_url(url):
    """
    Funtion Vaild the url
    """

    regex = re.compile(
        r"^(?:http|ftp)s?://"
        r"""(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"""
        r"localhost|"
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        r"(?::\d+)?"
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None


class ContactExtracter:
    """
    Class ContactExtracter extracts
    email and mobile number from the
    website and text files

    """

    def __init__(self, source: str):
        if is_valid_url(source):
            self.source = requests.get(source).text
        else:
            self.source = open(source, "r")

    @property
    def extract_email(self) -> list:
        pattern = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        result = re.findall(pattern, self.source)
        return result

    @property
    def extract_phone_number(self) -> list:
        pattern = r"""(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?"""
        result = list(
            map(
                lambda i: str(i)
                .replace("'", "")
                .replace(" ", "")
                .replace(",", "")
                .replace("(", "")
                .replace(")", ""),
                re.findall(pattern, self.source),
            )
        )
        return result


if __name__ == "__main__":
    source = input("Enter the URL or text files to extract contact: ")
    x = ContactExtracter(source)
    print(x.extract_email)
    print(x.extract_phone_number)
