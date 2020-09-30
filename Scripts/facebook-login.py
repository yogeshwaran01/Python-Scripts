#!/usr/bin/python3

import getpass

from selenium import webdriver

PATH = "/usr/bin/google-chrome"  # change your path

user = input("UserName:")
passwd = getpass.getpass("Password:", stream=None)

browser = webdriver.Chrome(executable_path=PATH)

website_URL = "https://www.facebook.com/"
browser.get(website_URL)

element_email = browser.find_element_by_id("email")
element_email.clear()
element_email.send_keys(user)

element_password = browser.find_element_by_id("pass")
element_password.clear()
element_password.send_keys(passwd)

element_login_button = browser.find_element_by_id("u_0_b").click()
