
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_chrome.get("https://www.ozon.ru/")
add_element = driver_chrome.find_element(By.CSS_SELECTOR, 'a.a1j.qd0')

add_element.click()
sleep(5)
driver_chrome.quit()
