from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_developer():
    response = client.post('/api/developers', json={
        "name": "Cesar",
        "country": "Ecuador",
        "age": 26,
        "experience":[
            {
                "title": "Frontend Developer",
                "location": "Ecuador",
                "start_date": "2021",
                "end_date": "Present",
                "organization": "Real company"
            }
        ],
        "skills": [
            
        ],
        "languages": [
            {
                "name": "Spanish",
                "level": "native"
            },
            {
                "name": "English",
                "level": "intermediate"
            }
        ]
    })

    assert response.status_code == 201


def test_get_developers():
    response = client.get('/api/developers')
    assert response.status_code == 200

def test_get_developer():
    response = client.get('/api/developers/62c3d228599b6e5d75b0b1aa')
    assert response.status_code == 200

def test_get_skills():
    response = client.get('/api/developers/62c3d228599b6e5d75b0b1aa/skills')
    assert response.status_code == 200


def test_update_developer():
    response = client.put('/api/developers/62c3d228599b6e5d75b0b1aa', json={
        "name": "Cesar",
        "country": "Ecuador",
        "age": 26,
        "experience":[
            {
                "title": "Frontend Developer",
                "location": "Ecuador",
                "start_date": "2021",
                "end_date": "Present",
                "organization": "Real company"
            }
        ],
        "skills": [
            
        ],
        "languages": [
            {
                "name": "Spanish",
                "level": "native"
            },
            {
                "name": "English",
                "level": "intermediate"
            }
        ]
    })

    assert response.status_code == 201

def test_delete_developer():
    response = client.delete('/api/developers/6268d00eb6b68776a1ffbde7')
    assert response.status_code == 200