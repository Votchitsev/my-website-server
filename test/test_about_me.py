from fastapi.testclient import TestClient
import json

from database.models import AboutMe, Language
from database.database import SessionLocal
from main import app


client = TestClient(app)
session = SessionLocal()

def clear_db():
    session.query(AboutMe).delete()
    session.commit()


def test_create_ru_text():
    response = client.post(
        'about_me/',
        json = {
    "text": "Тестовый текст",
    "language": "ru",
    "is_active": "true"
    })

    query_response = session.query(AboutMe).join(Language).filter(Language.name == "ru")

    assert response.status_code == 200
    assert len(query_response.all()) == 1
    assert type(query_response.first().language_id) == int
    assert query_response.first().text == "Тестовый текст"

    session.query(AboutMe).delete()
    session.commit()


def test_create_en_text():
    response = client.post(
        'about_me/',
        json = {
    "text": "Тестовый текст",
    "language": "en",
    "is_active": "true"
    })

    query_response = session.query(AboutMe).join(Language).filter(Language.name == "en")

    assert response.status_code == 200
    assert len(query_response.all()) == 1
    assert type(query_response.first().language_id) == int
    assert query_response.first().text == "Тестовый текст"

    session.query(AboutMe).delete()
    session.commit()


def test_create_text_negative():
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

    session.query(AboutMe).delete()
    session.commit()


def test_create_additional_text_negative():

    client.post(
        'about_me/',
        json = {
            "text": "Тестовый текст",
            "language": "ru",
            "is_active": "true"
        }
    )


    client.post(
        'about_me/',
        json = {
            "text": "Test text",
            "language": "en",
            "is_active": "true"
        }
    )

    client.post(
        'about_me/',
        json = {
            "text": "Test text 2",
            "language": "en",
            "is_active": "true"
        }
    )

    all_texts = session.query(AboutMe).all()
    en_text = session.query(AboutMe).join(Language).filter(Language.name == 'en').first()
    
    assert len(all_texts) == 2
    assert en_text.text == 'Test text 2'


def test_get_text():
    client.post(
        'about_me/',
        json = {
            "text": "Тестовый текст",
            "language": "ru",
            "is_active": "true"
        }
    )

    response = client.get(
        'about_me/?lang=ru'
    )

    assert response.status_code == 200
    assert json.loads(response._content)['text'] == 'Тестовый текст'

    clear_db()


def test_get_from_empty_table():
    response = client.get(
        'about_me/?lang=ru'
    )

    assert response.status_code == 404
    assert json.loads(response._content)['detail'] == 'Text not found'
