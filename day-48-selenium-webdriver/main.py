from selenium import webdriver

# chrome_driver_path = "/Users/Rachana 1/Documents/Development/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=pd_sbs_1/133-6711199-9903914?pd_rd_w=UMhm0&pf_rd_p=3676f086-9496-4fd7-8490-77cf7f43f846&pf_rd_r=ATS122CDCFV7EBPDRMMZ&pd_rd_r=f59cbe7a-ded0-4ee3-80c4-e85a165fec88&pd_rd_wg=VkZ8C&pd_rd_i=B00FLYWNYQ&psc=1")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# driver.get("https://www.python.org/")
# search_bar = driver.find_element_by_name("q")

# logo = driver.find_element_by_class_name("python-logo")

# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# ----------------------- Challenge 1: Use Selenium to Scrape Website Data (MY SOLUTION) ----------------------- #
# driver.get("https://www.python.org/")
# upcoming_events = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
# upcoming_events_list = upcoming_events.split("\n")

upcoming_events_list = ['2021-09-10', 'PyConline AU 2021', '2021-09-11', 'PyCon Odessa 2021', '2021-09-17', 'PyCon India 2021', '2021-09-19', 'PyWeek 32', '2021-10-02', 'PyConTW 2021']
# Hard coded for convenience

event_data = {}

dates_list = upcoming_events_list[slice(0, len(upcoming_events_list), 2)]
event_names = upcoming_events_list[slice(1, len(upcoming_events_list), 2)]

for n in range(5):
    event_data[n] = {"time": dates_list[n], "name": event_names[n]}

print(event_data)

# --------------------- Challenge 1: Use Selenium to Scrape Website Data (ANGELA'S SOLUTION) --------------------- #



# driver.quit()
