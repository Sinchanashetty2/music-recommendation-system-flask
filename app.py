from flask import Flask, render_template, request
from recommendation import recommend_song

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    # Variables available for both GET and POST requests
    recommendations = []
    message = ""

    # Handle form submission
    if request.method == "POST":

        # Get the song entered by the user
        song_name = request.form["song_name"]

        # Get recommendations
        recommendations = recommend_song(song_name)

        # If no recommendations are found
        if not recommendations:
            message = "❌ No matching song found. Please try another song."

    # Always return the page
    return render_template(
        "index.html",
        recommendations=recommendations,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)