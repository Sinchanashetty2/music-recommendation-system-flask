import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("data/clean_spotify.csv")

# ==========================================
# Features Used for Recommendation
# ==========================================

FEATURES = [
    "danceability_%",
    "energy_%",
    "valence_%",
    "acousticness_%",
    "instrumentalness_%",
    "liveness_%",
    "speechiness_%"
]

DEFAULT_RECOMMENDATIONS = 5

# ==========================================
# Prepare Data
# ==========================================

feature_matrix = df[FEATURES]

similarity_matrix = cosine_similarity(feature_matrix)

# Store lowercase song names once for faster searching
track_names = df["track_name"].str.lower()

# ==========================================
# Recommend Songs
# ==========================================

def recommend_song(song_name, num_recommendations=DEFAULT_RECOMMENDATIONS):
    """
    Returns a list of songs similar to the given song.
    """

    song_name = song_name.strip().lower()

    matching_tracks = track_names[
        track_names.str.contains(song_name, na=False)
    ]

    if matching_tracks.empty:
        return []

    selected_song_index = matching_tracks.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[selected_song_index])
    )

    similarity_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in similarity_scores:

        # Skip the selected song itself
        if index == selected_song_index:
            continue

        song = df.iloc[index]

        recommendations.append({

            "track_name": song["track_name"],

            "artist": song["artist(s)_name"],

            "year": song["released_year"],

            "streams": song["streams"],

            "similarity": round(score * 100, 1)

        })

        if len(recommendations) >= num_recommendations:
            break

    return recommendations


# ==========================================
# Autocomplete Suggestions
# ==========================================

def get_song_suggestions(query, limit=5):
    """
    Returns song names matching the search query.
    """

    query = query.strip().lower()

    if not query:
        return []

    matches = df["track_name"][
        track_names.str.contains(query, na=False)
    ]

    return matches.drop_duplicates().head(limit).tolist()