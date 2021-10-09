from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def get_button():
    button = browser.find_element_by_class_name("btn-primary")
    return button


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = get_button().click()
    # получить содержимое alert
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    value = calc(x)

    input1 = browser.find_element_by_id("answer").send_keys(value)
    submit = get_button().click()

finally:
    time.sleep(10)
    browser.quit()
