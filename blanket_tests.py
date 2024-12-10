import requests
import pytest

url = "http://localhost:4200"

@pytest.fixture
def create_blanket():
	new_blanket = { "name": "name", "price": 1500 }
	response = requests.post(f"{url}/blanket", json=new_blanket)
	assert response.status_code == 201
	
	data = response.json()
	assert data["name"] == new_blanket["name"]
	blanket_id = data["id"]

	return blanket_id

def test_create_blanket():
	new_blanket = { "name": "name", "price": 1500 }
	response = requests.post(f"{url}/blanket", json=new_blanket)
	assert response.status_code == 201
	
	data = response.json()
	assert data["name"] == new_blanket["name"]

def test_get_blanket(create_blanket):
	blanket_id = create_blanket

	response = requests.get(f"{url}/blanket/{blanket_id}")
	assert response.status_code == 200

def test_get_blankets():
	response = requests.get(f"{url}/blanket")
	assert response.status_code == 200

	data = response.json()

	assert isinstance(data, list)
	assert len(data) > 0

def test_update_blanket(create_blanket):
	blanket_id = create_blanket
	
	updated_blanket = { "name": "name", "price": 1500 }

	response = requests.patch(f"{url}/blanket/{blanket_id}", json=updated_blanket)
	assert response.status_code == 200
	
	data = response.json()
	assert data["name"] == updated_blanket["name"]

def test_delete_blanket(create_blanket):
	blanket_id = create_blanket

	response = requests.delete(f"{url}/blanket/{blanket_id}")
	assert response.status_code == 200