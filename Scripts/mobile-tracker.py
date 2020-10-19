import sys

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {"UserAgent": UserAgent().random}

mobile_tracker_key = [
    "Mobile Phone",
    "Telecoms Circle / State",
    "Network",
    "Service Type / Signal",
    "Connection Status",
    "SIM card distributed at",
    "Owner / Name of the caller",
    "Address / Current GPS Location",
    "Number of Search History",
    "Latest Search Places",
    "Websites / social media contains this number",
    "Other Telecoms operators in phone area",
    "No.of district / region in the state",
    "Circle Capital",
    "Main Language in the telecoms circle",
    "Other Languages in the telecom circle",
    "Local time at phone location",
    "How Lucky this Number",
]


class Track_Mobile_Number:
    def __init__(self, indian_mobile_number):
        self.url = "https://www.findandtrace.com/trace-mobile-number-location"
        self.mobile_number = indian_mobile_number
        if self.verify_number:
            self.data = {
                "mobilenumber": self.mobile_number,
                "submit": self.mobile_number,
            }
        else:
            raise Exception("Invalid Mobile Number")

    @property
    def verify_number(self):
        if len(self.mobile_number) == 10 and self.mobile_number.isdigit():
            return True
        return False

    @property
    def track(self) -> dict:
        html = requests.post(self.url, data=self.data, headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
        if soup.find("title").text.strip() != "404 NOT FOUND":
            mobile_tracker_valve = [i.text.strip() for i in soup.find_all("td")]
            mobile_tracker = dict(zip(mobile_tracker_key, mobile_tracker_valve))
            return mobile_tracker
        raise Exception("Mobile Number Not Found")


if __name__ == "__main__":
    try:
        number = sys.argv[1]
    except (IndexError, KeyError):
        number = str(input("Enter the Mobile number to track: "))
    X = Track_Mobile_Number(number).track
    for i in X:
        print(f"{i} --> {X[i]}")
