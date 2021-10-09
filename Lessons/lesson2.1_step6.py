from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input_1 = browser.find_element_by_id("answer")
    input_1.send_keys(y)

    checkbox = browser.find_element_by_id('robotCheckbox').click()
    radiobutton = browser.find_element_by_css_selector("[value='robots']").click()
    submit = browser.find_element_by_class_name("btn-default").click()

finally:
    time.sleep(10)
    browser.quit()