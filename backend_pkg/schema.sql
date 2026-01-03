CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE emotion_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    emotion TEXT NOT NULL,
    detected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    input_type TEXT CHECK(input_type IN ('text','face')),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE playlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    emotion TEXT UNIQUE NOT NULL,
    playlist_name TEXT NOT NULL,
    songs TEXT NOT NULL  -- comma separated for now
);

CREATE TABLE saved_playlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    playlist_id INTEGER,
    saved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(playlist_id) REFERENCES playlists(id)
);
