from urllib.error import HTTPError

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheetData = DataManager()
flightSearcher = FlightSearch()
telegramBot = NotificationManager()

sheet_data = sheetData.get_data()

for city, values in sheet_data.items():

    try:
        iata = flightSearcher.fetch_iata(city)
        price, origin, destination, deptDate, returnDate = flightSearcher.get_cheapest_flight(iata)
        print(f"Flight from London ({origin}) to {city} ({destination}): £{price}, Departs: {deptDate}, Returns: {returnDate}")

    except ValueError:
        print("Try another origin city")

    else:
        if float(price) < float(values['lowestPrice']):
            telegramBot.telegram_messenger(f"Flight from London ({origin}) to {city} ({destination}): £{price}, Departs: {deptDate}, Returns: {returnDate}")
            sheetData.update_prices(id= values['id'], price= price)