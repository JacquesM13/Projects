import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

BUDGET = 60

to_email = 'jacques.massey@outlook.com'

header = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-GB,en;q=0.5",
  "Connection": "keep-alive",
  "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Brave\";v=\"127\", \"Chromium\";v=\"127\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "cross-site",
  "Sec-Fetch-User": "?1",
  "Sec-Gpc": "1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
}

product_page = "https://www.amazon.co.uk/Shimano-Pedals-PD-EH500-pedals-inches/dp/B07CDQ4K7S?crid=3922Q7QU0WATO&dib=eyJ2IjoiMSJ9.Cs-rUJKBttLz_0hGoEy1LziWVjDWAaiYogS-zo4Rpg0NUZLxxfDMAMhLFdINIou56Xh2dft3by-lPXAxYPJ_cq3TY9j-0DLzhEz6ArA3Yuq02DWVy4unFLPK95uyt1S4ga3Ab9BZR9JpHvxVNTwHgQL-SigqVWrwTYIbfkmzkwcdQzHzkkOZyqhrwm-zh2jqjZRdJ8CQCq4LyUdtGQnE-S0eYvEhj1OeOjK1MP_BotcEi11y2E68M8dfGxYTdXD4NG3-oLB4HzFFibJyO7l3_GoMP4dXMrOh7mZoTHHZ198.V9dJvtKEgVe_B7RGy13ugyUKowV2qNac8VjH_rSpmbs&dib_tag=se&keywords=Shimano%2BPD-EH500%2BSPD%2BPedals&qid=1747766550&sprefix=shimano%2Bpd-eh500%2Bspd%2Bpedals%2Caps%2C195&sr=8-6&th=1&psc=1"
response = requests.get(url= product_page, headers= header)
response.raise_for_status()

# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify)

price_whole = float(soup.select_one(selector= ".a-price-whole").getText())
price_fraction = float((soup.select_one(selector= ".a-price-fraction").getText()))
price = price_whole + price_fraction/100

product_title = soup.select_one(selector= "h1#title > span#productTitle").getText().strip()

print(price)

print(product_title)

if price < BUDGET:
    with smtplib.SMTP(os.environ['SMTP_ADDRESS']) as connection:
        connection.starttls()
        connection.login(user= os.environ['MY_EMAIL'], password= os.environ['MY_PASSWORD'])
        connection.sendmail(from_addr= os.environ['MY_EMAIL'], to_addrs= to_email,
                            msg= f"Subject: Price Drop!\n\n {product_title} is now {price}\n {product_page}".encode('utf-8'))