from selenium import webdriver

# метод позволяет задать ожидание при инициализации драйвера
# implicitly_wait(5)
try:
    browser = webdriver.Chrome()

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")
    button.click()
finally:
    browser.quit()
# message = browser.find_element_by_id("verify_message")

# assert "successful" in message.text
