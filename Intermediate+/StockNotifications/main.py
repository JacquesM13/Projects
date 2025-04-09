import requests
from datetime import date, timedelta
import json
import html

# Dealing with dates
today = date.today()
yesterday = today - timedelta(days=1)
day_before = yesterday - timedelta(days=1)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "6DZ2HH6P86FJOHC5"

NEWS_KEY = "63cc360ec4b14381b54ee22f56b8b023"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_KEY,
}

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_KEY,
    "pageSize": 3,
    "from": str(yesterday),
    "language": "en",
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# response = requests.get("https://www.alphavantage.co/query", params = stock_parameters)
# response.raise_for_status()
# data = response.json()

# Exceed daily API calls and resort to loading datafile...
with open("data.json") as datafile:
    data = json.load(datafile)

yesterday_open = float(data["Time Series (Daily)"][str(yesterday)]["1. open"])
day_before_open = float(data["Time Series (Daily)"][str(day_before)]["1. open"])

difference = ((day_before_open - yesterday_open)/day_before_open) * 100

get_news = False

if abs(difference) > 5:
    get_news = True

# Telegram
# Send a separate message with the percentage change and each article's title and description

def telegram_messenger(message):
    bot_token = "7775756961:AAFdToL22-wjVd-DSwS_zbwicEAAVqREeak"
    bot_chat_id = '6166404353'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()

# Use https://newsapi.org
if get_news:
    response = requests.get("https://newsapi.org/v2/everything", news_parameters)
    response.raise_for_status()
    data = response.json()
    article_list = data['articles']

    if difference > 0:
        telegram_messenger(f"{STOCK}: 📈 {difference:.2f}%")
        for article in article_list:
            telegram_messenger(f"{article['author']}\nHeadline: {article['title']}\nBrief: {article['description']}")

    else:
        telegram_messenger(f"{STOCK}: 📉 {difference:.2f}%")
        for article in article_list:
            telegram_messenger(f"{article['author']}\nHeadline: {article['title']}\nBrief: {article['description']}")