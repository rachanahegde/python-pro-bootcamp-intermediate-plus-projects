from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

EMAIL = ""
PASSWORD = ""
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103291313&keywords=marketing&location=Hong%20Kong%20SAR&" \
      "sortBy=R"

chrome_driver_path = "/Users/Rachana 1/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(20)
driver.get(URL)

# Automatically Login to LinkedIn
sign_in_btn = driver.find_element_by_class_name("cta-modal__primary-btn")
sign_in_btn.click()
username_field = driver.find_element_by_id("username")
username_field.send_keys(EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(PASSWORD)
sleep(2)  # To prevent LinkedIn from thinking I'm a bot
sign_in = driver.find_element_by_class_name("login__form_action_container")
sign_in.click()

# Apply to all jobs that have 1 step applications
listings = driver.find_elements_by_class_name("jobs-search-results__list-item ")
# Click on each job on the left hand side
for listing in listings:
    sleep(1)
    try:
        listing.click()
    except NoSuchElementException and ElementClickInterceptedException:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, listing))).click()
    sleep(3)  # Wait for button to load
    try:
        apply_button = driver.find_element_by_class_name("jobs-apply-button")
        apply_button.click()
    except NoSuchElementException:
        continue
    # Fill out phone number if field is empty
    phone_number_field = driver.find_element_by_class_name("ember-text-field")
    if len(phone_number_field.text) == 0:
        phone_number_field.send_keys("0000 0000")
    submit_button = driver.find_element_by_class_name("artdeco-button--primary")
    # print(f"This is what the button says: {submit_button.text}")
    if submit_button.text == "Submit application":
        submit_button.click()
        sleep(2)
        try:
            # Close the main pop up window confirming your application
            driver.find_element_by_class_name("artdeco-modal__dismiss").click()
        except NoSuchElementException:
            # Close the smaller pop up window on the left hand side
            driver.find_element_by_class_name("artdeco-toast-item__dismiss").click()
    else:
        # Exit application if it has multiple steps and submit button can't be found
        sleep(2)
        driver.find_element_by_class_name("artdeco-modal__dismiss").click()  # Click close button
        driver.find_element_by_css_selector(".artdeco-modal__actionbar--confirm-dialog "
                                                             ".artdeco-button--primary").click()  # Click discard button

# OPTIONAL: Save job and follow company
# save_button = driver.find_element_by_class_name("jobs-save-button")
# save_button.click()
# driver.find_element_by_id("ember194").click()
# follow_button = driver.find_element_by_class_name("follow")
# follow_button.click()
