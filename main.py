from fetchData import get_weather_data
from analyze_weather import analyze_weather

def main():
    # Fetch weather data
    weather_df = get_weather_data()

    # Analyze weather data
    total_rain, avg_temp, hottest_day, mx_temp, mn_temp, coolest_day = analyze_weather(weather_df)


    print("Weather Analysis for Dhaka - April 2026")
    print(f"Total Rain in April 2026: {total_rain} mm")
    print(f"Average Temperature in April 2026: {avg_temp}°C")
    print(f"Hottest Day in April 2026: {hottest_day}, Temperature: {mx_temp}°C")
    print(f"Coolest Day in April 2026: {coolest_day}, Temperature: {mn_temp}°C")

main()