import pandas as pd

# Load dataset
df = pd.read_csv("spotify.csv", encoding="latin1")

# Basic information
print("========== DATASET INFO ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE SONGS ==========")
print(df.duplicated().sum())

print("\n========== FIRST 5 SONGS ==========")
print(df[['track_name', 'artist(s)_name', 'streams']].head())