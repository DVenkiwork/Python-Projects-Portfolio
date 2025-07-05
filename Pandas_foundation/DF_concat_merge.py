# Objective: To learn on concat concepts


import pandas as pd

# Data for January Sales
data_jan = {
    'OrderID': ['A001', 'A002', 'A003', 'A004'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Webcam'],
    'Sales': [1200, 25, 75, 40],
    'Region': ['East', 'East', 'West', 'North'],
    'Month': ['Jan', 'Jan', 'Jan', 'Jan']
}
df_jan_sales = pd.DataFrame(data_jan)

# Data for February Sales (similar structure)
data_feb = {
    'OrderID': ['B001', 'B002', 'B003', 'B004'],
    'Product': ['Monitor', 'Desk Chair', 'Speakers', 'Headphones'],
    'Sales': [300, 450, 100, 80],
    'Region': ['South', 'East', 'West', 'North'],
    'Month': ['Feb', 'Feb', 'Feb', 'Feb']
}
df_feb_sales = pd.DataFrame(data_feb)

print("df_jan_sales:\n", df_jan_sales)
print("\ndf_feb_sales:\n", df_feb_sales)

#  default behavior, axis = 0, to concat across rows 
print("\n\n-------Default Concat operations-------")
combined_df_janfeb = pd.concat([df_jan_sales, df_feb_sales])
print(combined_df_janfeb)

print("\n\n-------Default Concat operations-------")
combined_df_febjan = pd.concat([df_feb_sales,df_jan_sales])
print(combined_df_febjan)