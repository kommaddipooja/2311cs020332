sales_above_1000 = df[df["Sales"] > 1000]
print("Rows with sales greater than 1000:")
print(sales_above_1000)

east_sales = df[df["Region"] == "East"]
print("\nSales records for the 'East' region:")
print(east_sales)

df["Profit_Per_Unit"] = df["Profit"] / df["Quantity"]
df["High_Sales"] = df["Sales"].apply(lambda x: "Yes" if x > 1000 else "No")

print(df.head())
