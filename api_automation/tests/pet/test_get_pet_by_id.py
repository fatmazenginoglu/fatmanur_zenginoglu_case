import pytest
import requests
from pages.pet_api import PetAPI

@pytest.fixture
def pet_api():
    return PetAPI()

# POSITIVE TEST CASES
def test_find_pets_by_status_available(pet_api):
    """Retrieve pets with `status=available`"""
    response = pet_api.find_pets_by_status("available")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_pets_by_status_pending(pet_api):
    """Retrieve pets with `status=pending`"""
    response = pet_api.find_pets_by_status("pending")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_pets_by_status_sold(pet_api):
    """Retrieve pets with `status=sold`"""
    response = pet_api.find_pets_by_status("sold")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_pet_by_valid_id(pet_api):
    """Retrieve pet details with a valid pet ID"""
    pet_api.create_pet(1, "doggie")
    response = pet_api.get_pet_by_id(1)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "doggie"

def test_get_pet_by_different_id(pet_api):
    """Retrieve pet details with different pet IDs"""
    pet_api.create_pet(8, "PetH")
    response = pet_api.get_pet_by_id(8)
    assert response.status_code == 200
    assert response.json()["id"] == 8
    assert response.json()["name"] == "PetH"

# NEGATIVE TEST CASES
def test_find_pets_by_invalid_status(pet_api):
    """Send request with invalid `status=invalid`"""
    response = pet_api.find_pets_by_status("invalid")
    assert response.status_code == 400
    assert response.json() == []  

def test_find_pets_without_status(pet_api):
    """Make a request without sending any `status` parameter"""
    response = requests.get(f"{pet_api.base_url}/findByStatus")  
    assert response.status_code == 400  
    assert response.json() == []

def test_get_pet_by_invalid_id(pet_api):
    """Send request with an invalid pet ID (`petId="invalid"`)"""
    response = pet_api.get_pet_by_id("invalid")
    assert response.status_code == 404 

def test_get_non_existent_pet(pet_api):
    """Send request with a non-existent pet ID (`petId=99999999999999999999999`)"""
    response = pet_api.get_pet_by_id(99999999999999999999999)
    assert response.status_code in [404]

def test_get_pet_by_negative_id(pet_api):
    """Send request with a negative pet ID (`petId=-1`)"""
    response = pet_api.get_pet_by_id(-1)
    assert response.status_code == 404
