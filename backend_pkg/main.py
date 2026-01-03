from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from models.text_emotion import detect_text_emotion
from models.face_emotion import detect_face_emotion
from models.recommender import recommend_music

app = FastAPI(title="Emotion Music Recommender API")

class TextInput(BaseModel):
    text: str

@app.post("/detect/text")
async def detect_text(data: TextInput):
    emotion = detect_text_emotion(data.text)
    return {"emotion": emotion}

@app.post("/detect/face")
async def detect_face(image: UploadFile = File(...)):
    emotion = await detect_face_emotion(image)
    return {"emotion": emotion}

@app.get("/music/recommend/{emotion}")
def get_recommendations(emotion: str):
    songs = recommend_music(emotion)
    return {"emotion": emotion, "recommendations": songs}

@app.post("/music/recommend")
async def detect_and_recommend(data: TextInput):
    emotion = detect_text_emotion(data.text)
    songs = recommend_music(emotion)
    return {"emotion": emotion, "recommendations": songs}

