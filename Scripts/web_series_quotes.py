import requests

API = "https://web-series-quotes.herokuapp.com/"


def get_random_web_series_quotes(series_name: str, no_of_quotes="1") -> str:
    url = API + series_name + "/" + no_of_quotes
    res = requests.get(url)
    return res.json()

if __name__ == "__main__":
    a = input("Enter the series name: ")
    if a in ["breakingbad", "dark", "moneyheist", "gameofthrones"]:
        data = get_random_web_series_quotes(a)
        print(data['quote'])
        print(f"               -{data['author']}")
    else:
        print("Series not avilable")
