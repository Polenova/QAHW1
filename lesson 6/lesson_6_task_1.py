from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")
driver.current_url
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
wait = WebDriverWait(driver, 16).until(EC.presence_of_element_located(((By.CSS_SELECTOR, "p.bg-success"))))
load_text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(load_text)
driver.quit()