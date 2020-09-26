import requests
import bs4 as bs
import sys

url = "https://www.findandtrace.com/trace-mobile-number-location"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


def phone_number_detail(number):
    data = {"mobilenumber": number,
            "submit": number}
    html = requests.post(url, data=data, headers=headers)
    soup = bs.BeautifulSoup(html.text, 'html.parser')
    table_data_html = soup.find_all("td")
    data_table = []
    for i in table_data_html:
        data_table.append(i.text)
    table_head_html = soup.find_all("th")
    table_head = []
    for i in table_head_html:
        table_head.append(i.text)
    final_zip = zip(table_head, data_table)
    final = list(final_zip)
    final.pop(12)
    final.pop(-2)
    for i in final:
        print("{} : {}".format(i[0], i[1]))
    return final

try:
    mobile_number = sys.argv[1]
except:
    mobile_number = str(input("Enter the Mobile Number: "))

try:
    print("Loading...")
    phone_number_detail(mobile_number)
    print(" * Operator can change, If mobile portability is availed !")
except:
    print("Not Available!")
