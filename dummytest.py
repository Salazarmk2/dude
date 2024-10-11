from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time


driver = webdriver.Chrome()

try:
   
    driver.get('https://www.youtube.com')

    
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys('wojak')
    search_box.submit()

    
    time.sleep(5) 


    first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    first_video.click()

    time.sleep(5)

    driver.get('https://www.youtube.com')

    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys('fireship')
    search_box.submit()

    time.sleep(5)

    first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
    first_video.click()

   
    time.sleep(5)  

finally:

    driver.quit()
