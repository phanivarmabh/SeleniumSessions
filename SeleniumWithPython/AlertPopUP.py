from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")


singin_ele = driver.find_element(By.NAME, "proceed")
singin_ele.click()

alert_ele = driver.switch_to.alert
print(alert_ele.text)
alert_ele.accept() #accept it, click on Ok
#
alert_ele.dismiss() #cancel the pop up

time.sleep(3)
driver.quit()


