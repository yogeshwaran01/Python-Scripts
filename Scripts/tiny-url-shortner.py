from requests import post


def TinyShortner(big_url):
    """
    Funtion short the big urls to tiny by Tiny Api
    """
    return post("https://tinyurl.com/api-create.php", data={"url": big_url}).text


print(TinyShortner("https://www.python.org"))