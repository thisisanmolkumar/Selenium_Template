from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

links = []

data = []
for link in links:
    driver.get(link)
    sleep(2)
    data.append(driver.find_element(By.XPATH, '/body').text)

driver.close()
