from fastapi.testclient import TestClient
from database.models import AboutMe, Language
from database.database import SessionLocal

from main import app


client = TestClient(app)
session = SessionLocal()

def test_create_ru_text():
    response = client.post(
        'about_me/',
        json = {
    "text": "Тестовый текст",
    "language": "ru",
    "is_active": "true"
    })

    assert response.status_code == 200

    query_response = session.query(AboutMe).join(Language).filter(Language.name == "ru")

    assert len(query_response.all()) == 1
    assert type(query_response.first().language_id) == int
    assert query_response.first().text == "Тестовый текст"

    query_response = session.query(AboutMe).delete()
    session.commit()


def test_create_ru_text_negative():
    response = client.post(
        'about_me/',
        json = {
            "text": "Тестовый текст",
            "language": "it",
            "is_active": "true"
        }
    )

    assert response.status_code == 422

    query_response = session.query(AboutMe).all()

    assert len(query_response) == 0

    if len(query_response) > 0:
        session.query(AboutMe).delete()
