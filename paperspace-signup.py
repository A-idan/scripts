from selenium import webdriver
import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


##### Automatically setup Paperspace for use with FastAI-type models #####

url = 'https://www.paperspace.com/'
url2 = 'https://www.paperspace.com/console/notebooks'

email = 'abcabcabc@gmail.com'
pspacePass = 'TestingPassword'

projectName = 'ImageClassifier'
gitName = 'A-idan'
gitURL = 'https://github.com/A-idan/paperspace'


##### Navigating to webpage #####

driver = webdriver.Chrome('/Users/Aidan/Documents/Paperspace/chromedriver')
driver.get(url)

driver.find_element_by_xpath('//*[@class="topCTA centerMobile"]').click()

time.sleep(3)

gmailEntry = driver.find_element_by_id('input-email')
gmailEntry.send_keys(email)

gmailPass = driver.find_element_by_id('input-password')
gmailPass.send_keys(pspacePass)

wait = WebDriverWait(driver, 10)
captchaWait = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@src="/images/accountconfirmwelcome3.png"]')))

print("Go and confirm the email for" + email +"!")