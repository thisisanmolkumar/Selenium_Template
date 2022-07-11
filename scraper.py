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

links = ['https://ukutabs.com/p/plain-white-ts/hey-there-delilah/?transpose=-2',
         'https://ukutabs.com/f/frank-sinatra/fly-me-to-the-moon-two/',
         'https://ukutabs.com/c/coldplay/the-scientist/',
         'https://ukutabs.com/b/beabadoobee/coffee-two/?transpose=+5',
         'https://ukutabs.com/j/jason-mraz/im-yours/',
         'https://ukutabs.com/f/finneas/lets-fall-in-love-for-the-night/',
         'https://ukutabs.com/c/cristin-milioti/la-vie-en-rose-two/',
         'https://ukutabs.com/t/twenty-one-pilots/cant-help-falling-in-love/',
         'https://ukutabs.com/v/vance-joy/riptide/?transpose=+1',
         'https://ukutabs.com/r/radiohead/creep/']

data = []
for link in links:
    driver.get(link)
    sleep(2)
    data.append(driver.find_element(By.XPATH, '//pre[@id="ukutabs-song"]').text)

driver.close()

with open('chords.txt', 'w') as file:
    file.write('\n\n============================================================NEXT SONG============================================================\n\n'.join(data))