import os
from selenium import webdriver
import math
import time

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input2.send_keys("Ivanoff")
    input_email = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input_email.send_keys("kuporos@gmail.com")

    send_file = browser.find_element_by_id("file")
    send_file.send_keys(file_path)

    submit = browser.find_element_by_class_name("btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()
