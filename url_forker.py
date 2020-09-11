import requests
import bs4 as bs
import sys
from urllib.parse import urljoin
import webbrowser
from tqdm import tqdm

def is_valid(url):
    import re
    try:
        regex = re.compile(
                r'^(?:http|ftp)s?://'
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                r'localhost|'
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                r'(?::\d+)?'
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None
    except:
        return True

def download(url):
    get_response = requests.get(url, stream=True)
    file_name  = url.split("/")[-1]
    with open(file_name, 'wb') as f:
        for chunk in tqdm(get_response.iter_content(chunk_size=1024)):
            if chunk:
                f.write(chunk)

def get_links(url):
    try:
        r = requests.get(url)
    except:
        print("\nCheck Internet Connection..\n")
        sys.exit()
    soup = bs.BeautifulSoup(r.text,'html.parser')
    try:
        links = soup.find_all('a')
    except:
        print("\nNo links Found\n")
        sys.exit()
    data = []
    for link in links:
        data.append(link.get('href'))
    final = []
    for link in data:
        if is_valid(link):
            a = link
        else:
            a = urljoin(url, link)
        final.append(a)
    return final


def main(links):
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

if __name__ == '__main__':
    url = sys.argv[1]
    if url[-1] == "/":
        url = url[:-1]
    else:
        pass
    if is_valid(url):
        print("\nForking {}...\n".format(url))
        main(get_links(url))
    else:
        print("\nInvalid Url\n")
