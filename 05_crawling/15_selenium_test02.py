from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://www.naver.com')
search = driver.find_element(By.ID,'query')
time.sleep(5)
search.send_keys('고슴도치')
search.send_keys(Keys.ENTER)
time.sleep(5)
item = driver.find_elements(By.CSS_SELECTOR,'mark')
item[0].click()
time.sleep(5)
page = driver.page_source
print(page)
time.sleep(5)
driver.quit()