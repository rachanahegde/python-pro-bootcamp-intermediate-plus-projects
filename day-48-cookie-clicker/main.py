from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/Users/Rachana 1/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
wait = WebDriverWait(driver, 10)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie
cookie = driver.find_element_by_id("cookie")

# money = int(driver.find_element_by_id("money").text.replace(",", ""))

# Set up the timer to end loop after 5 minutes
timeout = 60 * 5
timeout_start = time.time()
check_upgrade = timeout_start + 15

upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma",
               "buyCursor"]

while time.time() < timeout_start + timeout:
    try:
        cookie.click()
    except StaleElementReferenceException and AttributeError and WebDriverException:
        wait.until(EC.element_to_be_clickable((By.ID, 'cookie'))).click()

    # Check for upgrades every 15 seconds and buy all upgrades available, starting with most expensive
    if time.time() >= check_upgrade:
        check_upgrade = time.time() + 15

        for upgrade_id in upgrades_id:
            try:
                driver.find_element_by_id(upgrade_id).click()
            except NoSuchElementException and StaleElementReferenceException:
                continue

# Find final cookies per second score
cps = driver.find_element_by_id("cps").text
print(cps)

driver.quit()
