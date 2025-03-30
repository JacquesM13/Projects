import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "jacquesmassi@gmail.com"
PASSWORD = "divp mlyg ynfv iupp"

my_location = {
    "lat": 54.895061,
    "lng": -2.933550,
    "formatted": 0,
    "tzid": "Europe/London"
}


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    my_latitude = my_location["lat"]
    my_longitude = my_location["lng"]
    if abs(iss_latitude - my_latitude) < 5 and abs(iss_longitude - my_longitude) < 5:
        return True


def is_night():
    now = datetime.now()
    response = requests.get("https://api.sunrise-sunset.org/json", params= my_location)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    if now.hour < sunrise or now.hour > sunset:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= PASSWORD)
            connection.sendmail(from_addr= MY_EMAIL,
                                to_addrs= MY_EMAIL,
                                msg= "Subject: Look Up! 👆\n\nThe ISS is overhead!")