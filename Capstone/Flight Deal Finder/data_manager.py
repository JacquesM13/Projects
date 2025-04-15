import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
        self.SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.HEADERS = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }


    def get_data(self):
        response = requests.get(url= self.SHEETY_PRICES_ENDPOINT, headers= self.HEADERS)
        response.raise_for_status()
        data = response.json()
        # data = {'prices': [{'city': 'Milan', 'iata': 'MIL', 'price': '180.91', 'id': 2}, {'city': 'Paris', 'iata': 'PAR', 'price': '152.22', 'id': 3}, {'city': 'New York', 'iata': 'NYC', 'price': '600.48', 'id': 4}]}     # Save on API calls
        return {data['prices'][i]['city']: {'iata': data['prices'][i]['iata'], 'id': data['prices'][i]['id'], 'lowestPrice': data['prices'][i]['price']} for i in range(len(data['prices']))}


    def get_customer_emails(self):
        response = requests.get(url= self.SHEETY_USERS_ENDPOINT, headers= self.HEADERS)
        response.raise_for_status()
        data = response.json()
        # data = {'users': [{'timestamp': '4/15/2025 10:05:05', 'whatIsYourFirstName?': 'Jacques', 'whatIsYourLastName?': 'Massey', 'whatIsYourEmailAddress': 'jacquesmassi@gmail.com', 'id': 2}]}
        emails = [data['users'][i]['whatIsYourEmailAddress'] for i in range(len(data['users']))]
        return emails


    def update_prices(self, id, price):
        data = {
            'price': {
                'price': price
            }
        }
        response = requests.put(url= f"{self.SHEETY_PRICES_ENDPOINT}/{id}", json= data, headers= self.HEADERS)
        response.raise_for_status()
