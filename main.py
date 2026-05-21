from fetchData import get_weather_data
from analyze_weather import analyze_weather

def main():
    # Fetch weather data
    weather_df = get_weather_data()

    # Analyze weather data
    total_rain, avg_temp = analyze_weather(weather_df)

    print("Weather Analysis for Dhaka - April 2026")
    print(f"Total Rain in April 2026: {total_rain} mm")
    print(f"Average Temperature in April 2026: {avg_temp}°C")

main()