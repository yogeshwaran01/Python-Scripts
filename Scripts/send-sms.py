import requests

"""
To get api key visit
https://textbelt.com/
"""


def send_sms(number: str, message: str) -> list:
    url = "http://textbelt.com/text"
    key = "PUT API HERE"
    payload = {"number": number, "message": message, "key": key}
    response = requests.post(url, data=payload)
    return response.json()


if __name__ == "__main__":
    a = input("Enter the number: ")
    b = input("Enter the message: ")
    print(send_sms(a, b))
