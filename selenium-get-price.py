from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from datetime import datetime

import time
import sys

DEBUG = True
DEBUG_SLEEP = 2

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
ser = Service('./chromedriver')
driver = webdriver.Chrome(service=ser, options=options)

driver.get("https://www.starlink.com")

if DEBUG: time.sleep(DEBUG_SLEEP)

address = driver.find_element(By.ID,"service-input")

address.send_keys("C3F7+CG Khmelnytskyi,  Ukraine")

if DEBUG: time.sleep(DEBUG_SLEEP)

order_now = driver.find_element(By.XPATH,"/html/body/app-root/public-header-navigation/div/mat-drawer-container/mat-drawer-content/div/app-landing/div/div[1]/div/div/div[2]/form/div[2]/button")
order_now.click()
