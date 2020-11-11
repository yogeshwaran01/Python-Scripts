"""
Description:
-----------
    This Script Mask the url with given and Keyword

Usage:
-----
    python3 maskphish.py 
    
"""

from urllib.parse import urlparse

from requests import post


def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://da.gd/s/?url={big_url}").text


def MaskPish(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    target = input("Enter the Phishing url (With http or https): ")
    domain = input("Enter the domain name to mask Phishing url (With http or https): ")
    keyword = input("Enter the keywords (use '-' instead of whitespace): ")
    print(f"\033[91m {MaskPish(target, domain, keyword)}\033[00m")
