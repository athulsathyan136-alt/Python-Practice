import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    data = requests.get(url,timeout=10).json()
    if "results" in data and len(data["results"]) > 0:
        r = data["results"][0]
        return{
            "name":r["name"],
            "country":r.get("country",'N/A'),
            "lat":r["latitude"],
            "long":r["longitude"],
        }
    return None

def get_forecast(lat,long,day = 7):
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={long}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&timezone=auto&forecast_days={day}"
    )
    data = requests.get(url,timeout=10).json()
    daily = data.get("daily",{})
    return pd.DataFrame({
         "date":daily.get("time",[]),
         "max_temp":daily.get("temperature_2m_max",[]),
         "min_temp":daily.get("temperature_2m_min",[]),
         "rain_mm":daily.get("precipitation_sum",[]),   
        })


def main():
    print('='*50)
    print("🌤️  WEATHER DASHBOARD")
    print('='*50)

    city = input('\n Enter a city name: ')

    print(f"\n🔍 Fetching weather for '{city}'...")
    location = get_coordinates(city)
    if not location:
        print(f"❌ City '{city}' not found.")
        return
    print(f" found:{location['name']},{location['country']} ")
    df = get_forecast(location['lat'], location['long'])

    if df.empty:
        print("❌ Could not fetch forecast.")
        return

    print('\n' +'=' *50)
    print(f"📅 7-DAY FORECAST FOR {location['name'].upper()}")
    print('='*50)
    print(df.to_string(index=False))

    print('\n STATISTICS')
    print('='*50)
    print(f"Avg Max temp: {df['max_temp'].mean():.1f}°C")
    print(f"Avg Min temp: {df['min_temp'].mean():.1f}°C")
    print(f"Warmest Day:{df.loc[df['max_temp'].idxmax() , 'date']}({df['max_temp'].max()}°C)")
    print(f"Coldest Day:{df.loc[df['min_temp'].idxmin() , 'date']}({df['min_temp'].min()}°C)")
    print(f"Total Rain {df['rain_mm'].sum():.1f}mm")

    fig,(ax1,ax2) = plt.subplots(2,1,figsize=(12,8))

    ax1.plot(df["date"],df["max_temp"], "r-o",label="Max Temp",linewidth=2)
    ax1.plot(df["date"],df["min_temp"], "r-o",label="Min Temp",linewidth=2)
    ax1.fill_between(df["date"],df["min_temp"],df["max_temp"],alpha=0.2,color='orange')
    ax1.set_title(f"Temperature Forecast -{location['name']}",fontsize=14,fontweight="bold")
    ax1.set_ylabel("temperature (°C)")
    ax1.legend()
    ax1.grid(True,alpha=0.3)

    ax2.bar(df['date'],df["rain_mm"],color='steelblue',edgecolor='black')
    ax2.set_title(f"Percipitation Forecast",fontsize=14,fontweight="bold")
    ax2.set_ylabel("Rain (mm)")
    ax2.grid(True,alpha=0.3,axis="y")

    plt.tight_layout()
    plt.savefig('Weather_dashboard.png',dpi=150)
    plt.show()

    df.to_csv('Weather_dashboard.csv',index=False)
    print("\n✅ Chart saved: weather_dashboard.png")
    print("✅ Data saved: weather_forecast.csv")

if __name__ == "__main__":
    main()