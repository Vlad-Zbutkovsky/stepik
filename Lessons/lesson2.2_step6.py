from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    value = calc(x)
    button = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_id("answer").send_keys(value)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']").click()
    submit = button.click()


finally:
    time.sleep(5)
    browser.quit()
