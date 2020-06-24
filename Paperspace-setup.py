from selenium import webdriver
import time
import os

url = 'https://www.paperspace.com/console/account/api'

email = 'quilocs@gmail.com'
pspacePass = 'TestingPassword'

apiName = 'Test'
apiDesc = 'Testing generating API Key automatically'

#########

driver = webdriver.Chrome('/Users/Aidan/Documents/Challenges/chromedriver')
driver.get(url)


emailBox = driver.find_element_by_id('input-email')
emailBox.send_keys(email)

passBox = driver.find_element_by_id('input-password')
passBox.send_keys(pspacePass)

driver.find_element_by_id('button-login').click()

time.sleep(2)

nameBox = driver.find_element_by_id('input-name')
nameBox.send_keys(apiName)

nameBox = driver.find_element_by_id('input-description')
nameBox.send_keys(apiDesc)

driver.find_element_by_xpath('//*[@type="submit"]').click()

time.sleep(2)

apiKeyy = driver.find_element_by_xpath('//*[@class="referralCodeDiv"]').get_attribute("data-clipboard-text")

os.system("gradient apiKey " + apiKeyy)

## - First time setup - What machine and container to use etc. Upload model to this after
 