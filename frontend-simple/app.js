async function detectEmotion() {
  const text = document.getElementById("textInput").value.trim();
  const resultDiv = document.getElementById("result");
  const songsDiv = document.getElementById("songs");

  if (!text) {
    resultDiv.innerText = "Please enter something!";
    return;
  }

  resultDiv.innerText = "Analyzing mood...";
  songsDiv.innerHTML = "";

  try {
    const res = await fetch("http://127.0.0.1:8000/detect/text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    resultDiv.innerText = "Detected Emotion: " + data.emotion;

    if (!data.songs || data.songs.length === 0) {
      songsDiv.innerHTML = "<p style='text-align:center; font-size:18px;'>No recommendations available</p>";
      return;
    }

    data.songs.forEach(song => {
      songsDiv.innerHTML += `
        <div class="song">
          <img src="https://picsum.photos/seed/${encodeURIComponent(song)}/200" alt="thumbnail"/>
          <div class="title">${song}</div>

          <!-- Spotify placeholder (won’t break UI) -->
          <iframe style="border-radius:12px; margin-top:10px;"
            src="https://open.spotify.com/embed/track/PLACEHOLDER_ID?utm_source=generator"
            width="100%" height="152" frameBorder="0"
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
            loading="lazy">
          </iframe>

          <a class="preview-btn" href="https://www.youtube.com/results?search_query=${encodeURIComponent(song + " song")}" target="_blank">▶ Preview</a>
        </div>
      `;
    });

  } catch (err) {
    resultDiv.innerText = "Server not reachable";
    console.error(err);
  }
}

function toggleTheme() {
  const body = document.body;
  body.classList.toggle("dark");
  body.classList.toggle("light");

  document.getElementById("toggleIcon").innerText =
    body.classList.contains("dark") ? "☀️" : "🌙";
}
