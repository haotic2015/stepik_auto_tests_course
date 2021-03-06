from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector(".trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
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
