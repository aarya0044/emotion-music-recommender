from fastapi import UploadFile
import asyncio

async def detect_face_emotion(image: UploadFile) -> str:
    # Mock delay to simulate model processing
    await asyncio.sleep(1)
    return "happy"  # Always returns happy for now (placeholder)
