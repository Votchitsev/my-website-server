import json 

from test.common import client, clear_db, session
from database.models import Skill, Language, EducationCompany


def test_create_skill():
    client.post('edu/', json = {
        "name": "Тестовое Имя",
        "start_education_date": "2022-01-01",
        "finish_education_date": "2023-01-01",
        "logo": "path_to_logo",
        "language": "ru"
    })

    education_company = session.query(EducationCompany).join(Language).filter(Language.name == 'ru').first()

    response = client.post('/skill', json = {
        "name": "Тестовый навык",
        "education_company_id": education_company.id,
        "language": 'ru'
    })

    query_response = session.query(Skill).join(EducationCompany).join(Language).\
        filter(EducationCompany.id == education_company.id, Language.name == 'ru')

    assert response.status_code == 200
    assert len(query_response.all()) == 1
    assert query_response.first().name == 'Тестовый навык'


def test_get_skill():
    education_company = session.query(EducationCompany).join(Language).filter(Language.name == 'ru').first()

    response = client.get(f'/skill/?lang=ru&edu_id={education_company.id}')

    assert json.loads(response._content)["skills"] == [{
            "name": "Тестовый навык",
            "education_company_id": 1,
            "language_id": 1,
            "id": 1
        }]
        
    clear_db(Skill)
    clear_db(EducationCompany)
