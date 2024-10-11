from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open a website
driver.get("https://example.com")

# Locators in action
element_by_id = driver.find_element(By.ID, "element_id")
element_by_name = driver.find_element(By.NAME, "element_name")
element_by_class = driver.find_element(By.CLASS_NAME, "element_class")
element_by_tag = driver.find_element(By.TAG_NAME, "div")
element_by_link_text = driver.find_element(By.LINK_TEXT, "Exact Link Text")
element_by_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, "Partial Text")
element_by_css = driver.find_element(By.CSS_SELECTOR, "div.classname > input#element_id")
element_by_xpath = driver.find_element(By.XPATH, "//div[@id='element_id']")
