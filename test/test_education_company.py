import json

from test.common import client, clear_db, session
from database.models import EducationCompany, Language


def test_create_ru_edu():
    response = client.post('edu/', json = {
        "name": "Тестовое Имя",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "ru"
    })
    
    query_response = session.query(EducationCompany).join(Language).filter(Language.name == 'ru')

    assert response.status_code == 200
    assert len(query_response.all()) == 1
    assert query_response.first().name == 'Тестовое Имя'


def test_create_en_edu():
    response = client.post('edu/', json = {
        "name": "Test Name",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "en"
    })
    
    query_response = session.query(EducationCompany).join(Language).filter(Language.name == 'en')

    assert response.status_code == 200
    assert len(query_response.all()) == 1
    assert query_response.first().name == 'Test Name'

    clear_db(EducationCompany)


def test_create_negative_edu():
    response = client.post('edu/', json = {
        "name": "Test Name",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "it"
    })

    query_response = session.query(EducationCompany).all()

    assert response.status_code == 422
    assert len(query_response) == 0

    clear_db(EducationCompany)


def test_create_additional_edu_negative():
    client.post('edu/', json = {
        "name": "Тестовое Имя",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "ru"
    })

    client.post('edu/', json = {
        "name": "Test Name",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "en"
    })

    client.post('edu/', json = {
        "name": "Тестовое Имя 2",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "ru"
    })


    all_edu = session.query(EducationCompany).all()
    ru_edu = session.query(EducationCompany).join(Language).filter(Language.name == 'ru').first()

    assert len(all_edu) == 2
    assert ru_edu.name == 'Тестовое Имя 2'


def test_get_edu():
    response = client.get(
        'edu/?lang=ru'
    )

    assert response.status_code == 200
    assert json.loads(response._content)['name'] == 'Тестовое Имя 2'
    
    clear_db(EducationCompany)


def test_delete_edu():
    client.delete('/?id=1')

    query_response = session.query(EducationCompany).filter(EducationCompany.id == 1).all()
    assert len(query_response) == 0


def test_get_from_empty_table():
    response = client.get(
        'edu/?lang=ru'
    )

    assert response.status_code == 404
    assert json.loads(response._content)['detail'] == 'Education company not found'

    clear_db(EducationCompany)
