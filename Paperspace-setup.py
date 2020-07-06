from selenium import webdriver
import time
import os



##### Automatically setup Paperspace for use with FastAI-type models #####

url = 'https://www.paperspace.com/console/account/api'
url2 = 'https://www.paperspace.com/console/notebooks'

email = 'quilocs@gmail.com'
pspacePass = 'TestingPassword'

apiName = 'Test'
apiDesc = 'Automatically generated API Key'
nbName = 'Testing Notebook'

projectName = 'ImageClassifier'
gitName = 'A-idan'
gitURL = 'https://github.com/A-idan/paperspace'



##### Navigating to webpage #####

driver = webdriver.Chrome('/Users/Aidan/Documents/Paperspace/chromedriver')
driver.get(url)

##### Sign in #####

emailBox = driver.find_element_by_id('input-email')
emailBox.send_keys(email)

passBox = driver.find_element_by_id('input-password')
passBox.send_keys(pspacePass)

driver.find_element_by_id('button-login').click()

time.sleep(3)

##### API Key Generation #####

driver.get(url)
time.sleep(3)


nameBox = driver.find_element_by_id('input-name')
nameBox.send_keys(apiName)

nameBox = driver.find_element_by_id('input-description')
nameBox.send_keys(apiDesc)

driver.find_element_by_xpath('//*[@type="submit"]').click()

time.sleep(3)

##### Local use of API Key #####

apiKey = driver.find_element_by_xpath('//*[@class="referralCodeDiv"]').get_attribute("data-clipboard-text")

os.system("gradient apiKey " + apiKey)

##### Setting up Notebook with FastAI container and free GPU #####

driver.get(url2)

time.sleep(3)

driver.find_element_by_xpath('//*[@class="strong tab"]').click()

driver.find_element_by_xpath("//*[text()='Free-GPU']").click()

time.sleep(3)

driver.find_element_by_class_name("greenActionButton").click()

##### Creating Gradient project and linking with Github repository #####
 
os.system("gradient projects create --name " + projectName + " --repositoryName " + gitName + " --repositoryUrl " + gitURL)