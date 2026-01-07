# Moodify 🎵  
**Emotion-based Music Recommender**

Moodify detects emotion from text using NLP and recommends songs with YouTube & Spotify links.

## Features
- Text emotion detection (Happy, Sad, Angry, Neutral, etc.)
- Music suggestions by mood
- Responsive UI + Dark/Light mode
- Real-time results with confidence score

## Live Demo
https://emotion-music-recommender-kc88.onrender.com/

## Tech Stack
- **Backend:** FastAPI, Uvicorn, SQLite (SQLAlchemy)
- **Frontend:** HTML, CSS, JavaScript
- **Deployment:** Render (Free Tier)

## Run Locally
```bash
git clone https://github.com/your-username/emotion-music-recommender.git
pip install -r requirements.txt
uvicorn backend_pkg.main:app --reload
Open: http://localhost:8000

API Example
curl -X POST "http://localhost:8000/detect/text" -H "Content-Type: application/json" -d "{\"text\": \"I am happy\"}"

Contribute

Fork → Branch → Commit → Pull Request (Follow PEP 8)

License

MIT License © 2025 — Aarya Dharmadhikari
