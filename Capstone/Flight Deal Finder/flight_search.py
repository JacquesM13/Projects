from urllib.error import HTTPError

import requests
from datetime import datetime, timedelta
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.BASE_ENDPOINT = "https://test.api.amadeus.com/v1"
        self.AUTH_ENDPOINT = f"{self.BASE_ENDPOINT}/security/oauth2/token"
        self.IATA_ENDPOINT = f"{self.BASE_ENDPOINT}/reference-data/locations"
        self.CHEAPEST_ENDPOINT = f"{self.BASE_ENDPOINT}/shopping/flight-dates"
        self.FLIGHT_API = os.environ.get("FLIGHT_API")
        self.FLIGHT_API_SECRET = os.environ.get("FLIGHT_API_SECRET")
        self.TOKEN = None
        self.get_token()
        self.HEADERS = {"Authorization": f"Bearer {self.TOKEN}"}
        self.ORIGIN_IATA = "LON"
        self.DURATION = "6,7"


    def get_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.FLIGHT_API,
            "client_secret": self.FLIGHT_API_SECRET
        }
        response = requests.post(url=self.AUTH_ENDPOINT, data=body, headers=header)
        response.raise_for_status()
        data = response.json()
        self.TOKEN = data['access_token']


    def fetch_iata(self, city):
        parameters = {
            "keyword": city,
            "subType": "CITY"
        }

        response = requests.get(url=self.IATA_ENDPOINT, headers=self.HEADERS, params=parameters)
        try:
            response.raise_for_status()

        except Exception as e:
            print(f"Amadeus says you're sending too many requests, *eyeroll*\n {e}")
            return "N/A"

        else:
            data = response.json()
            return data['data'][0]['iataCode']


    def get_cheapest_flight(self, iata):
        now = datetime.now()
        earliest_dept_date = (now + timedelta(days=1)).date()
        latest_dept_date = (earliest_dept_date + timedelta(days=30 * 4))
        dept_dates = f"{earliest_dept_date},{latest_dept_date}"
        parameters = {
            "origin": self.ORIGIN_IATA,
            "destination": iata,
            "departureDate": dept_dates,
            "duration": self.DURATION
        }
        response = requests.get(url=self.CHEAPEST_ENDPOINT, headers=self.HEADERS, params=parameters)
        data = response.json()
        try:
            data = data['data'][0]

        except KeyError:
            print(f"No flights found from {self.ORIGIN_IATA}")
            return "N/A"

        return data['price']['total'], data['origin'], data['destination'], data['departureDate'], data['returnDate']