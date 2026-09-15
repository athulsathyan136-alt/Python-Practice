import requests

def get_coo(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    try:
        response = requests.get(url,timeout=10)
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            return {
                "name":result["name"],
                "country":result.get("country","N/A"),
                "latitude":result["latitude"],
                "longitude":result["longitude"]
            }
        return None
    except Exception as e:
        print(f"Error fetching location: {e}")
        return None

def get_weather(lat,lon):
    url  = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    try:
        reponse = requests.get(url,timeout=10)
        data = reponse.json
        return data.get("current_weather",None)
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None

def get_weather_desc(code):
    weather_codes = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy ⛅",
        3: "Overcast ☁️",
        45: "Foggy 🌫️",
        51: "Light drizzle 🌦️",
        61: "Slight rain 🌧️",
        63: "Moderate rain 🌧️",
        71: "Slight snow ❄️",
        80: "Rain showers 🌦️",
        95: "Thunderstorm ⛈️"

    }    
    return weather_codes.get(code,f"Unknown ({code})")

def display(city_data,weather_data):
    print("\n" + "=" * 50)
    print(f"🌍 WEATHER FOR {city_data['name'].upper()}, {city_data['country']}")
    print("=" * 50)

    print(f"🌡️  Temperature: {weather_data['temperature']}°C")
    print(f"💨 Wind Speed: {weather_data['windspeed']} km/h")
    print(f"🧭 Wind Direction: {weather_data['winddirection']}°")
    print(f"☁️  Condition: {get_weather_desc(weather_data['weathercode'])}")
    print(f"⏰ Updated: {weather_data['time']}")
    print("="*50)

def main():
    print("="*50)
    print('🌤️  WEATHER APP')
    print("="*50)

    while True:
        city = input("\nEnter a city name (or 'quit' to exit): ").strip()

        if city.lower() == 'quit':
            print("Goodbye! ")
            break

        if not city:
            print("❌ Please enter a valid city name.")
            continue
        print(f"\n🔍 Searching for '{city}'...")
        location = get_coo(city)

        if not location:
            print(f"❌ Could not find '{city}'. Try another city.")
            continue
        
        weather = get_weather(location["latitude"],location["longitude"])
        if not weather:
            print("❌ Could not fetch weather data.")
            continue

        display(location,weather)

if __name__ == "__main__":
    main()
