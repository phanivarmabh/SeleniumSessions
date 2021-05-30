from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "opera"

if browsername == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browsername == "safari":
    driver = webdriver.Safari()
else:
    print("Please enter the correct browsername :" + browsername)
    raise Exception("driver is not defined")


driver.get("https://www.facebook.com/")

driver.implicitly_wait(5)
driver.find_element(By.ID, "email").send_keys("phanivarmabh@live.com")
driver.find_element(By.ID, "pass").send_keys("Test@123")
driver.find_element(By.NAME, "login").click()

print(driver.title)

time.sleep(5)
driver.quit()



