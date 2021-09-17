from selenium import webdriver
from time import sleep

FB_EMAIL = ""
FB_PASSWORD = ""

chrome_driver_path = "/Users/Rachana 1/Documents/Development/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/app")
sleep(2)

# Log In with Facebook
login_btn = driver.find_element_by_xpath\
    ('//*[@id="o771500765"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_btn.click()
sleep(2)
fb_login = driver.find_element_by_xpath('//*[@id="o-1268705039"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
fb_login.click()

# Switch to facebook login window
sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Enter login info
driver.find_element_by_id('email').send_keys(FB_EMAIL)
driver.find_element_by_id('pass').send_keys(FB_PASSWORD)
sleep(2)
driver.find_element_by_id('loginbutton').click()

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Project unsuccessful after this point due to Tinder demanding verification

