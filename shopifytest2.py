from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from selenium.webdriver.common.by import By

import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



try:
    driver = webdriver.Chrome()
except WebDriverException as e:
    logger.error(f"Failed to initialize Chrome driver: {e}")
    exit(1)

# Open the website
try:
    driver.get("https://83d8b0-75.myshopify.com/")
    driver.maximize_window()

except TimeoutException as e:
    logger.error(f"Failed to open website: {e}")
    driver.quit()
    exit(1)

# Find the search bar and enter the search query
try:
    search_bar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search']")))
    search_bar.click()
    logger.info("Search bar clicked")
except TimeoutException as e:
    logger.error(f"Failed to find search bar: {e}")
    driver.quit()
except NoSuchElementException as e:
    logger.error(f"Search bar not found: {e}")
    driver.quit()
    
try:
    search_bar = driver.find_element(By.CLASS_NAME("search__input field__input"))
    search_bar.send_keys("1.5mm 5 Core Cable")
    search_bar.submit(5)

except NoSuchElementException as e:
    logger.error(f"Failed to find search bar: {e}")
    driver.quit(5)
    exit(5)

# Wait for the search results to load
try:
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.search-result"))
    )
except TimeoutException as e:
    logger.error(f"Failed to load search results: {e}")
    driver.quit(5)
    exit(5)

# Click on the first search result
try:
    search_results[0].click()
except IndexError as e:
    logger.error(f"Failed to click on search result: {e}")
    driver.quit()
    exit(1)

# Wait for the product page to load
try:
    product_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-page"))
    )
except TimeoutException as e:
    logger.error(f"Failed to load product page: {e}")
    driver.quit()
    exit(1)

# Click the "Add to cart" button
try:
    add_to_cart_button = product_page.find_element(By.CSS_SELECTOR("button.add-to-cart"))
    add_to_cart_button.click()
except NoSuchElementException as e:
    logger.error(f"Failed to find 'Add to cart' button: {e}")
    driver.quit()
    exit(1)

# Wait for the popup menu to appear
try:
    popup_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.popup-menu"))
    )
except TimeoutException as e:
    logger.error(f"Failed to load popup menu: {e}")
    driver.quit()
    exit(1)

# Click the "View in cart" option
try:
    view_in_cart_option = popup_menu.find_element(By.CSS_SELECTOR("a.view-in-cart"))
    view_in_cart_option.click()
except NoSuchElementException as e:
    logger.error(f"Failed to find 'View in cart' option: {e}")
    driver.quit()
    exit(1)

# Wait for the cart page to load
try:
    cart_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.cart-page"))
    )
except TimeoutException as e:
    logger.error(f"Failed to load cart page: {e}")
    driver.quit()
    exit(1)

# Click the "Checkout" button
try:
    checkout_button = cart_page.find_element(By.CSS_SELECTOR("button.checkout"))
    checkout_button.click()
except NoSuchElementException as e:
    logger.error(f"Failed to find 'Checkout' button: {e}")
    driver.quit()
    exit(1)

# Wait for the checkout page to load
try:
    checkout_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.checkout-page"))
    )
except TimeoutException as e:
    logger.error(f"Failed to load checkout page: {e}")
    driver.quit()
    exit(1)

# Fill in the email and other fields
try:
    email_field = checkout_page.find_element(By.NAME("email"))
    email_field.send_keys("example@example.com")

    other_fields = [
        ("name", "John Doe"),
        ("address", "123 Main St"),
        ("city", "Anytown"),
        ("state", "CA"),
        ("zip", "12345"),
        ("phone", "555-555-5555")
    ]

    for field, value in other_fields:
        field_element = checkout_page.find_element(By.NAME(field))
        field_element.send_keys(value)
except NoSuchElementException as e:
    logger.error(f"Failed to find field: {e}")
    driver.quit()
    exit(1)

# Close the browser
driver.quit()