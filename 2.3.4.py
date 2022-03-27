from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)
    input = browser.find_element_by_id("answer")
    input.send_keys(y)
    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
