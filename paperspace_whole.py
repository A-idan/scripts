from selenium import webdriver
import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

import Paperspace_signup as signup
import Paperspace_setup as setup
import Paperspace_notebook as notebook

##### Automatically setup Paperspace for use with FastAI-type models #####

url = 'https://www.paperspace.com/'
url2 = 'https://www.paperspace.com/console/notebooks'
url3 = 'https://www.paperspace.com/console/account/api'

email = 'abcdabcdabcd@gmail.com'
pspacePass = 'TestingPassword'

projectName = 'ImageClassifier'
gitName = 'A-idan'
gitURL = 'https://github.com/A-idan/paperspace'

driver = webdriver.Chrome('/Users/Aidan/Documents/Paperspace/chromedriver')



##### Paperspace Sign up #####

signup.sign_up()

##### API Key Generation #####

setup.api_key()

##### Setting up Notebook with FastAI container and free GPU #####

setup.notebook_setup()

##### Uploading notebook to Paperspace  #####

notebook.notebook_upload()
