import json

from database.models import Feedback
from test.common import client, clear_db, session


def test_create_feedback():
    response = client.post(
        'feedback/',
        json = {
            "date": "2023-01-01",
            "name": "Test name",
            "email": "test@test.com",
            "message": "Test text"
        }
    )

    query_response = session.query(Feedback).all()

    assert response.status_code == 200
    assert len(query_response) == 1
    assert query_response[0].name == 'Test name'
    

def test_get_feedback():
    response = client.get('feedback/')

    assert response.status_code == 200
    assert json.loads(response._content)['feedback'][0]['name'] == 'Test name'


def test_delete_feedback():
    client.delete('feedback/?id=1')

    query_response = session.query(Feedback).all()

    assert len(query_response) == 0
