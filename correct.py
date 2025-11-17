import requests

def get_weather(city_name):
    # ✅ Use your actual API key here
    API_KEY = "63e9bacd9668740ab99f3d65f7ddb2db"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # 'metric' gives temperature in Celsius
    }

    try:
        # Sending GET request to the API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises an error for bad responses (4xx/5xx)

        # Extracting JSON data from response
        data = response.json()

        # Extracting important info
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']

        # Neatly display the data
        print("\n------------------------------------")
        print(f" Weather Report for {city}, {country}")
        print("------------------------------------")
        print(f" Temperature : {temperature}°C")
        print(f" Humidity    : {humidity}%")
        print(f" Condition   : {weather_condition.capitalize()}")
        print("------------------------------------\n")

    except requests.exceptions.HTTPError:
        print("❌ Error: Invalid city name or API key.")
    except requests.exceptions.ConnectionError:
        print("🌐 Network error. Please check your internet connection.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    print("====== Real-Time Weather App ======")
    city = input("Enter city name: ").strip()
    get_weather(city)
