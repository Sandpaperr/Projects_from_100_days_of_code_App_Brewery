import requests
from newscatcherapi import NewsCatcherApiClient
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api = os.getenv("STOCK_API")
stock_url = os.getenv("STOCK_URL")

news_api = os.getenv("NEWS_API")

account_sid = os.getenv("NEWS_ACCOUNT_SID")
auth_token = os.getenv("NEWS_AUTH_TOKEN")

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api,

}

response = requests.get(stock_url, params=parameters_stock)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_close_stock = float(yesterday_data["4. close"])

day_before_data = data_list[1]
day_before_close_stock = float(day_before_data["4. close"])
percentage = 100 * abs(yesterday_close_stock - day_before_close_stock ) / yesterday_close_stock

if percentage >= 5:

    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    newscatcherapi_type = NewsCatcherApiClient(x_api_key=news_api)
    articles = newscatcherapi_type.get_search(
        q=COMPANY_NAME,
        lang="en",
        published_date_precision="full",
        sort_by="relevancy",
        page_size=3,
    )

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    if yesterday_close_stock > day_before_close_stock:
        symbol = "🔺"
    else:
        symbol = "▼"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"\n{STOCK}: {symbol}%.2f%%\n" % percentage,
        from_="+18788880816",
        to="+447742200038"
    )
    print(message.status)

    for _ in range(3):
        heading = articles["articles"][_]["title"]
        brief = articles["articles"][_]["summary"]
        published_date = articles["articles"][_]["published_date"]
        article_link = articles["articles"][_]["link"]

        message = client.messages.create(
            body=f"\nHeading: {heading}\n" + f"Brief: {published_date} - {brief}\n Link: {article_link}",
            from_="+18788880816",
            to="+447742200038"
        )
        print(message.status)

