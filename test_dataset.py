import pandas as pd

# Load the dataset
df = pd.read_csv("spotify.csv", encoding="latin1")

# Display first 5 rows
print(df.head())

print("\n----------------------------")

print("Dataset Shape:")
print(df.shape)

print("\n----------------------------")

print("Columns:")
print(df.columns.tolist())