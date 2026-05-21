import pandas as pd

def analyze_weather(df):

    # Total rain 
    total_rain = df['precipitation'].sum()
    # Average temperature
    avg_temp = df['temperature_2m'].mean()
    # Hottest day
    hottest_day = df.loc[df.temperature_2m.idxmax()]['time']
    # Max temperature
    mx_temp = df['temperature_2m'].max()

    return total_rain, avg_temp, hottest_day, mx_temp
