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

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

notebook = "MonkeyClassification.ipynb"
path = "C:/notebooks/" + notebook


##### Navigating to webpage #####

driver = webdriver.Chrome('/Users/Aidan/Documents/Paperspace/chromedriver')
driver.get(url)
driver.fullscreen_window() 

##### Sign in #####

emailBox = driver.find_element_by_id('input-email')
emailBox.send_keys(email)

passBox = driver.find_element_by_id('input-password')
passBox.send_keys(pspacePass)

driver.find_element_by_id('button-login').click()

time.sleep(3)

##### Uploading Notebook to Jupyter and launching #####
def notebook_upload():
    driver.get(url2)

    time.sleep(2)

    driver.find_element_by_xpath('//*[@class="launch-button"]').click()

    time.sleep(5)

    iframe = driver.find_element_by_xpath("//iframe[@class='notebook-page-iframe']")
    driver.switch_to.frame(iframe)

    time.sleep(2)

    driver.find_element_by_name("datafile").send_keys(path)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@class="btn btn-primary btn-xs upload_button"]').click()
    driver.find_element_by_xpath('//*[@class="btn btn-primary btn-xs upload_button"]').click()


    time.sleep(60)
    driver.find_element_by_link_text(notebook).click()

notebook_upload()



