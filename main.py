from fetchData import get_weather_data
from analyze_weather import analyze_weather

def main():
    # Fetch weather data
    weather_df = get_weather_data()

    # Analyze weather data
    total_rain = analyze_weather(weather_df)
    print(f"Total rain in April 2026: {total_rain} mm")

main()