from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, checksum
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/checksum-news/")
def create_checksum_news(search_keys: list, db: Session = Depends(get_db)):
    result_checksum = checksum.checksum_news(search_keys)
    db_result = models.Result(endpoint="checksum-news", search_key=", ".join(search_keys), checksum=result_checksum)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

@app.post("/checksum-images-news/")
def create_checksum_images(search_keys: list, db: Session = Depends(get_db)):
    result_checksum = checksum.checksum_images(search_keys)
    db_result = models.Result(endpoint="checksum-images-news", search_key=", ".join(search_keys), checksum=result_checksum)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

@app.post("/checksum-files/")
def create_checksum_files(depth: int, db: Session = Depends(get_db)):
    result_checksum = checksum.checksum_files(depth)
    db_result = models.Result(endpoint="checksum-files", search_key=str(depth), checksum=result_checksum)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
