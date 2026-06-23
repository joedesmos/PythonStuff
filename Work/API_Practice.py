#Had to use ai to learn and figure this out but I learned a lot from it.

import requests

API_KEY = "a3570d1429da703b46032fe4e690bc9d"
CITY = "Paris"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()

    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["main"]

    print(f"Currently it is {temp}°F in {CITY} and there are {condition}.")

    if temp > 70:
        print("It is hot out! You should probably put on sunscreen and wear shorts and a t-shirt.")
    
    elif temp < 40:
        print("It is cold out! Bundle up! You should wear a coat and pants today!")

    else:
        print("It is cool outside you should proabably wear pants and a long sleeve shirt or a sweatshirt.")
