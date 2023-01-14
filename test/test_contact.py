import json

from database.models import Contact, Language
from test.common import client, clear_db, session


def test_create_ru_contact():
    response = client.post(
        'contact/',
        json = {
    "name": "Тестовое Имя",
    "burth_date": "2023-01-01",
    "city": "Тестовый город",
    "email": "test@test.com",
    "phone": "+0 000 000 00 00",
    "current_job": "Тестовая работа",
    "language": "ru",
    "is_active": "true",
    })

    query_response = session.query(Contact).join(Language).filter(Language.name == 'ru')

    assert response.status_code == 200
    assert len(query_response.all()) == 1
    assert type(query_response.first().language_id) == int
    assert query_response.first().name == 'Тестовое Имя'
    assert query_response.first().city == 'Тестовый город'
    assert query_response.first().email == 'test@test.com'
    assert query_response.first().phone == '+0 000 000 00 00'
    assert query_response.first().current_job == 'Тестовая работа'
    
    clear_db(Contact)
