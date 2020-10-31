import requests


def get_jokes():
    """
    Funtion get random Jokes
    """
    url = "https://programming-quotes-api.herokuapp.com/quotes/random"
    return requests.get(url).json()["en"]


if __name__ == "__main__":
    print(get_jokes())
