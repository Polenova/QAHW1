from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# 1 Chrome *****************************************************

driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# задание 1.1 клик по кнопке и печать элементов
driver_chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_element = driver_chrome.find_element(By.CSS_SELECTOR, "button")
for i in range(5):
    i = add_element.click()

all_elements = driver_chrome.find_element(By.CSS_SELECTOR, "#elements").text
print(all_elements)

# задание 1.2 клик по кнопке без ID
driver_chrome.get("http://uitestingplayground.com/dynamicid")
dynamic_id = driver_chrome.find_element(By.CSS_SELECTOR, "button.btn-primary")
for i in range(3):
    i = dynamic_id .click()
    print("click")

# задание 1.3 Клик по кнопке с CSS-классом
driver_chrome.get("http://uitestingplayground.com/classattr")
button_css = driver_chrome.find_element(By.CSS_SELECTOR, "button.btn.class3.btn-primary.btn-test")
button_css.click()

# задание 1.4 Клик по кнопке Close
driver_chrome.get("http://the-internet.herokuapp.com/entry_ad")
button_close = driver_chrome.find_element(By.CSS_SELECTOR, "div.modal-footer")
sleep(2)
button_close.click()

# задание 1.5 Ввод, удаление, ввод
driver_chrome.get("http://the-internet.herokuapp.com/inputs")
input_number = driver_chrome.find_element(By.CSS_SELECTOR, '[type="number"]')
input_number.send_keys("1000")
input_number.clear()
input_number.send_keys("999")

# задание 1.6 Залогинить
driver_chrome.get("http://the-internet.herokuapp.com/login")
input_user = driver_chrome.find_element(By.CSS_SELECTOR, '[id="username"]')
input_user.send_keys("tomsmith")
input_password = driver_chrome.find_element(By.CSS_SELECTOR, '[id="password"]')
input_password.send_keys("SuperSecretPassword!")
button_login = driver_chrome.find_element(By.CSS_SELECTOR, 'button.radius')
button_login.click()

# 2 Firefox ************************************************

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# задание 2.1 клик по кнопке и печать элементов
driver_firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_element = driver_firefox.find_element(By.CSS_SELECTOR, "button")
for i in range(5):
    i = add_element.click()

all_elements = driver_firefox.find_element(By.CSS_SELECTOR, "#elements").text
print(all_elements)

# задание 2.2 клик по кнопке без ID
driver_firefox.get("http://uitestingplayground.com/dynamicid")
dynamic_id = driver_firefox.find_element(By.CSS_SELECTOR, "button.btn-primary")
for i in range(3):
    i = dynamic_id .click()
    print("click")

# задание 2.3 Клик по кнопке с CSS-классом
driver_firefox.get("http://uitestingplayground.com/classattr")
button_css = driver_firefox.find_element(By.CSS_SELECTOR, "button.btn.class1.btn-primary.btn-test")
button_css.click()

# задание 2.4 Клик по кнопке Close
driver_firefox.get("http://the-internet.herokuapp.com/entry_ad")
button_close = driver_firefox.find_element(By.CSS_SELECTOR, "div.modal-footer")
sleep(2)
button_close.click()

# задание 2.5 Ввод, удаление, ввод
driver_firefox.get("http://the-internet.herokuapp.com/inputs")
input_number = driver_firefox.find_element(By.CSS_SELECTOR, '[type="number"]')
input_number.send_keys("1000")
input_number.clear()
input_number.send_keys("999")

# задание 2.6 Залогинить
driver_firefox.get("http://the-internet.herokuapp.com/login")
input_user = driver_firefox.find_element(By.CSS_SELECTOR, '[id="username"]')
input_user.send_keys("tomsmith")
input_password = driver_firefox.find_element(By.CSS_SELECTOR, '[id="password"]')
input_password.send_keys("SuperSecretPassword!")
button_login = driver_firefox.find_element(By.CSS_SELECTOR, 'button.radius')
button_login.click()
