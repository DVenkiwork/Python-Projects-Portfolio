import pandas as pd

# Dataset 1: Customer Information
customers = {
    'CustomerID': [101, 102, 103, 104, 105], #104, 105 are not in Orders DF
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Houston']
}
df_customers = pd.DataFrame(customers)

# Dataset 2: Order Information
orders1 = {
    'OrderID': ['ORD1', 'ORD2', 'ORD3', 'ORD4', 'ORD5', 'ORD6'],
    'ClientID': [101, 103, 101, 106, 102, 107], # Note 106, 107 are new
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Desk Chair', 'Webcam'],
    'Amount': [1200, 25, 75, 300, 450, 40]
}

orders2 = {
    'OrderID': ['ORD1', 'ORD2', 'ORD4', 'ORD5', 'ORD6'],
    'CustomerID': [101, 103, 106, 102, 107], # Note 106, 107 are new
    'Product': ['Laptop', 'Mouse',  'Monitor', 'Desk Chair', 'Webcam'],
    'Amount': [1200, 25, 300, 450, 40]
}
df_orders = pd.DataFrame(orders1)

print("df_customers:\n", df_customers)
print("\ndf_orders:\n", df_orders)

# print("\n\n----Default Merge Operation-----")
# Df_merge = pd.merge(df_customers, df_orders)
# print(Df_merge)

# print("\n\n----Merge with On CustomerID-----")
# print(f"{pd.merge(df_customers, df_orders, on='CustomerID')}")

# print("\n\n----Merge with On Name-----") #KeyError as there is no common Key Name in give DFs
# print(f"{pd.merge(df_customers, df_orders, on='Name')}")

# print("\n\n----Merge with added How = 'left' with customers, orders-----")
# print(f"{pd.merge(df_customers, df_orders, on='CustomerID', how='left')}")

# print("\n\n----Merge with added How = 'left' with orders, customers-----")
# print(f"{pd.merge(df_orders, df_customers, on='CustomerID', how='left')}")

# print("\n\n----Merge with added How = 'right' with customers, orders-----")
# print(f"{pd.merge(df_customers, df_orders, on='CustomerID', how='right')}")

# print("\n\n----Merge with added How = 'right' with orders, customers-----")
# print(f"{pd.merge(df_orders, df_customers, on='CustomerID', how='right')}")

# print("\n\n----Merge with added How = 'outer' with customers, orders-----")
# print(f"{pd.merge(df_customers, df_orders, on='CustomerID', how='outer')}")

# print("\n\n----Merge with added How = 'inner' with customers, orders-----")
# print(f"{pd.merge(df_customers, df_orders, on='CustomerID', how='inner')}")

print("\n\n----Merge with added Left_on= 'CustomerID, right_on = 'ClientID' how = 'right' with customers, orders-----")
print(f"{pd.merge(df_customers, df_orders, left_on='CustomerID', right_on='ClientID', how='right')}")

print("\n\n----Merge with added Left_index= True, right_on = 'ClientID' how = 'right' with customers, orders-----")
print(f"{pd.merge(df_customers, df_orders, left_index= True, right_on='ClientID', how='right')}")

print("\n\n----Merge with added Left_index= True, right_index = True how = 'right' with customers, orders-----")
print(f"{pd.merge(df_customers, df_orders, left_index= True, right_index = True, how='right')}")