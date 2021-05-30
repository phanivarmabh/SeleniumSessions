from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

driver.find_element(By.NAME, 'upfile').send_keys('E:\AWS\Task1\index.html')
driver.find_element(By.XPATH, '//input[@type="submit"]').click()
