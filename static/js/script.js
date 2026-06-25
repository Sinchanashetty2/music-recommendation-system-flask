console.log("Music Recommendation System Loaded Successfully!");

const input = document.getElementById("song_name");
const suggestionsBox = document.getElementById("suggestions");

input.addEventListener("input", async function () {

    const query = input.value.trim();

    if (query.length === 0) {
        suggestionsBox.innerHTML = "";
        return;
    }

    try {

        const response = await fetch(`/search?query=${encodeURIComponent(query)}`);

        const songs = await response.json();

        suggestionsBox.innerHTML = "";

        songs.forEach(song => {

            const div = document.createElement("div");

            div.className = "suggestion-item";

            div.textContent = song;

            div.onclick = function () {

                input.value = song;

                suggestionsBox.innerHTML = "";

            };

            suggestionsBox.appendChild(div);

        });

    }

    catch (error) {

        console.error(error);

    }

});