import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = ""
auth_token = ""

weather_params = {
    "lat": 22.396427,
    "lon": 114.109497,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]


def check_rain():
    weather_codes = [hour_data['weather'][0]['id'] for hour_data in weather_slice]
    bring_umbrella = False
    for code in weather_codes:
        if code < 700:
            bring_umbrella = True
    return bring_umbrella


if check_rain():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☔️",
        from_='',
        to=''
    )
    print(message.status)
