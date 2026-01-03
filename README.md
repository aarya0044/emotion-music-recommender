# 🎧 Emotion-Based Music Recommender

A full-stack project that detects a user's emotion from text or facial expression and recommends songs accordingly.  
Built for learning and practical use with a focus on **ML integration + API-driven architecture**.

---

## 🚀 Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | React.js |
| Backend | FastAPI (Python) |
| ML Model | Hugging Face Transformer Pipeline |
| Database | SQLite (via SQLAlchemy ORM) |
| Server | Uvicorn |
| Deployment (future scope) | GitHub + Cloud |

---

## ✨ Features

- 🧠 Detect emotion from **text input**
- 📷 Detect emotion from **face expressions** (CV model)
- 🎶 Recommend songs based on detected emotion
- 💾 Store emotion history in SQL database
- 🌐 Interactive API docs using **Swagger UI**
- 🔄 Real-time reload for development

---

## 📁 Project Structure

emotion-music-recommender/
│── frontend/ # React UI
│── backend_pkg/ # FastAPI backend
│── models/ # Trained ML model files
│── data/ # Emotion-song mapping JSON
│── venv/ # Virtual environment
│── README.md # Project documentation


---

## 🛠 Setup Instructions

1. Clone the repo
2. Create & activate virtual environment
3. Install dependencies
4. Run FastAPI server using Uvicorn
5. Start frontend using `npm start`
6. Test API at `/detect/text` or `/detect/face`
7. View results & recommendations

---

## 📌 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/detect/text` | Detect emotion from text + recommend songs |
| POST | `/detect/face` | Detect emotion from image + recommend songs |
| GET | `/history` | Fetch stored emotion history |
| GET | `/recommend/{emotion}` | Get songs for a given emotion |
| GET | `/docs` | Swagger UI API documentation |

---

## 🧩 How It Works

1. User enters text or uploads an image
2. ML model predicts the emotion label
3. Backend fetches songs from `emotion_songs.json`
4. Emotion record is stored in SQLite DB
5. Songs + confidence score returned to UI

---

## 📈 Learning Goals

- Understanding FastAPI + ASGI server flow
- SQLAlchemy ORM model creation
- Integrating transformer-based ML models
- Building API-based recommendation logic
- Connecting backend ↔ frontend seamlessly

---

## 🔮 Future Enhancements

- User authentication
- Dynamic playlist creation (Spotify/YouTube)
- Mood analytics dashboard
- Cloud deployment
- Song filtering by language/genre

---

## 🤝 Acknowledgments

Built with guidance from ChatGPT and open-source ML tools.  
A project developed as part of academic learning and practical ML system building.

---

**Author:** Aarya Dharmadhikari  
SPPU – Information Technology (3rd Year)  
