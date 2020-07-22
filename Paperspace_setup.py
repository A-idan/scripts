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
def sign_in():
    emailBox = driver.find_element_by_id('input-email')
    emailBox.send_keys(email)

    passBox = driver.find_element_by_id('input-password')
    passBox.send_keys(pspacePass)

    driver.find_element_by_id('button-login').click()

    time.sleep(3)

sign_in()
driver.get(url)

##### API Key Generation #####
def api_key():
    
    time.sleep(3)


    nameBox = driver.find_element_by_id('input-name')
    nameBox.send_keys(apiName)

    nameBox = driver.find_element_by_id('input-description')
    nameBox.send_keys(apiDesc)

    driver.find_element_by_xpath('//*[@type="submit"]').click()

    time.sleep(3)


    apiKey = driver.find_element_by_xpath('//*[@class="referralCodeDiv"]').get_attribute("data-clipboard-text")

    os.system("gradient apiKey " + apiKey)

api_key()

##### Setting up Notebook with FastAI container and free GPU #####
def notebook_setup():
    driver.get(url2)

    time.sleep(3)

    driver.find_element_by_xpath('//*[@class="strong tab"]').click()

    driver.find_element_by_xpath("//*[text()='Free-GPU']").click()

    time.sleep(3)

    driver.find_element_by_class_name("greenActionButton").click()

notebook_setup()

##### Creating Gradient project and linking with Github repository #####

os.system('python Paperspace-notebook.py')