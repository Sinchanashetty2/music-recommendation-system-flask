// ==========================================
// EchoTune
// Autocomplete + Loading Animation
// ==========================================

document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("song_name");
    const suggestionsBox = document.getElementById("suggestions");
    const form = document.querySelector("form");
    const overlay = document.getElementById("loadingOverlay");
    const submitBtn = form.querySelector("button");

    // ==========================
    // Autocomplete Search
    // ==========================

    input.addEventListener("input", async () => {

        const query = input.value.trim();

        if (!query) {

            suggestionsBox.innerHTML = "";

            return;

        }

        try {

            const response = await fetch(
                `/search?query=${encodeURIComponent(query)}`
            );

            const songs = await response.json();

            suggestionsBox.innerHTML = "";

            songs.forEach(song => {

                const item = document.createElement("div");

                item.className = "suggestion-item";

                item.textContent = song;

                item.addEventListener("click", () => {

                    input.value = song;

                    suggestionsBox.innerHTML = "";

                });

                suggestionsBox.appendChild(item);

            });

        }

        catch (error) {

            console.error("Autocomplete Error:", error);

        }

    });

    // ==========================
    // Close Suggestions
    // ==========================

    document.addEventListener("click", (event) => {

        if (!event.target.closest(".search-section")) {

            suggestionsBox.innerHTML = "";

        }

    });

    // ==========================
    // Loading Animation
    // ==========================

    form.addEventListener("submit", () => {

        overlay.style.display = "flex";

        submitBtn.disabled = true;

        submitBtn.textContent = "Finding Songs...";

    });

});