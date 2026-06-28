from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/{user_id}/files/save")
def save_user_file(user_id: int, file: schemas.SavedFileCreate, db: Session = Depends(get_db)):
    db_file = models.SavedFile(
        owner_id=user_id,
        file_name=file.file_name,
        encrypted_content=file.encrypted_content
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return {"message": "File saved successfully", "file_id": db_file.id}

@app.post("/users/{user_id}/files/receive")
def receive_file(user_id: int, file: schemas.ReceivedFileCreate, db: Session = Depends(get_db)):
    db_file = models.ReceivedFile(
        receiver_id=user_id,
        sender_id=file.sender_id,
        file_name=file.file_name,
        encrypted_content=file.encrypted_content
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return {"message": "File received successfully", "file_id": db_file.id}