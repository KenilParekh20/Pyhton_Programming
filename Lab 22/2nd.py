import pandas as pd
import numpy as np

data = {
    "Name": ["Om", "Priya", "Rahul", "Sneha", "Rohit"],
    "Age": [28, 32, np.nan, 30, 27],
    "Salary": [50000, 60000, 45000, np.nan, 48000]
}

df = pd.DataFrame(data)

print("Original Data with missing values:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\nData after filling missing values with mean:")
print(df)
