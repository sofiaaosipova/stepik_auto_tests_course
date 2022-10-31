from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(x))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    btn = browser.find_element(By.CSS_SELECTOR, "button")
    btn.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = browser.find_element(By.ID, "input_value")
    browser.find_element(By.ID, "answer").send_keys(calc(int(x.text)))
    
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()
    
except Exception as error:
    print(f'\nПроизошла ошибка: {error}\n')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()