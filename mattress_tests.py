import requests
import pytest

url = "http://localhost:4200"

@pytest.fixture
def create_mattress():
	new_mattress = { "name": "name", "price": 1500 }
	response = requests.post(f"{url}/mattress", json=new_mattress)
	assert response.status_code == 201
	
	data = response.json()
	assert data["name"] == new_mattress["name"]
	mattress_id = data["id"]

	return mattress_id

def test_create_mattress():
	new_mattress = { "name": "name", "price": 1500 }
	response = requests.post(f"{url}/mattress", json=new_mattress)
	assert response.status_code == 201
	
	data = response.json()
	assert data["name"] == new_mattress["name"]

def test_get_mattress(create_mattress):
	mattress_id = create_mattress

	response = requests.get(f"{url}/mattress/{mattress_id}")
	assert response.status_code == 200

def test_get_mattresss():
	response = requests.get(f"{url}/mattress")
	assert response.status_code == 200

	data = response.json()

	assert isinstance(data, list)
	assert len(data) > 0

def test_update_mattress(create_mattress):
	mattress_id = create_mattress
	
	updated_mattress = { "name": "name", "price": 1500 }

	response = requests.patch(f"{url}/mattress/{mattress_id}", json=updated_mattress)
	assert response.status_code == 200
	
	data = response.json()
	assert data["name"] == updated_mattress["name"]

def test_delete_mattress(create_mattress):
	mattress_id = create_mattress

	response = requests.delete(f"{url}/mattress/{mattress_id}")
	assert response.status_code == 200