from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

driver.find_element(By.ID, "Form_submitForm_subdomain").send_keys("phanivarmabh")
driver.find_element(By.NAME, "FirstName").send_keys("Phani")
driver.find_element(By.NAME, "LastName").send_keys("Varma")
driver.find_element(By.XPATH, '//input[@id="Form_submitForm_Email"]').send_keys("phani@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#Form_submitForm_JobTitle").send_keys("SSE")
driver.find_element(By.LINK_TEXT, "Platform").click()

time.sleep(5)
driver.quit()
