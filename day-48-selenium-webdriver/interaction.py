from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Rachana 1/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# ------------------------- Challenge: Fill in the form and click sign up ------------------------ #
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_class_name("top")
first_name.send_keys("Rachana")
last_name = driver.find_element_by_class_name("middle")
last_name.send_keys("Hegde")
email = driver.find_element_by_class_name("bottom")
email.send_keys("rachanahegde@gmail.com")
submit_btn = driver.find_element_by_class_name("btn-block")
submit_btn.click()
