import requests
from bs4 import BeautifulSoup


def get_wearther(location):
    url = f"https://wttr.in/{location}"

    return BeautifulSoup(requests.get(url).text, "html.parser")


if __name__ == "__main__":
    location = input("Enter the Location: ")
    print(get_wearther(location=location))