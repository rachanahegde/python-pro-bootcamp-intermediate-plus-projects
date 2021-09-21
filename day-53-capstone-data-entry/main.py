from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


CHROME_DRIVER_PATH = "/Users/Rachana 1/Documents/Development/chromedriver"
RENTAL_LISTINGS_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%" \
                      "7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%" \
                      "2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.84" \
                      "7169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value" \
                      "%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%" \
                      "7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22" \
                      "%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22" \
                      "value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D" \
                      "%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isList" \
                      "Visible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
RENTING_RESEARCH_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScEYI4u0dXlXhN5s0s2HtIk1YwJ8CXiNOQz-_fUFFEy6yKi7Q/" \
                        "viewform?usp=sf_link"

# TODO Use Selenium to scrape listings and get the price, address, and URL of each listing

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
# driver.get(RENTAL_LISTINGS_URL)
driver.implicitly_wait(20)
sleep(4)  # Wait for the page to load completely

# Use tab and arrow_down to scroll through all the listings to the bottom of the page
# for _ in range(20):
#     webdriver.ActionChains(driver).key_down(Keys.TAB).perform()
# for _ in range(300):
#     webdriver.ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

# links_list = []
# addresses_list = []
# prices_list = []

# Scrape the prices and addresses on the first page
# listings = driver.find_elements_by_class_name('list-card-info')
# for listing in listings:
#     try:
        # prices_list.append(listing.find_element_by_class_name('list-card-price').text)
        # addresses_list.append(listing.find_element_by_class_name('list-card-addr').text)
    # except NoSuchElementException and StaleElementReferenceException:
    #     continue
    # sleep(2)

# Scrape the listing links on the first page
# sleep(2)
# list_cards = driver.find_elements_by_class_name('list-card-top')
# for card in list_cards:
#     try:
#         print(card.find_element_by_tag_name('a').get_attribute('href'))
#         links_list.append(card.find_element_by_tag_name('a').get_attribute('href'))
#     except NoSuchElementException and StaleElementReferenceException:
#         continue
#     sleep(2)

# print(links_list)

# Hard coded for convenience since the website recognises this program is a bot
prices_list = ['$2,500/mo', '$2,650/mo', '$2,500/mo', '$1,995/mo', '$2,950/mo', '$2,990/mo', '$2,499+ 1 bd',
               '$2,355+ 1 bd', '$2,810+/mo', '$2,895/mo', '$2,354+/mo', '$2,925+ 1 bd', '$2,720+ 1 bd', '$2,560+/mo',
               '$2,995/mo', '$2,795/mo', '$2,495/mo', '$2,695+/mo', '$2,995/mo', '$2,695/mo', '$2,600+/mo', '$2,695/mo',
               '$2,795+ 1 bd', '$2,795+ 1 bd', '$2,295+ 1 bd', '$1,663+ 1 bd', '$2,680+ 1 bd', '$2,495/mo',
               '$2,600+/mo', '$2,795/mo', '$2,495+ 1 bd', '$2,895+ 1 bd', '$2,250/mo', '$2,395/mo', '$2,319+ 1 bd',
               '$2,995/mo', '$3,000+ 1 bd', '$2,595+ 1 bd', '$2,599/mo', '$2,995/mo']
addresses_list = ['1367 8th Ave APT 4, San Francisco, CA 94122', '241 10th St, San Francisco, CA 94103', '1948 Eddy St, San Francisco, CA 94115', '138 Clinton Park #A, San Francisco, CA 94103', '895 24th Ave, San Francisco, CA 94121', '1717 Webster St #1413, Oakland, CA 94612', '1190 Mission at Trinity Place | 1190 Mission St, San Francisco, CA', 'Coliseum Connections | 805 71st Ave, Oakland, CA', '2211 Stockton St #1492387, San Francisco, CA 94133', '355 Fulton St APT 203, San Francisco, CA 94102', '1411 Alice St #KQGEKNY6U, Oakland, CA 94612', 'Channel House | 40 Harrison St, Oakland, CA', 'Lydian | 238 13th St, Oakland, CA', '515 John Muir Dr #1657467, San Francisco, CA 94132', '1801 Wedemeyer St UNIT 216, San Francisco, CA 94129', '920 Leavenworth St #206, San Francisco, CA 94109', '840 California St #28PRATT, San Francisco, CA 94108', '1801 Shoreline Dr #QPGHMRNMK, Alameda, CA 94501', '861 Post St APT 8, San Francisco, CA 94109', '345 Fulton St APT 34, San Francisco, CA 94102', '2440 Van Ness Ave #F08Z3F5EN, San Francisco, CA 94109', '1385 Clay St #DJ9TJ5VEK, San Francisco, CA 94109', '990 Geary | 990 Geary St, San Francisco, CA', '324 Larkin | 324 Larkin St, San Francisco, CA', '747 Ellis | 747 Ellis St, San Francisco, CA', 'Jackson Lake Apartments | 1533 Jackson St, Oakland, CA', 'The Union | 532 Union St, Oakland, CA', '1201 Pine St #10, San Francisco, CA 94109', '150 Van Ness Ave #XQ3JAB4QU, San Francisco, CA 94102', '77 Glen Ave APT 301, Oakland, CA 94611', '472 Jean | 472 Jean St, Oakland, CA', '1025 Sutter | 1025 Sutter St, San Francisco, CA', '1 Woodward St #3, San Francisco, CA 94103', '1940 Franciscan Way #206, Alameda, CA 94501', '50 Jones | 50 Jones St, San Francisco, CA', '600 Oak St #31, San Francisco, CA 94117', '1 Daniel Burnham Ct, San Francisco, CA', '977 Pine | 977 Pine St, San Francisco, CA', '240 Dolores St APT 237, San Francisco, CA 94103', '1753 Mason St #1755, San Francisco, CA 94133']
links_list = ['https://www.zillow.com/homedetails/1319-Palou-Ave-San-Francisco-CA-94124/332861291_zpid/', 'https://www.zillow.com/homedetails/2420-Market-St-APT-3-San-Francisco-CA-94114/2100854954_zpid/', 'https://www.zillow.com/b/soma-square-san-francisco-ca-5Xj2Yr/', 'https://www.zillow.com/homedetails/1222-10th-Ave-5-San-Francisco-CA-94122/2068436101_zpid/', 'https://www.zillow.com/homedetails/3253-Ettie-St-UNIT-2-Emeryville-CA-94608/2077828114_zpid/', 'https://www.zillow.com/homedetails/757-Jackson-St-APT-301-San-Francisco-CA-94108/2068436371_zpid/', 'https://www.zillow.com/homedetails/820-E-21st-St-5-Oakland-CA-94606/2068436517_zpid/', 'https://www.zillow.com/homedetails/1712-33rd-Ave-Oakland-CA-94601/2068436659_zpid/', 'https://www.zillow.com/homedetails/2249-Myrtle-St-Oakland-CA-94607/333757043_zpid/', 'https://www.zillow.com/homedetails/801-53rd-St-4-Emeryville-CA-94608/2076709077_zpid/', 'https://www.zillow.com/homedetails/871-Apgar-St-1-Emeryville-CA-94608/2068437069_zpid/', 'https://www.zillow.com/b/San-Francisco-CA/37.74781,-122.42734_ll/', 'https://www.zillow.com/b/3465-25th-st-san-francisco-ca-5YCLFj/', 'https://www.zillow.com/b/parc-on-powell-emeryville-ca-5XjR3k/', 'https://www.zillow.com/homedetails/1025-Geneva-Ave-5-San-Francisco-CA-94112/2068438076_zpid/', 'https://www.zillow.com/homedetails/1618-85th-Ave-Oakland-CA-94621/24797630_zpid/', 'https://www.zillow.com/homedetails/860-Geary-St-APT-507-San-Francisco-CA-94109/2081912219_zpid/', 'https://www.zillow.com/homedetails/1065-Bella-Vista-Ave-Oakland-CA-94610/24762458_zpid/', 'https://www.zillow.com/homedetails/371-Somerset-Rd-APT-B-Piedmont-CA-94611/2111829326_zpid/', 'https://www.zillow.com/homedetails/1727-12th-St-UNIT-1727-Oakland-CA-94607/2079251638_zpid/', 'https://www.zillow.com/homedetails/1-Hawthorne-St-UNIT-12B-San-Francisco-CA-94105/111711064_zpid/', 'https://www.zillow.com/b/Emeryville-CA/37.838744,-122.306001_ll/', 'https://www.zillow.com/homedetails/318-Turk-St-405-San-Francisco-CA-94102/2071561503_zpid/', 'https://www.zillow.com/b/925-geary-san-francisco-ca-5XjMQS/', 'https://www.zillow.com/homedetails/455-Hyde-St-41-San-Francisco-CA-94109/2073368842_zpid/', 'https://www.zillow.com/b/781-o%27farrell-san-francisco-ca-9NKJ5L/', 'https://www.zillow.com/homedetails/26-Sargent-St-San-Francisco-CA-94132/15193050_zpid/', 'https://www.zillow.com/homedetails/2450-Palmetto-St-Oakland-CA-94602/82833059_zpid/', 'https://www.zillow.com/b/19th-and-harrison-oakland-ca-BPPyPZ/', 'https://www.zillow.com/homedetails/1717-Webster-St-1413-Oakland-CA-94612/2081841712_zpid/', 'https://www.zillow.com/b/1190-mission-at-trinity-place-san-francisco-ca-5XjVtb/', 'https://www.zillow.com/b/coliseum-connections-oakland-ca-BMXbv9/', 'https://www.zillow.com/homedetails/2211-Stockton-St-1492387-San-Francisco-CA-94133/2104934304_zpid/', 'https://www.zillow.com/homedetails/355-Fulton-St-APT-203-San-Francisco-CA-94102/2071569339_zpid/', 'https://www.zillow.com/b/channel-house-oakland-ca-BjbC68/', 'https://www.zillow.com/b/lydian-oakland-ca-BqzFbt/', 'https://www.zillow.com/homedetails/515-John-Muir-Dr-1657467-San-Francisco-CA-94132/2100225033_zpid/', 'https://www.zillow.com/homedetails/1801-Wedemeyer-St-UNIT-216-San-Francisco-CA-94129/2088758859_zpid/', 'https://www.zillow.com/homedetails/920-Leavenworth-St-206-San-Francisco-CA-94109/2072084973_zpid/', 'https://www.zillow.com/homedetails/840-California-St-28PRATT-San-Francisco-CA-94108/2075393120_zpid/']

# Format the prices list and remove '/mo' and '+ 1 bd' using replace()
formatted_prices = [price.replace("/mo", "").replace("+ 1 bd", "") for price in prices_list]

# TODO Use Selenium to auto-fill a google form per listing on Zillow

driver.get(RENTING_RESEARCH_FORM)

for n in range(len(formatted_prices)):
    property_address = driver.find_element_by_xpath \
        ('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_address.send_keys(addresses_list[n])
    price_per_month = driver.find_element_by_xpath \
        ('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month.send_keys(formatted_prices[n])
    property_link = driver.find_element_by_xpath \
        ('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link.send_keys(links_list[n])
    sleep(2)
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit_btn.click()

    new_form_link = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_form_link.click()
