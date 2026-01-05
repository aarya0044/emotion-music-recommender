from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    name = Column(String(50), nullable=False)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    history = relationship("EmotionHistory", back_populates="user")
    playlists = relationship("SavedPlaylist", back_populates="user")

class EmotionHistory(Base):
    __tablename__ = "emotion_history"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    emotion = Column(String(20), nullable=False)
    input_text = Column(Text, nullable=True)
    detected_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="history")

class SavedPlaylist(Base):
    __tablename__ = "saved_playlists"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    emotion = Column(String(20))
    playlist_name = Column(String(100))
    playlist_data = Column(Text)
    saved_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="playlists")

class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String(20), unique=True, nullable=False)
    playlist_name = Column(String(100))
    playlist_songs = Column(Text)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    emotion = Column(String(20))
    song = Column(String(100))
    feedback = Column(Text)
    given_at = Column(DateTime, default=datetime.datetime.utcnow)
