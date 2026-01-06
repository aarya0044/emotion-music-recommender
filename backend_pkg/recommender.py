import json
import random

def recommend_music(emotion: str):
    # Try to load from emotion_songs.json for extensive lists
    try:
        with open('backend_pkg/models/emotion_songs.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        songs_data = data.get(emotion.lower(), [])
        if songs_data:
            # If JSON has objects, use them; else, assume strings and parse
            if isinstance(songs_data[0], dict):
                return songs_data  # Already structured
            else:
                # Parse strings like "Title – Artist"
                return [
                    {
                        "title": song.split(" – ")[0].strip(),
                        "artist": song.split(" – ")[1].strip() if " – " in song else "Unknown Artist",
                        "duration": f"{random.randint(3,5)}:{random.randint(10,59):02d}"  # Mock duration
                    }
                    for song in songs_data
                ]
    except (FileNotFoundError, KeyError, IndexError):
        pass  # Fallback to hardcoded playlists

    # Fallback hardcoded playlists (expanded for extensiveness)
    playlists = {
        "happy": [
            {"title": "Here Comes The Sun", "artist": "The Beatles", "duration": "3:05"},
            {"title": "Walking on Sunshine", "artist": "Katrina & The Waves", "duration": "3:43"},
            {"title": "Good as Hell", "artist": "Lizzo", "duration": "2:39"},
            {"title": "Tum Hi Ho", "artist": "Arijit Singh", "duration": "4:22"},
            {"title": "Senorita", "artist": "Shawn Mendes, Camila Cabello", "duration": "3:10"},
            {"title": "Kar Gayi Chull", "artist": "Badshah", "duration": "3:05"},
            {"title": "Gallan Goodiyan", "artist": "YRF", "duration": "4:18"},
            {"title": "Happy", "artist": "Pharrell Williams", "duration": "3:53"},
            {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "duration": "3:56"},
            {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "duration": "4:30"}
        ],
        "sad": [
            {"title": "Fix You", "artist": "Coldplay", "duration": "4:55"},
            {"title": "All I Want", "artist": "Kodaline", "duration": "5:05"},
            {"title": "Let Her Go", "artist": "Passenger", "duration": "4:12"},
            {"title": "Channa Mereya", "artist": "Arijit Singh", "duration": "4:49"},
            {"title": "Agar Tum Saath Ho", "artist": "Arijit Singh", "duration": "5:41"},
            {"title": "Someone Like You", "artist": "Adele", "duration": "4:45"},
            {"title": "Hurt", "artist": "Nine Inch Nails", "duration": "3:36"},
            {"title": "The Night We Met", "artist": "Lord Huron", "duration": "3:23"}
        ],
        "angry": [
            {"title": "Look What You Made Me Do", "artist": "Taylor Swift", "duration": "3:31"},
            {"title": "Break Stuff", "artist": "Limp Bizkit", "duration": "2:47"},
            {"title": "Gussa", "artist": "EMIWAY", "duration": "3:15"},
            {"title": "Zinda", "artist": "Siddharth Mahadevan", "duration": "4:02"},
            {"title": "Killing in the Name", "artist": "Rage Against the Machine", "duration": "5:14"},
            {"title": "Bitch Better Have My Money", "artist": "Rihanna", "duration": "3:39"}
        ],
        "calm": [
            {"title": "Weightless", "artist": "Marconi Union", "duration": "8:06"},
            {"title": "Sunset Lover", "artist": "Petit Biscuit", "duration": "4:44"},
            {"title": "Raabta (Soft)", "artist": "Arijit Singh", "duration": "4:03"},
            {"title": "Phir Le Aya Dil", "artist": "Arijit Singh", "duration": "5:37"},
            {"title": "River", "artist": "Joni Mitchell", "duration": "4:03"},
            {"title": "Holocene", "artist": "Bon Iver", "duration": "5:36"}
        ],
        "neutral": [
            {"title": "Numb", "artist": "Linkin Park", "duration": "3:07"},
            {"title": "Industry Baby", "artist": "Lil Nas X", "duration": "3:32"},
            {"title": "Heat Waves", "artist": "Glass Animals", "duration": "3:58"},
            {"title": "Bekhayali", "artist": "Sachet Tandon", "duration": "6:12"},
            {"title": "Blinding Lights", "artist": "The Weeknd", "duration": "3:20"},
            {"title": "Levitating", "artist": "Dua Lipa", "duration": "3:23"}
        ]
    }

    return playlists.get(emotion.lower(), [{"title": "No songs found for this mood yet", "artist": "Unknown", "duration": "0:00"}])