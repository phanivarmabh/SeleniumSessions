from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")

click_ele = driver.find_element(By.CSS_SELECTOR, "span.context-menu-one.btn.btn-neutral")
act_chains = ActionChains(driver)
act_chains.context_click(click_ele).perform()

options_list = driver.find_elements(By.CSS_SELECTOR, "ul.context-menu-list.context-menu-root")
for ele in options_list:
    print(ele.text)
    if ele.text == 'Edit':
        ele.click()
        break

# options_list = driver.find_elements(By.CSS_SELECTOR, "li.context-menu-item.context-menu-icon.context-menu-icon-edit span")
# for ele in options_list:
#     print(ele.text)
#     if ele.text == 'Edit':
#         ele.click()
#         break



