import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned dataset
df = pd.read_csv("clean_spotify.csv")

# Features used for recommendation
FEATURES = [
    "danceability_%",
    "energy_%",
    "valence_%",
    "acousticness_%",
    "instrumentalness_%",
    "liveness_%",
    "speechiness_%"
]

# Create similarity matrix
feature_matrix = df[FEATURES]
similarity_matrix = cosine_similarity(feature_matrix)


def recommend_song(song_name, num_recommendations=5):
    """
    Returns a list of recommended songs.
    """

    # Remove extra spaces and convert to lowercase
    song_name = song_name.strip().lower()

    # Convert all song names to lowercase
    track_names = df["track_name"].str.lower()

    # Find songs containing the entered text
    matching_songs = track_names[track_names.str.contains(song_name, na=False)]

    # No matching songs
    if matching_songs.empty:
        return []

    # Select the first matching song
    song_index = matching_songs.index[0]

    # Calculate similarity scores
    similarity_scores = list(enumerate(similarity_matrix[song_index]))

    # Sort songs by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores:

        if index == song_index:
            continue

        recommendations.append({
            "track_name": df.iloc[index]["track_name"],
            "artist": df.iloc[index]["artist(s)_name"],
            "year": df.iloc[index]["released_year"],
            "streams": df.iloc[index]["streams"]
        })

        if len(recommendations) == num_recommendations:
            break

    return recommendations