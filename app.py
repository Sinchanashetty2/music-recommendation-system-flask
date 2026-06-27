from flask import Flask, render_template, request, jsonify
from recommendation import recommend_song, get_song_suggestions

app = Flask(__name__)


# ==========================================
# Home Page
# ==========================================
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Displays the home page and handles song recommendations.
    """

    recommendations = []
    message = ""

    if request.method == "POST":

        song_name = request.form.get("song_name", "").strip()

        if song_name:

            recommendations = recommend_song(song_name)

            if not recommendations:
                message = "❌ No matching song found. Please try another song."

    return render_template(
        "index.html",
        recommendations=recommendations,
        message=message
    )


# ==========================================
# Autocomplete Search
# ==========================================
@app.route("/search")
def search():
    """
    Returns song suggestions for autocomplete.
    """

    query = request.args.get("query", "").strip()

    suggestions = get_song_suggestions(query)

    return jsonify(suggestions)


# ==========================================
# Run Application
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)