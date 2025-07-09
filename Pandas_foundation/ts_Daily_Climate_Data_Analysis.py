# Objective: To implement Time series functionality to analyse Daily Climate Data Analysis

import pandas as pd 
import datetime

#importing data as pandas dataframe from csv
df = pd.read_csv('DailyDelhiClimateTrain.csv') 
print("Imported data Info is:")
print(df.info())
print("Imported data Header is:")
print(df.head())

# Convert to Datetime & Set as Index
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
# Or more concisely: df = pd.read_csv('path/to/DailyDelhiClimateTrain.csv', parse_dates=['Date'], index_col='Date')
print("\n\n-----After Conversion to Datetime for Date column-------")
print(df.info())
print("Imported data Header after conversion is:")
print(df.head())

# Resample Data (Weekly and Monthly Averages):
weekly_avg_temp = df['meantemp'].resample('W').mean() # 'W' for weekly
print("\nWeekly Average Temperature Header:\n", weekly_avg_temp.head())
print("\nWeekly Average Temperature Tail:\n", weekly_avg_temp.tail())

monthly_max_humidity = df['humidity'].resample('ME').max() # 'M' for monthly
print("\nMonthly Max Humidity Header:\n", monthly_max_humidity.head())
print("\nMonthly Max Humidity Tail:\n", monthly_max_humidity.tail())

# Calculate Rolling Averages
meantemp_7day_rolling_avg = df['meantemp'].resample('7D', closed='left').mean() #7D for 7 calendar days
print("\nmeantemp 7 day rolling avg:\n", meantemp_7day_rolling_avg.head())
df['Meantemp_7day_rolling_avg'] = meantemp_7day_rolling_avg
print("\nNew updated dataframe")
print(df)

df['Meantemp_7day_rolling_avg'] = df['meantemp'].rolling(window=7).mean()
print("\nDataFrame with 7-day Rolling Average:\n", df.head(10))