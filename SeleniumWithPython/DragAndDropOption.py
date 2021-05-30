from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://jqueryui.com/resources/demos/droppable/default.html")

drag_ele = driver.find_element(By.ID, "draggable")
drop_ele = driver.find_element(By.ID, "droppable")

act_chains = ActionChains(driver)
act_chains.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()
#act_chains.drag_and_drop(drag_ele, drop_ele).perform()


time.sleep(2)
driver.quit()