# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace these values with your Flipkart email
email = "atwaludayveer43@gmail.com"

# Setting up the webdriver
driver = webdriver.Chrome()

try:
    # Navigating to the Flipkart homepage
    driver.get("https://www.flipkart.com")
    time.sleep(8)

    # Finding the search bar and entering text
    search_bar = driver.find_element(By.NAME, "q")
    assert search_bar.is_displayed(), "Search bar not found"
    search_bar.send_keys("mobile")

    # Submitting the search query
    search_bar.send_keys(Keys.RETURN)

    # Waiting for the search results page to load
    time.sleep(7)

    # Verifying that the search results page has loaded
    #assert "mobile" in driver.title

    # Selecting a mobile from the search results using the class name
    mobile_link = driver.find_element("xpath","/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div/a/div[2]/div[1]/div/div/img")
    assert mobile_link.is_displayed(), "Mobile link not found"
    mobile_link.click()

    # Waiting for the mobile details page to load
    time.sleep(8)

    # Switching to the new tab opened
    driver.switch_to.window(driver.window_handles[1])

    # Adding the laptop to the cart
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "In9uk2")
    add_to_cart_button.click()

    # Waiting for the cart to update
    time.sleep(5)

    # Proceeding to checkout
    proceed_to_checkout = driver.find_element(By.XPATH, "//span[contains(text(), 'Place Order')]")
    assert proceed_to_checkout.is_displayed(), "Place Order button not found"
    proceed_to_checkout.click()
    time.sleep(5)

    # Logging in with email
    email_field = driver.find_element(By.XPATH, "//input[@type='text' and @class='r4vIwl Jr-g+f']")
    assert email_field.is_displayed(), "Email field not found"
    email_field.send_keys(email)
    time.sleep(5)

    # Clicking the continue button
    continue_button = driver.find_element(By.XPATH, "//button[@type='submit' and @class='QqFHMw YhpBe+ _7Pd1Fp']")
    continue_button.click()
    time.sleep(20)

    # Clicking the verify button
    verify_button = driver.find_element(By.XPATH, "//button[@type='submit' and @class='QqFHMw YhpBe+ _7Pd1Fp']")
    verify_button.click()
    time.sleep(10)

finally:
    # Closing the webdriver
    driver.quit()
