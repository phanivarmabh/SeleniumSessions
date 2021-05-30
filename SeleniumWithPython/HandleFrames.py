from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://www.londonfreelance.org/courses/frames/index.html")

#driver.switch_to.frame(2)
#driver.switch_to.frame('main')
# frameValue = driver.find_element(By.NAME,"main")
# driver.switch_to.frame(frameValue)
#
# ele = driver.find_element(By.CSS_SELECTOR, "body > h2")
# print(ele.text)

driver.switch_to.frame('navbar')

# ele2 = driver.find_element(By.CSS_SELECTOR, 'body > h3')
# print(ele2.text)

goto_frame = driver.find_element(By.LINK_TEXT, 'HTML resources index')
goto_frame.click()

driver.switch_to.default_content()
driver.switch_to.parent_frame()

