from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


CHROME_DRIVER_PATH = "/Users/Rachana 1/Documents/Development/chromedriver"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(USERNAME)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(PASSWORD)
        sleep(2)
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        try:
            # Tell Instagram not to save login information and exit 'turn on notifications' popup
            sleep(2)
            not_now_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
            not_now_btn.click()
            sleep(2)
            not_now_link = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            not_now_link.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        followers_popup = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/'
                                                            'section/ul/li[2]/a')
        followers_popup.click()
        sleep(4)
        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
        while True:
            self.follow()
            sleep(2)
            # Keep scrolling through the followers list
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            sleep(3)

    def follow(self):
        follow_btn_list = self.driver.find_elements_by_class_name('y3zKF')
        for follow_btn in follow_btn_list:
            try:
                sleep(3)
                follow_btn.click()
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
                continue


follower_bot = InstaFollower(CHROME_DRIVER_PATH)
follower_bot.login()
follower_bot.find_followers()
