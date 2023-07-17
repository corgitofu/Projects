import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = json.loads(response.text)
    return weather_data

def display_weather(weather_data):
    if weather_data["cod"] != "404":
        main_info = weather_data["main"]
        temperature = main_info["temp"]
        humidity = main_info["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        print(f"Weather: {weather_desc}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found.")

def main():
    api_key = input("Please find your openweathermap API key and enter it here")
    city = input("Enter city name: ")
    print("Fetching weather data...")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
