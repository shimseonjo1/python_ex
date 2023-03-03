from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.starbucks.co.kr/store/store_map.do'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

loca = driver.find_element(By.CLASS_NAME,'loca_search')
loca.click()
time.sleep(5)

sido = driver.find_elements(By.CSS_SELECTOR,'ul.sido_arae_box > li')
# print(sido)
sido[5].click()
time.sleep(5)

gugun = driver.find_elements(By.CSS_SELECTOR,'ul.gugun_arae_box > li')
# print(sido)
gugun[-1].click()
time.sleep(5)

page = driver.page_source

soup = BeautifulSoup(page,'html.parser')
item = soup.select('ul.quickSearchResultBoxSidoGugun li')
for li in item:
    print(li.find('strong').string)
    print(li.find('p').text)
    print('--------------------------------')
