from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from math import log, sin

def calc(x):
  return str(log(abs(12*sin(x))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100")
        )
    browser.find_element(By.ID, "book").click()
   
    
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