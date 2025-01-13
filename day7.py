import pandas as pd
from io import StringIO

data = """
Date,Product,Region,Sales,Profit,Quantity
2023-01-02,Tablet,East,1061.81,236.12,7
2023-01-06,Laptop,North,1926.07,246.34,8
2023-01-03,Tablet,East,1597.99,253.17,3
2023-01-20,Tablet,North,1397.99,242.23,1
2023-01-04,Laptop,West,734.03,140.36,4
2023-01-17,Tablet,North,733.99,188.66,2
2023-01-14,Keyboard,East,587.13,82.16,8
2023-01-07,Smartphone,East,1799.26,364.97,4
2023-01-11,Smartphone,West,1401.67,306.24,2
2023-01-01,Laptop,North,1562.11,170.72,6
2023-01-19,Monitor,North,530.88,117.59,6
2023-01-12,Laptop,West,1954.86,262.16,4
2023-01-09,Monitor,North,1748.66,197.62,6
2023-01-10,Smartphone,North,818.51,237.19,2
2023-01-08,Laptop,East,772.74,226.51,2
2023-01-05,Keyboard,North,775.11,202.83,4
2023-01-15,Tablet,North,956.36,153.9,8
2023-01-18,Monitor,West,1287.13,153.86,7
2023-01-13,Tablet,West,1147.92,271.88,9
2023-01-16,Tablet,South,936.84,176.15,8
"""

df = pd.read_csv(StringIO(data))

print("First 5 rows of the dataset:")
print(df.head())

print("\nBasic statistics:")
print(df.describe())

total_sales_by_region = df.groupby("Region")["Sales"].sum()
print("Total sales for each region:")
print(total_sales_by_region)

most_sold_product = df.groupby("Product")["Quantity"].sum().idxmax()
print("\nMost sold product (based on quantity):", most_sold_product)

df["Profit Margin (%)"] = (df["Profit"] / df["Sales"]) * 100
average_profit_margin_by_product = df.groupby("Product")["Profit Margin (%)"].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin_by_product)
