import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.HEADERS = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }


    def get_data(self):
        response = requests.get(url= self.SHEETY_ENDPOINT, headers= self.HEADERS)
        response.raise_for_status()
        data = response.json()
        # data = {'prices': [{'city': 'Milan', 'iata': 'MIL', 'price': '111.91', 'id': 2}, {'city': 'Paris', 'iata': 'PAR', 'price': '132.22', 'id': 3}, {'city': 'New York', 'iata': 'NYC', 'price': '358.48', 'id': 4}]}     # Save on API calls
        return {data['prices'][i]['city']: {'iata': data['prices'][i]['iata'], 'id': data['prices'][i]['id'], 'lowestPrice': data['prices'][i]['price']} for i in range(len(data['prices']))}


    def update_prices(self, id, price):
        data = {
            'price': {
                'price': price
            }
        }
        response = requests.put(url= f"{self.SHEETY_ENDPOINT}/{id}", json= data, headers= self.HEADERS)
        response.raise_for_status()