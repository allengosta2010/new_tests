from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('Test')

    lastname = browser.find_element(By.NAME, 'lastname')
    lastname.send_keys('Test')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('Test')

    file = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла