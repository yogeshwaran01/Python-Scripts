import sys

import bs4 as bs
import requests
from fake_useragent import UserAgent

url = "https://www.findandtrace.com/trace-mobile-number-location"

headers = {"UserAgent": UserAgent().random}


def track_phone_number(number) -> list:
    """
    Funtion that track the mobile number

    """
    data = {"mobilenumber": number, "submit": number}
    html = requests.post(url, data=data, headers=headers)
    soup = bs.BeautifulSoup(html.text, "html.parser")
    data_table = [i.text for i in soup.find_all("td")]
    table_head = [i.text for i in soup.find_all("th")]
    final = list(zip(table_head, data_table))
    final.pop(12)
    final.pop(-2)
    return final


if __name__ == "__main__":
    try:
        mobile_number = sys.argv[1]
    except (IndexError, KeyError):
        mobile_number = str(input("Enter the Mobile Number: "))
    for i in track_phone_number(mobile_number):
        print(f"{i[0]} : {i[1]} \n")
