from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

MY_EMAIL = ""
MY_PASSWORD = ""

# Step 1 - Use BeautifulSoup to Scrape the Product Price

URL = "https://www.amazon.com.au/Rosaline-Palmer-Takes-Cake-Winner-ebook/dp/B08TQYSD4D/ref=sr_1_4?dchild=1&" \
      "keywords=alexis+hall&qid=1628565994&sr=8-4"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.77 Safari/537.36",
}

response = requests.get(URL, headers=headers)
product_page = response.text
soup = BeautifulSoup(product_page, "lxml")
product_title = soup.find(name="span", id="productTitle").getText()
product_price = float(soup.find(name="span", id="kindle-price").getText().split('$')[1])

# Step 2 - Email Alert When Price Below Preset Value

if product_price < 13:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="",
            msg=f"Subject:Amazon Price Alert!\n\n"
                f"{product_title} is now ${product_price}. "
                f"Buy here: {URL}"
        )


