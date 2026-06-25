import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
df = pd.read_csv("clean_spotify.csv")

# Features used for recommendation
features = [
    "danceability_%",
    "energy_%",
    "valence_%",
    "acousticness_%",
    "instrumentalness_%",
    "liveness_%",
    "speechiness_%"
]

# Create similarity matrix
feature_matrix = df[features]
similarity_matrix = cosine_similarity(feature_matrix)


def recommend_song(song_name):
    # Check if the song exists
    if song_name not in df["track_name"].values:
        print("Song not found!")
        return

    # Get the index of the song
    song_index = df[df["track_name"] == song_name].index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(similarity_matrix[song_index]))

    # Sort by similarity score (highest first)
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print(f"\nRecommendations for '{song_name}':\n")

    count = 0

    for index, score in similarity_scores:

        if index == song_index:
            continue

        print(
            f"{count + 1}. {df.iloc[index]['track_name']} "
            f"- {df.iloc[index]['artist(s)_name']}"
        )

        count += 1

        if count == 5:
            break


# Test
recommend_song("Cruel Summer")