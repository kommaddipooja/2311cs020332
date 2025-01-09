import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000],
}

df = pd.DataFrame(data)
print(df)

import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob", "Diana"],
    "Age": [28, 34, 23, 29],
    "Department": ["HR", "IT", "Marketing", "Finance"],
    "Salary": [45000, 60000, 35000, 50000],
}

df = pd.DataFrame(data)

print("First 2 rows of the DataFrame:")
print(df.head(2))

df["Bonus"] = df["Salary"] * 0.1
print("\nDataFrame after adding the 'Bonus' column:")
print(df)

average_salary = df["Salary"].mean()
print(f"\nAverage salary of employees: {average_salary}")

filtered_employees = df[df["Age"] > 25]
print("\nEmployees older than 25:")
print(filtered_employees)
