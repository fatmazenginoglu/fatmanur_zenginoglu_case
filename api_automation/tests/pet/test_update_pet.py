import pytest
import requests
from pages.pet_api import PetAPI

@pytest.fixture
def pet_api():
    return PetAPI()

# POSITIVE TESTS
def test_update_pet_success(pet_api):
    """Successfully updating an existing pet"""
    pet_api.create_pet(1010, "Golden Retriever")
    response = pet_api.update_pet(1010, "Golden Retriever Updated")

    assert response.status_code == 200
    assert response.json()["name"] == "Golden Retriever Updated"

def test_update_pet_status_change(pet_api):
    """Changing a pet's status"""
    pet_api.create_pet(1011, "Persian Cat", status="available")
    response = pet_api.update_pet(1011, "Persian Cat", status="sold")

    assert response.status_code == 200
    assert response.json()["status"] == "sold"

# NEGATIVE TESTS
def test_update_pet_invalid_id(pet_api):
    """Updating with an invalid ID (string)"""
    response = pet_api.update_pet("invalid_id", "InvalidPet")

    assert response.status_code in [500] 

def test_update_non_existent_pet(pet_api):
    """Trying to update a non-existent pet"""
    response = pet_api.update_pet(99999999999999999999, "GhostPet")

    assert response.status_code in [500]

def test_update_pet_with_missing_fields(pet_api):
    """Sending a request with missing fields"""
    response = requests.put(pet_api.base_url, json={"id": 1012})

    assert response.status_code in [200]
