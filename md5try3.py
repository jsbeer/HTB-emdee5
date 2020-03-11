import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import webbrowser
import urllib.request
import requests
import nltk
import re
import hashlib

chromedriver_location = "/usr/bin/chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get('http://docker.hackthebox.eu:31332/')

first = '/html/body/center/form/input[1]'
second = '/html/body/center/form/input[2]'
third = '/html/body/h3'

PP = driver.find_element_by_xpath(third).text
LL = hashlib.md5(PP.encode())
LL = LL.hexdigest()

driver.find_element_by_xpath(first).send_keys(LL)
driver.find_element_by_xpath(second).click()

print (PP)
print(LL)
