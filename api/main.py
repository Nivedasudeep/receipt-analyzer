from fastapi import FastAPI, UploadFile, File
from backend.parser import parse_file
from backend.models import Receipt
from backend.database import SessionLocal, init_db
from sqlalchemy.orm import Session
from typing import List
import shutil

app = FastAPI()
init_db()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    with open("temp_file", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    parsed = parse_file("temp_file")
    if parsed:
        db = SessionLocal()
        receipt = Receipt(**parsed)
        db.add(receipt)
        db.commit()
        db.refresh(receipt)
        db.close()
        return {"message": "Uploaded", "data": parsed}
    return {"error": "Could not parse"}
