def detect_text_emotion(text: str) -> str:
    text = text.lower()
    if any(word in text for word in ["happy", "great", "love", "excited"]):
        return "happy"
    if any(word in text for word in ["sad", "cry", "miss", "heartbroken"]):
        return "sad"
    if any(word in text for word in ["angry", "hate", "furious", "annoyed"]):
        return "angry"
    if any(word in text for word in ["calm", "peace", "relax", "chill"]):
        return "calm"
    return "neutral"
