from selenium import webdriver
from selenium.webdriver.support.ui import Select

import math
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    select = Select(browser.find_element_by_tag_name("select"))

    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum_num = int(num1) + int(num2)
    select.select_by_value(str(sum_num))
    
    
    submit = browser.find_element_by_class_name("btn-default").click()

finally:
    time.sleep(10)
    browser.quit()