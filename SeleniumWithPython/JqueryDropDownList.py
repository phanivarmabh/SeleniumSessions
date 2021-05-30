from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def select_list(input_list, value):
    if value[0] == 'all':
        try:
            for ele in input_list:
                ele.click()
        except Exception as e:
            print(e)
    else:
        for ele in options_list:
            print(ele.text)
            for val_list in range(len(value)):
                if ele.text == value[val_list]:
                    ele.click()
                    break


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID, "justAnInputBox").click()

time.sleep(1)
options_list = driver.find_elements(By.CSS_SELECTOR, 'span.comboTreeItemTitle')
print(len(options_list))


#value_list = ['choice 1', 'choice 2', 'choice 6 2 3']
#value_list = ['choice 3']


value_list = ['all']
select_list(options_list, value_list)

# for ele in options_list:
#     print(ele.text)
#     if ele.text == 'choice 2':
#         ele.click()
