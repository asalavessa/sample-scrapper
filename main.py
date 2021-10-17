import requests as requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.kuantokusta.pt/p/211861/msi-radeon-rx-6700-xt-mech-2x-oc-12gb-gddr6-912-v398-005?queryID=c50768cb791a0a24a702248acf7db6db&sort=1'

driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds


driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection').click()

prices = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div/div/div/div[5]/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div').text

requests.get("https://api.telegram.org/bot2096239060:AAGrLdvRJSdenZ1iU-ojKW3b1Gv54hNwp2w/sendMessage?chat_id=1626467621&text={}".format(prices))


