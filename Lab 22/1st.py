import pandas as pd

data = {
    "Name": ["Kenil", "BOB", "Charlie"],
    "Age": [21, 25, 35],
    "City": ["Rajkot", "Los Angeles", "London"],
    "Salary": [70000.0, 50000.0, 80000.0],
    "Is_Manager": [True, False, True]
}

df = pd.DataFrame(data)

print("Data types of each column:")
print(df.dtypes)
