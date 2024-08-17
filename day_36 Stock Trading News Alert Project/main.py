import requests
from datetime import datetime
from datetime import timedelta
from twilio.rest import Client

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# stocks
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")

# news
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")

# twilio
account_sid = os.getenv("TWILIO_account_sid")
auth_token = os.getenv("TWILIO_auth_token")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHAVANTAGE_API_KEY
}
# get response
response = requests.get(STOCK_ENDPOINT, params=params)
response.raise_for_status()
stock_data = response.json()

# get today's date and yesterday
now = datetime.now()
today_formatted = now.strftime("%Y-%m-%d")
yesterday = now - timedelta(days=1)
yesterday_formatted = yesterday.strftime("%Y-%m-%d")

# if there is a time difference and a new date is not registered in the server
if today_formatted not in stock_data["Time Series (Daily)"]:
    now = now - timedelta(days=1)
    today_formatted = now.strftime("%Y-%m-%d")
    yesterday = now - timedelta(days=1)
    yesterday_formatted = yesterday.strftime("%Y-%m-%d")

# get closing prices in today and yesterday
today_close_price = float(stock_data["Time Series (Daily)"][today_formatted]["4. close"])
yesterday_close_price = float(stock_data["Time Series (Daily)"][yesterday_formatted]["4. close"])

# if STOCK price increase/decreases by 5% between yesterday and the day before yesterday
if abs(today_close_price - yesterday_close_price) / yesterday_close_price >= 0.05:
    is_up = today_close_price - yesterday_close_price > 0.05
    percentage = int(100 * abs(today_close_price - yesterday_close_price) / yesterday_close_price)
    news_params = {
        'qInTitle': COMPANY_NAME,
        'apiKey': NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    # get 3 news pieces
    articles = news_data["articles"]
    # get SMS client
    client = Client(account_sid, auth_token)
    # send SMS for each article
    for i in range(3):
        title = articles[i]["title"]
        description = articles[i]["description"]
        if is_up:
            emoji = "🔺"
        else:
            emoji = "🔻"

        message = client.messages.create(
            body=f"{STOCK}: {emoji}{percentage}%\n"
                 f"Headline: {title}\n"
                 f"Brief: {description}",
            from_=os.getenv("SENDER_PHONE_NUMBER"),
            to=os.getenv("RECEIVER_PHONE_NUMBER")
        )



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

