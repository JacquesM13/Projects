import requests
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.BOT_TOKEN = os.environ.get("BOT_TOKEN")
        self.CHAT_ID = os.environ.get("CHAT_ID")
        self.API_ENDPOINT = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"


    def telegram_messenger(self, message):
        parameters = {
            "chat_id": self.CHAT_ID,
            "text": message
        }
        response = requests.get(url= self.API_ENDPOINT, json= parameters)
        response.raise_for_status()
        return response.json()