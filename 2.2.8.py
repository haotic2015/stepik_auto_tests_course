from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Dmitry")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Vagner")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("blabla@blabla.bla")
    input4 = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
