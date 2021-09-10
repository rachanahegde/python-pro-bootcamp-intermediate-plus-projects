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

# Set up the timer to end loop after 5 minutes
timeout = 60 * 5
timeout_start = time.time()
check_upgrade = timeout_start + 10

upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma",
               "buyCursor"]

while time.time() < timeout_start + timeout:
    try:
        cookie.click()
    except StaleElementReferenceException and AttributeError:
        wait.until(EC.element_to_be_clickable((By.ID, 'cookie'))).click()

    money = int(driver.find_element_by_id("money").text.replace(",", ""))

    # Get cost of upgrades
    # try:
    #     upgrades = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#store b')))
    #     upgrades_list = [upgrade.text.replace(',', '').split()[-1] for upgrade in upgrades if len(upgrade.text) > 0]
    #     # upgrades = driver.find_elements_by_css_selector("#store b")
    # except NoSuchElementException and StaleElementReferenceException and WebDriverException and TypeError:
    #     pass

    # Set upgrade costs
    # cursor_cost = int(upgrades_list[0])
    # grandma_cost = int(upgrades_list[1])
    # factory_cost = int(upgrades_list[2])
    # mine_cost = int(upgrades_list[3])
    # shipment_cost = int(upgrades_list[4])
    # lab_cost = int(upgrades_list[5])
    # portal_cost = int(upgrades_list[6])
    # time_machine_cost = int(upgrades_list[7])

    # Check for upgrades every 10 seconds
    if time.time() >= check_upgrade:
        check_upgrade = time.time() + 10
        # print(f"This is the upgrades list: {upgrades_list}")
        # print("It has been 10 seconds.")

        for upgrade_id in upgrades_id:
            try:
                driver.find_element_by_id(upgrade_id).click()
            except NoSuchElementException and StaleElementReferenceException:
                continue

        # try:
        #     if money >= time_machine_cost:
        #         driver.find_element_by_id("buyTime machine").click()
        #     elif money >= portal_cost:
        #         driver.find_element_by_id("buyPortal").click()
        #     elif money >= lab_cost:
        #         driver.find_element_by_id("buyAlchemy lab").click()
        #     elif money >= shipment_cost:
        #         driver.find_element_by_id("buyShipment").click()
        #     elif money >= mine_cost:
        #         driver.find_element_by_id("buyMine").click()
        #     elif money >= factory_cost:
        #         driver.find_element_by_id("buyFactory").click()
        #     elif money >= grandma_cost:
        #         driver.find_element_by_id("buyGrandma").click()
        #     elif money >= cursor_cost:
        #         driver.find_element_by_id("buyCursor").click()
        #         # wait.until(EC.element_to_be_clickable((By.ID, 'buyCursor'))).click()
        # except NoSuchElementException and StaleElementReferenceException and WebDriverException:
        #     pass

# Find final cookies per second score
cps = driver.find_element_by_id("cps").text
print(cps)

driver.quit()
