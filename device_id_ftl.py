import os, json, time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as chromeopt
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_device_id():
    d = DesiredCapabilities.CHROME
    d['goog:loggingPrefs'] = {'browser': 'ALL'}
    chromeoptions = chromeopt()
    chromeoptions.add_argument('--headless')
    driver = webdriver.Chrome(desired_capabilities=d, options=chromeoptions)
    driver.get('https://www.footlocker.com/checkout')
    time.sleep(5)
    with open('device_id.json','w+') as device_json:
        json.dump({"device_id": "%s"%driver.execute_script('return _i_cr.__if_cz()'), "pxid": "%s"%driver.execute_script('return window._pxAppId')}, device_json)
    driver.quit()

get_device_id()
