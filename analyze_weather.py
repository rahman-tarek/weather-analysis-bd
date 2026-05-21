import pandas as pd

def analyze_weather(df):

    # Total rain 
    total_rain = df['precipitation'].sum()
    # Average temperature
    avg_temp = df['temperature_2m'].mean()
    return total_rain, avg_temp
