import requests
import os
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.BOT_TOKEN = os.environ.get("BOT_TOKEN")
        self.CHAT_ID = os.environ.get("CHAT_ID")
        self.API_ENDPOINT = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
        self.PASSWORD = os.environ.get("PASSWORD")
        self.MY_EMAIL = os.environ.get("MY_EMAIL")


    def telegram_messenger(self, message):
        parameters = {
            "chat_id": self.CHAT_ID,
            "text": message
        }
        response = requests.get(url= self.API_ENDPOINT, json= parameters)
        response.raise_for_status()
        return response.json()

    def email_sender(self, email_address, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= self.MY_EMAIL, password= self.PASSWORD)
            connection.sendmail(from_addr= self.MY_EMAIL,
                                to_addrs= email_address,
                                msg= f"Subject: Flight Offer!\n\n{message}")
