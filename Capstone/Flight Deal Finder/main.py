from urllib.error import HTTPError

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

sheetData = DataManager()
flightSearcher = FlightSearch()
notificationManager = NotificationManager()

sheet_data = sheetData.get_data()
sheet_users = sheetData.get_customer_emails()

for city, values in sheet_data.items():

    try:
        iata = flightSearcher.fetch_iata(city)
        price, origin, destination, deptDate, returnDate = flightSearcher.get_cheapest_flight(iata)
        message = f"Flight from London ({origin}) to {city} ({destination}): {price} GBP, Departs: {deptDate}, Returns: {returnDate}"
        print(message)

    except ValueError:
        print("Try another origin city")

    else:
        if float(price) < float(values['lowestPrice']):
            notificationManager.telegram_messenger(message)
            sheetData.update_prices(id= values['id'], price= price)

            for user in sheet_users:
                notificationManager.email_sender(email_address= user, message= message)
                print(f"Sent to {user}")
