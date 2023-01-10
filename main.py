from fastapi import FastAPI
from database.database import Base, engine, SessionLocal
from database import models
from database.create_language import create_languages

Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

create_languages(SessionLocal())
