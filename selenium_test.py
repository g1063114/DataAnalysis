from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

chrome_driver = 'C:\\Users\\g1063\\Desktop\\workspace\\da\\chromedriver.exe'
url = 'https://www.wanted.co.kr'

driver = webdriver.Chrome(chrome_driver)

driver.get(url)
time.sleep(2)

search = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/nav/ul/li[2]/a')
search.click()

src = driver.page_source
content = BeautifulSoup(src)
print(content)

time.sleep(5)

driver.close()