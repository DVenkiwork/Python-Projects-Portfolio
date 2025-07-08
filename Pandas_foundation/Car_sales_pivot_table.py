# Objective: extracting required data from Car_sales.scsv using pivot table

import pandas as pd 

df = pd.read_csv("Car_sales.csv")

print(df)

# What is the average __year_resale_value for each Vehicle_type?

# Hint: 'Vehicle_type' is the index, '__year_resale_value' is the value, and the function is 'mean'.
avg_resale_value = df.pivot_table(index='Vehicle_type', values='__year_resale_value', aggfunc='mean')
print("\n\nAverage __year_resale_value for each Vehicle_type")
print(avg_resale_value)

# What is the total Sales_in_thousands for each Manufacturer, broken down by Vehicle_type?
total_sales_per_manufacture = df.pivot_table(index=['Manufacturer','Vehicle_type'], values='Sales_in_thousands', aggfunc='sum' )
print("\n\nTotal Sales_in_thousands for each Manufacturer, broken down by Vehicle_type")
print(total_sales_per_manufacture)

# Hint: 'Manufacturer' is the index, 'Vehicle_type' is the columns, 'Sales_in_thousands' is the value, and the function is 'sum'.
print(df.pivot_table(index='Manufacturer', columns='Vehicle_type', values='Sales_in_thousands', aggfunc='sum'))