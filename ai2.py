import requests
import json

# Define function to get weather data from OpenWeatherMap API
def get_weather_data(city):
    api_key = "your_api_key_here"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        return f"The temperature in {city} is {temp} degrees Celsius and the weather is {weather}."
    else:
        return "Sorry, there was an error fetching the weather data."

# Define function to query the user for their name and location, and provide a welcome message
def get_user_info():
    name = input("Hello! What is your name? ")
    location = input("What city are you in? ")
    weather = get_weather_data(location)
    print(f"Welcome {name}! {weather}")

# Call the get_user_info function to start the program
get_user_info()
