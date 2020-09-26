from instagramy import Instagram # pip install instagramy
import sys
import requests
import webbrowser # pip install webbrowser
"""
    Usage: python instagram_dp.py <username>
    package_used: https://github.com/yogeshwaran01/instagramy visit is page to get more usage about package
    Author: YOGESHWARAN R

"""


def get_dp(username):
    """
    Funtion to get dp url of the username
    """
    try:
        user = Instagram(username)
        dp_url = user.get_profile_pic()
        return dp_url
    except:
        print("Url not found")
        return None

def download(username):
    """
    Funtion to download the dp
    """
    dp_url = get_dp(username)
    file_name = "{}.jpeg".format(username)
    r = requests.get(dp_url,stream=True)
    if r.ok:
        file = open(file_name,"wb")
        file.write(r.content)
        print("{}'s dp downloaded!".format(username))
    else:
        print("Check your internet connection")

def opener(username):
    """
    Funtion to open dp in default webbrowser
    """
    url = get_dp(username)
    print("{}'s dp is opening...".format(username))
    webbrowser.open(url)

if __name__ == '__main__':
    username = sys.argv[1]
    prompt = """

    [1] Download
    [2] Open

    """
    print(prompt)
    option = str(input(">>> "))
    if option == "1":
        download(username)
    elif option == "2":
        opener(username)
    else:
        print("press 1 or 2")
        sys.exit()
