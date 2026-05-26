import requests
import pandas as pd

def get_weather_data():
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 23.8103,   # Dhaka
        "longitude": 90.4125,
        "start_date": "2026-04-01",
        "end_date": "2026-04-30",
        "hourly": "temperature_2m,precipitation,wind_speed_10m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data['hourly'])
    
    return df