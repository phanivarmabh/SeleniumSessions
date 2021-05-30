from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)


def selectOptions(optionList, value):
    select = Select(optionList)
    select.select_by_visible_text(value)

def selectDropDownList(dropDownList, value):
    print(len(dropDownList))
    for ele in dropDownList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

indus_list = driver.find_elements(By.XPATH, "//select[@id='Form_submitForm_Industry']/option")
selectDropDownList(indus_list, "Aerospace")

country_list = driver.find_elements(By.XPATH, '//select[@id="Form_submitForm_Country"]/option')
selectDropDownList(country_list, "Indonesia")

#ele_indus = driver.find_element(By.ID, "Form_submitForm_Industry")
#select = Select(ele_indus)
#select.select_by_visible_text("Aerospace")
#selectOptions(ele_indus, "Education")

#ele_country = driver.find_element(By.ID, "Form_submitForm_Country")
#select_coun = Select(ele_country)
#select_coun.select_by_visible_text("Algeria")
#selectOptions(ele_country, "India")

# select.select_by_index(4)
# select.select_by_value("Government-National/Federal")





