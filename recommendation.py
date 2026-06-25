import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_csv("clean_spotify.csv")

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

# ==========================================
# Create Similarity Matrix
# ==========================================

feature_matrix = df[FEATURES]
similarity_matrix = cosine_similarity(feature_matrix)


# ==========================================
# Recommend Songs
# ==========================================

def recommend_song(song_name, num_recommendations=5):
    """
    Returns a list of recommended songs.
    """

    song_name = song_name.strip().lower()

    track_names = df["track_name"].str.lower()

    matching_songs = track_names[
        track_names.str.contains(song_name, na=False)
    ]

    if matching_songs.empty:
        return []

    song_index = matching_songs.index[0]

    similarity_scores = list(enumerate(similarity_matrix[song_index]))

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


# ==========================================
# Get Song Suggestions (Autocomplete)
# ==========================================

def get_song_suggestions(query, limit=5):
    """
    Returns a list of song names matching the search text.
    """

    query = query.strip().lower()

    if query == "":
        return []

    matches = df["track_name"][
        df["track_name"].str.lower().str.contains(query, na=False)
    ]

    suggestions = matches.drop_duplicates().head(limit).tolist()

    return suggestions