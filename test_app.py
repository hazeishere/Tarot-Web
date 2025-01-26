from app import app
from cards import get_cards
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_cards():
    card, card_value = get_cards()
    assert card is not None
    assert card_value is not None

def test_index_get(client):
    response = client.get("/")
    assert response.status_code == 200

def test_index_post(client):
    response = client.post("/", data={"question": "what is the meaning of life?"}, follow_redirects=True)
    assert response.status_code == 200
    
def test_get_card(client):
    response = client.get("/get_card")
    assert response.status_code == 200
    assert b"image" in response.data
    assert b"keywords" in response.data


