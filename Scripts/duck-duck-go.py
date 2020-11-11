from urllib.parse import quote_plus
import requests


class DuckDuckGO:

    url = "https://api.duckduckgo.com/?q={}&format=json"

    def __init__(self, query: str):
        self.query = quote_plus(query)
        self.url = self.url.format(self.query)
        self.data = self.get_json()

    def get_json(self):

        return requests.get(self.url).json()

    @property
    def AbstractText(self):

        return self.data["AbstractText"]

    @property
    def AbstractSource(self):

        return self.data["AbstractSource"]


if __name__ == "__main__":

    query = input("Enter the Query: ")

    a = DuckDuckGO(query)

    print(f"Source: {a.AbstractSource}" + "\n")
    print(a.AbstractText)
