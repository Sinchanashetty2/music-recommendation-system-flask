import pandas as pd

# Load the dataset
df = pd.read_csv("spotify.csv", encoding="latin1")

print("========== BEFORE CLEANING ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Remove duplicate songs
df = df.drop_duplicates(subset="track_name")

# Remove rows where song name is missing
df = df.dropna(subset=["track_name"])

# Keep only useful columns
df = df[
    [
        "track_name",
        "artist(s)_name",
        "released_year",
        "streams",
        "danceability_%",
        "energy_%",
        "valence_%",
        "acousticness_%",
        "instrumentalness_%",
        "liveness_%",
        "speechiness_%"
    ]
]

print("\n========== AFTER CLEANING ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== SAMPLE DATA ==========")
print(df.head())

# Save cleaned dataset
df.to_csv("clean_spotify.csv", index=False)

print("\nClean dataset saved successfully!")