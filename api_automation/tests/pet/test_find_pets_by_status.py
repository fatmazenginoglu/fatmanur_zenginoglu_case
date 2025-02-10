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
