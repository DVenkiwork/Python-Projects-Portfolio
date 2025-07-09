# pivot_table

import pandas as pd

# Data for January Sales
data_jan = {
    'OrderID': ['A001', 'A002', 'A003', 'A004'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Webcam'],
    'Sales': [1200, 25, 75, 40],
    'Region': ['East', 'East', 'West', 'North'],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb']
}
df_jan_sales = pd.DataFrame(data_jan)

print(df_jan_sales)

df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

# DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=<no_default>, sort=True)[source]
df_jan_sales_pt = pd.pivot_table(df, values='D', index=['A', 'B'],
                       columns=['C'], aggfunc="sum", fill_value=0)


print ("Sample Dataframe to use for pivot Table")
print(df)
print("\n\n-------Pivot Table-------------")
print(df_jan_sales_pt)

# DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=<no_default>, sort=True)[source]
df_jan_sales_pt = pd.pivot_table(df_jan_sales, values='Sales', index = ['OrderID', 'Product'], columns = 'Month', aggfunc= 'sum', fill_value='novalue')

print("\n\n-------Pivot Table, fill value-------------")
print(df_jan_sales_pt)

table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                       aggfunc={'D': "mean", 'E': "mean"})

print(table)

table2 = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                       aggfunc={'D': "mean",
                                'E': ["min", "max", "mean"]})

print(table2)

