def recommend_music(emotion: str):
    playlists = {
        "happy": ["Here Comes The Sun", "Walking on Sunshine", "Good as Hell"],
        "sad": ["All I Want", "Fix You", "Let Her Go"],
        "angry": ["Break Stuff", "Look What You Made Me Do", "No Vaseline"],
        "calm": ["Weightless", "Sunset Lover", "Let You Go"],
        "neutral": ["Numb", "Blinding Lights", "Industry Baby"]
    }
    return playlists.get(emotion, ["No songs found for this mood yet"])
