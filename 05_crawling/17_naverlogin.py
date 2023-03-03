from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

url ='https://nid.naver.com/nidlogin.login'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

id=''
pw=''

# driver.find_element(By.ID,'id').send_keys(id)
# driver.find_element(By.ID,'pw').send_keys(pw)

# driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
# driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")

ele_id = driver.find_element(By.ID,'id')
ele_id.click()
pyperclip.copy(id)
ele_id.send_keys(Keys.CONTROL,'v')
time.sleep(2)

ele_pw = driver.find_element(By.ID,'pw')
ele_pw.click()
pyperclip.copy(pw)
ele_pw.send_keys(Keys.CONTROL,'v')
time.sleep(2)

time.sleep(5)
# driver.find_element(By.CLASS_NAME,'btn_login').click()
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()
time.sleep(20)