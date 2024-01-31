from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")
driver.current_url
button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")
button_press = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)
driver.quit()