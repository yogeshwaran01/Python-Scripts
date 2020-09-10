"""
    Author: Yogeshwaran R
    Description: Extract E-mail and Phone Number
                 from website and textfiles
    python extract-contact.py <filename>
    python extract-contact.py <website> <0> or <1>
    <0> =  website not get open
    <1> =  website  get open
    (Chrome driver must be install at current location")

"""
# You can change this path Here

PATH_TO_DRIVER = "C: \Program Files(x86)\Google\Chrome\chromedriver.exe"

# Importing required Modules
import re
import sys
import bs4 as bs
import requests
import urllib.request
import ssl

#ssl certify
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#funtion to extract phone numbers
def phone(text):
    pattern = '(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'
    result = re.findall(pattern,text)
    return result

#funtion to extract email-address
def email(text):
    pattern = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
    result = re.findall(pattern,text)
    return result


try:
    url = sys.argv[1] #input for cmd arguement
    if sys.argv[2] == "1":
        try:
            from selenium import webdriver
        except ImportError as e:
            print("No selenium Found")
        try:
            try: # for windows
                driver = webdriver.Chrome(executable_path=PATH) 
            except: 
                print("No driver for chrome found")
            finally:    
                driver.get(url)
                html = driver.page_source
                print("Extracted Phone Numbers from",url)
                for i in phone(html):
                    print(str(i).replace("'","").replace(" ","").replace(",",""))
                print("Extracted E-mail address from",url)
                for j in email(html):
                    print(j)
        except:
            print("Acess Denied")
        
    elif sys.argv[2] == "0":
        try:
            source=urllib.request.urlopen(url).read()

            soup=bs.BeautifulSoup(source,'html.parser')
            print("Extracted Phone Numbers from",url)
            for i in phone(soup.text):
                print(str(i).replace("'","").replace(" ","").replace(",",""))
            print("Extracted E-mail address from",url)
            for j in email(soup.text):
                print(j)
        except urllib.error.HTTPError:
            print("Acess Denied")
        
    else:
        print("Unexcepted Arguements")
        # if arguement is not url it is file
except ValueError and IndexError:
    file = open(sys.argv[1],"r")

    for line in file:
        for i in phone(line):
            print(str(i).replace("'","").replace(" ","").replace(",",""))
        for j in email(line):
            print(j)    
