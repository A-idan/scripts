from selenium import webdriver
import time
import os
import PySimpleGUI as sg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException

sg.theme('DarkAmber')   
layout = [  [sg.Text('This application will automatically train your Machine Learning notebook, using your specified dataset.')],
            [sg.Text('Enter your desired email:'), sg.InputText('example@gmail.com',key='input_email')],
            [sg.Text('Enter your desired password:'), sg.InputText('********',key='input_pass')],
            [sg.Text('Enter your chrome driver:'), sg.InputText(key='input_driver'), sg.FileBrowse(target='input_driver')],
            [sg.Text('Enter your notebook:'), sg.InputText(key='input_notebook'), sg.FileBrowse(target='input_notebook')],
            [sg.Text('Enter your dataset:'), sg.InputText(key='input_dataset'), sg.FileBrowse(target='input_dataset')],
            [sg.Button('Run'), sg.Button('Cancel')] ]

window = sg.Window('Machine Learning Automation Tool V1.0', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    email = values['input_email']
    pspacePass = values['input_pass']
    driver = webdriver.Chrome(values['input_driver'])
    path = values['input_notebook']
    notebook = path.rsplit('/', 1)[1]
    datasetpath = values['input_dataset']
    break

window.close()


##### Automatically setup Paperspace for use with FastAI-type models #####

url = 'https://www.paperspace.com/'
url2 = 'https://www.paperspace.com/console/notebooks'
url3 = 'https://www.paperspace.com/console/account/api'
url4 = 'https://console.paperspace.com/gradient'


options = webdriver.ChromeOptions()
driver.fullscreen_window()


##### Navigating to webpage #####

def sign_up():

    driver.get(url)

    time.sleep(3)

    driver.find_element_by_xpath('//*[@class="signup-use-email-btn w-inline-block"]').click()

    time.sleep(3)

    gmailEntry = driver.find_element_by_id('input-email')
    gmailEntry.send_keys(email)

    gmailPass = driver.find_element_by_id('input-password')
    gmailPass.send_keys(pspacePass)

    sg.popup('Complete the captcha!') 

    wait = WebDriverWait(driver, 1000)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "p-t-20")))

    confirm = sg.popup_yes_no('Did you confirm the email and verify your account?')

    if confirm == 'Yes':
        print("Confirmed!")
       
    else:
        sg.popup('Confirm the email before proceeding!') 
        sign_up()

sign_up()



##### Sign in #####
def sign_in():
    time.sleep(3)
    driver.get(url3)
    time.sleep(3)
    emailBox = driver.find_element_by_id('input-email')
    emailBox.send_keys(email)

    passBox = driver.find_element_by_id('input-password')
    passBox.send_keys(pspacePass)

    time.sleep(3)

    driver.find_element_by_id('button-login').click()

    time.sleep(3)

sign_in()

##### API Key Generation #####

def api_key():

    apiName = 'Test'
    apiDesc = 'Automatically generated API Key'

    driver.get(url3)

    time.sleep(1)

    nameBox = driver.find_element_by_id('input-name')
    nameBox.send_keys(apiName)

    nameBox = driver.find_element_by_id('input-description')
    nameBox.send_keys(apiDesc)

    driver.find_element_by_xpath('//*[@type="submit"]').click()

    time.sleep(1)

    apiKey = driver.find_element_by_xpath(
        '//*[@class="referralCodeDiv"]').get_attribute("data-clipboard-text")

    os.system("gradient apiKey " + apiKey)


api_key()

##### Setting up Notebook with FastAI container and free GPU #####

def notebook_setup():
    driver.get(url4)

    try:
        driver.get(url2)

        time.sleep(3)

        driver.find_element_by_xpath("//*[text()='All Containers']").click()

        time.sleep(2)
        
        driver.find_element_by_xpath("//*[text()='Paperspace + Fast.AI 1.0 (V3)']").click()

        time.sleep(2)

        driver.find_element_by_xpath("//*[text()='Free-GPU']").click()
        
        time.sleep(2)

        driver.find_element_by_class_name("greenActionButton").click()

    except WebDriverException:
        print("Waiting for Free GPU to become available...")
        time.sleep(5)        
        notebook_setup()


notebook_setup()


##### Uploading Notebook to Jupyter and launching #####
def upload_notebook():
    driver.get(url2) 

    time.sleep(2)

    try:
        element = WebDriverWait(driver, 200).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@class="launch-button"]')))
        element.click()
    except:
        driver.get(url2) 

    time.sleep(3)

    driver.refresh()

    time.sleep(2)

    iframe = driver.find_element_by_xpath("//iframe[@class='notebook-page-iframe']")
    driver.switch_to.frame(iframe)


    driver.find_element_by_name("datafile").send_keys(datasetpath)
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='Ok']").click()
    time.sleep(2)

    
    driver.find_element_by_xpath('//*[@class="btn btn-primary btn-xs upload_button"]').click()

    element = WebDriverWait(driver, 10000).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'TrainingData.zip')]")))

    driver.find_element_by_name("datafile").send_keys(path)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@class="btn btn-primary btn-xs upload_button"]').click()

    driver.find_element_by_id('ipython-main-app').click()

    element = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '" + notebook + "')]")))

    element.click()

    time.sleep(5)

upload_notebook()


##### Running all the cells within the notebook + exporting model #####

def run_model():

    driver.find_element_by_id('menubar').click()

    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 5)
    actions.send_keys(Keys.DOWN * 5)
    actions.perform()

    driver.find_element_by_id('run_all_cells').click()

    time.sleep(1000)

    actions.key_down(Keys.CONTROL)
    actions.send_keys("s")
    actions.key_up(Keys.CONTROL)
    actions.perform()

    time.sleep(2)

run_model()

##### Downloading model from Jupyter back onto local PC #####

def download_model():

    driver.find_element_by_xpath('//*[@title="dashboard"]').click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='/tree/data']").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "//a[@href='/edit/data/export.pkl']").click()

    time.sleep(1)

    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 3)
    actions.send_keys(Keys.DOWN * 5)
    actions.perform()

    driver.find_element_by_id('download-file').click()

download_model()
