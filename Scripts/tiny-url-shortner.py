from requests import post


def TinyShortner(big_url: str) -> str:
    """
    Funtion short the big urls to tiny by Tiny Api
    """
    return post("https://tinyurl.com/api-create.php", data={"url": big_url}).text


if __name__ == "__main__":
    url = input("Enter the Big Url to short: ")
    print(TinyShortner(url))
