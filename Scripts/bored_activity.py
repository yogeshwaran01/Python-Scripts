import requests


def get_activity():
    """
    Funtion get random activity from the Api
    """
    url = "https://www.boredapi.com/api/activity"
    return requests.get(url).json()


if __name__ == "__main__":

    data = get_activity()
    for i in data:
        print(f"{i}: {data[i]}")
