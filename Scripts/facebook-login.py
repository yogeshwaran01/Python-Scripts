#!/usr/bin/python3
"""
    Author: Yogeshwaran R
    Description: Login FaceBook from Command Line
    
"""
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys as ks
import getpass

PATH = "executable-path-of-chrome" # change the path of dirver

user = input("UserName:")
passwd = getpass.getpass("Password:",stream=None)

browser = webdriver.Chrome(executable_path = PATH) 

website_URL ="https://www.facebook.com/"
browser.get(website_URL) 
  
element_email = browser.find_element_by_id("email")
element_email.clear()
element_email.send_keys(user)

element_pass = browser.find_element_by_id("pass")
element_pass.clear()
element_pass.send_keys(passwd)

element_login_button = browser.find_element_by_id("u_0_b").click()
