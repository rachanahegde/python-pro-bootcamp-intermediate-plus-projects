import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

account_sid = ""
auth_token = ""

# Get yesterday's date and day before yesterday's date and format them.
today = dt.date.today()
yesterday = str(today - dt.timedelta(days=1))
day_before_yesterday = str(today - dt.timedelta(days=2))

# Get the daily close price data from the Alpha Vantage API
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
yesterday_close = float(stock_data[yesterday]['4. close'])
day_before_yesterday_close = float(stock_data[day_before_yesterday]['4. close'])

# Find percentage stock price increase/decrease
price_difference = yesterday_close - day_before_yesterday_close
percent_change = (price_difference / yesterday_close) * 100

# If stock price increased/decreased by over 5%, fetch the first 3 articles for the COMPANY_NAME.
if abs(percent_change) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data['articles'][:3]

    if percent_change > 0:
        main_title = f"{STOCK}: 🔺{round(percent_change)}%"
    else:
        main_title = f"{STOCK}: 🔻{round(percent_change)}%"

    # Send a separate message with each article's title and description to your phone number.

    formatted_articles = [f"{main_title}\nHeadline: {article['title']}.\n Brief: {article['description']}"
                          for article in articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='',
            to=''
        )
        print(message.status)
