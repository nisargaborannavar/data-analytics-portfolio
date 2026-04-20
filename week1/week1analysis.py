import pandas as pd


df = pd.read_csv("student.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nNull counts:\n", df.isnull().sum())
print("\nFirst 5 rows:\n", df.head())