import pandas as pd

def analyze_weather(df):
    total_rain = df['precipitation'].sum()
    return total_rain
