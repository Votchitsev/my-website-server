from main import app
from fastapi.testclient import TestClient

from database.database import SessionLocal


client = TestClient(app)

session = SessionLocal()


def clear_db(model):
    session.query(model).delete()
    session.commit()
