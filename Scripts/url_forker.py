import re
import sys
import webbrowser
from urllib.parse import urljoin

import bs4 as bs
import requests
from fake_useragent import UserAgent
from tqdm import tqdm

headers = {"UserAgent": UserAgent().random}


def is_valid(url):
    """
    Funtion that vaild the url
    """

    try:
        regex = re.compile(
            r"^(?:http|ftp)s?://"
            r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"
            r"localhost|"
            r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
            r"(?::\d+)?"
            r"(?:/?|[/?]\S+)$",
            re.IGNORECASE,
        )
        return re.match(regex, url) is not None
    except:
        return True


def download(url):
    get_response = requests.get(url, stream=True)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as f:
        for chunk in tqdm(get_response.iter_content(chunk_size=1024)):
            if chunk:
                f.write(chunk)


def get_links(url):
    """
    Funtion get all links in website
    """

    r = requests.get(url, headers=headers)
    soup = bs.BeautifulSoup(r.text, "html.parser")
    try:
        links = soup.find_all("a")
    except:
        print("\nNo links Found\n")
        sys.exit()
    data = [link.get("href") for link in links]
    final = []
    for link in data:
        if is_valid(link):
            a = link
        else:
            a = urljoin(url, link)
        final.append(a)
    return final


def main(links):
    """
    Funtion that loop through
    the url and open in browser
    and dowload the files from
    website
    """

    while True:
        count = 0
        for link in links:
            count = count + 1
            print("[{}] {}".format(count, link))

        valve = input("\n>>> ")
        if valve == "save":
            a = int(input("\n(save)>>>"))
            valve = int(a)
            download(links[valve - 1])
            print("Downloaded!")
            sys.exit(0)
        elif valve == "open":
            try:
                a = int(input("\n(open)>>>"))
                valve = int(a)
                webbrowser.open(links[valve - 1])
                continue
            except:
                print("Unabe to open")
                continue
        else:
            try:
                valve = int(valve)
            except:
                print("use integer or save for download or open for open in webbrowser")
                sys.exit()
        try:
            print("\nForking {}...\n".format(links[valve - 1]))
            links = get_links(links[valve - 1])
        except:
            continue


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except:
        url = str(input("Enter the url to Fork: "))
    if url[-1] == "/":
        url = url[:-1]
    else:
        pass
    if is_valid(url):
        print("\nForking {}...\n".format(url))
        main(get_links(url))
    else:
        print("\nInvalid Url\n")
