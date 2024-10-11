#Test Case automation: run test that opens website feels in 1.5mm 5 Core Cable in search bar then finds the element on page clicks it then adds to cart clicks the pop menu that has options to go to view in cart,in new page selects check out and fill email and 6 other fields 


from ssl import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://83d8b0-75.myshopify.com/")
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, ""))
)

element = driver.find_element(By.XPATH, "//div[@id='Slide-template--18588964257956__slideshow_Y9WFh8-1']//div[@class='slideshow__text-wrapper banner__content banner__content--bottom-left page-width banner--desktop-transparent scroll-trigger animate--slide-in']//div[@class='banner__buttons']//a")
element.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Checkout-button"))
)

link = driver.find_element(By.ID, "Checkout-button")
link.click()



time.sleep(10)

driver.quit()