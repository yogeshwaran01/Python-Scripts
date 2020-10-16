import re

from requests import get

def get_my_ip():
    """
    Funtion to get current ip in Network
    """
    
    url = "http://checkip.dyndns.com/"
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(get(url).text).group(1)

def get_ip_info(ip):
    """
    Function to get info about any ip
    """
    
    url = f'http://ipinfo.io/{ip}/json'
    return get(url).json()

if __name__ == "__main__":
    info = get_ip_info(get_my_ip())
    for i in info:
        print(f'{i}: {info[i]}')