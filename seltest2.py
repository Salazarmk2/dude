from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Search for something (replace with your search query)
search_query = "selenium tutorial"
driver.find_element_by_name("q").send_keys(search_query)
driver.find_element_by_name("q").submit()

# Loop through the first 4 search results
for i in range(4):
    # Wait for the search results to load
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
    )

    # Click on the first link of the current search result
    link = search_results[i].find_element(By.NAME,"a")
    link.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.title_contains(search_query))

    # Go back to the Google search results page
    driver.back()

    # Wait for the search results page to load again
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
    )

# Close the browser
driver.quit()
