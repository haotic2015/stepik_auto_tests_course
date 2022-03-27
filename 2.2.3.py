from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = x_element.text
    y = y_element.text
    z = str(int(x) + int(y))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
