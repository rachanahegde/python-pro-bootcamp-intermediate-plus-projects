from selenium import webdriver
from time import sleep

PROMISED_DOWN = 150  # Example Internet Speed
PROMISED_UP = 10  # Example Internet Speed
CHROME_DRIVER_PATH = "/Users/Rachana 1/Documents/Development/chromedriver"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.implicitly_wait(20)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                      'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                      'div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                    'div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        # print(f"down: {self.down}")
        # print(f"up: {self.up}")

    def tweet_at_provider(self):
        # Log in to Twitter
        self.driver.get("https://twitter.com/")
        sleep(2)
        sign_in_link = self.driver.find_element_by_xpath\
            ('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
        sign_in_link.click()
        sleep(2)
        sign_in_btn = self.driver.find_element_by_xpath\
            ('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span')
        sign_in_btn.click()
        sleep(3)
        email_field = self.driver.find_element_by_name('username')
        email_field.send_keys(TWITTER_EMAIL)
        sleep(2)
        next_btn = self.driver.find_element_by_xpath\
            ('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
        next_btn.click()
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(TWITTER_PASSWORD)
        login_btn = self.driver.find_element_by_xpath\
            ('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
        sleep(2)
        login_btn.click()

        # Tweet at the service provider
        sleep(3)
        new_tweet_button = self.driver.find_element_by_xpath\
            ('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_tweet_button.click()
        write_tweet = self.driver.find_element_by_xpath\
            ('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/'
             'div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        write_tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay "
                              f"for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/'
                                                      'div/div[2]/div[4]/div')
        sleep(2)
        tweet_btn.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
