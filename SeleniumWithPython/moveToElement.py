from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.spicejet.com/")


'''move to element'''
signup_ele = driver.find_element(By.ID, 'ctl00_HyperLinkLogin')
spiceClub_ele = driver.find_element(By.CSS_SELECTOR, "#smoothmenu1 > ul > li.li-login.float-right.tabres > ul > li:nth-child(2) > a")
member_ele = driver.find_element(By.LINK_TEXT, "Member Login")
#member_ele = driver.find_element(By.CSS_SELECTOR, "#smoothmenu1 > ul > li.li-login.float-right.tabres > ul > li:nth-child(2) > ul > li:nth-child(1) > a")

act_chains = ActionChains(driver)
act_chains.move_to_element(signup_ele).perform()
act_chains.move_to_element(spiceClub_ele).perform()

member_ele.click()


time.sleep(5)
driver.quit()
