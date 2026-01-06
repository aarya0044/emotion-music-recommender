from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random  # For random score

# Correct imports matching your actual folder structure
from backend_pkg.database import SessionLocal, Base, engine
from backend_pkg.models.face_emotion import detect_face_emotion
from backend_pkg.models.text_emotion import detect_text_emotion
from backend_pkg.recommender import recommend_music

app = FastAPI(title="Moodify API")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/detect/text")
def detect_text_api(data: TextInput):
    text = data.text.strip().lower()
    if not text:
        return {"error": "No text provided"}

    emotion = detect_text_emotion(text)
    score = random.randint(1, 100)  # Random score 1-100

    songs = recommend_music(emotion)

    return {
        "emotion": emotion,
        "score": score,
        "songs": songs
    }

@app.post("/detect/face")
async def detect_face_api(image: UploadFile = File(...)):
    emotion = await detect_face_emotion(image)
    return {"emotion": emotion}

@app.get("/music/recommend/{emotion}")
def get_recommendations_api(emotion: str):
    songs = recommend_music(emotion)
    return {"emotion": emotion, "recommendations": songs}