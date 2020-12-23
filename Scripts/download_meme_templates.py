import requests
from bs4 import BeautifulSoup


def save_img(image, filename):
    file_name = "{}.jpeg".format(filename)
    r = requests.get(image, stream=True)
    if r.ok:
        file = open(file_name, "wb")
        file.write(r.content)
        return True


def get_templates(page_no):
    images = {}
    url = "https://imgflip.com/memetemplates?page={page_no}"
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    tags = soup.find_all("img", {'class': 'shadow'})
    for tag in tags:
        src = "https:" + tag.get('src')
        name = tags.get('alt') + ".jpeg"
        images["src"] = src
        images["file_name"] = name
        
    return images

if __name__ == "__main__":
    for i in range(21):
        x = get_templates(i)
        for j in x:
            save_img(j['src'], j['file_name'])
