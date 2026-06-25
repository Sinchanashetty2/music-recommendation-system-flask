console.log("Music Recommendation System Loaded Successfully!");

const input = document.getElementById("song_name");
const suggestionsBox = document.getElementById("suggestions");

input.addEventListener("input", async () => {

    const query = input.value.trim();

    if(query.length === 0){

        suggestionsBox.innerHTML = "";

        return;
    }

    const response = await fetch(`/search?query=${query}`);

    const songs = await response.json();

    suggestionsBox.innerHTML = "";

    songs.forEach(song => {

        const div = document.createElement("div");

        div.classList.add("suggestion-item");

        div.innerText = song;

        div.onclick = () => {

            input.value = song;

            suggestionsBox.innerHTML = "";

        };

        suggestionsBox.appendChild(div);

    });

});