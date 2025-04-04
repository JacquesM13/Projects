import requests
import os

owm_api = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": 35.149532,
    "lon": -90.048981,
    "appid": owm_api,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()

def telegram_bot_sendtext(bot_message):
    bot_token = os.environ.get("BOT_TOKEN")
    bot_chat_id = '6166404353'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

will_rain = False

for i in range(len(data["list"])):
    weather_id = data["list"][i]["weather"][0]["id"]
    if weather_id < 600:
        will_rain = True

if will_rain:
    message = telegram_bot_sendtext("Bring an umbrella ☂️")
    print(message)