from selenium import webdriver
import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


##### Automatically setup Paperspace for use with FastAI-type models #####

url = 'https://www.paperspace.com/'
url2 = 'https://www.paperspace.com/console/notebooks'
url3 = 'https://www.paperspace.com/console/account/api'

email = '_________@gmail.com'
pspacePass = 'TestingPassword'

projectName = 'ImageClassifier'
gitName = 'A-idan'
gitURL = 'https://github.com/A-idan/paperspace'

driver = webdriver.Chrome('/Users/Aidan/Documents/Paperspace/chromedriver')

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']


##### Navigating to webpage #####

def sign_up():

    driver.get(url)

    driver.find_element_by_xpath('//*[@class="topCTA centerMobile"]').click()

    time.sleep(2)

    gmailEntry = driver.find_element_by_id('input-email')
    gmailEntry.send_keys(email)

    gmailPass = driver.find_element_by_id('input-password')
    gmailPass.send_keys(pspacePass)

    print("Complete the Captcha!")

    wait = WebDriverWait(driver, 120)
    wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"p-t-20")))

    confirm = input("Did you confirm the email? (y/N) ").lower()
    if confirm in yesChoice:
      driver.get(url3)

    else: 
        print ("Confirm the email before proceeding!")


sign_up()