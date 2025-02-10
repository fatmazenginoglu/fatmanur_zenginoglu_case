import pytest
import requests
from pages.pet_api import PetAPI

@pytest.fixture
def pet_api():
    return PetAPI()

# POSITIVE TEST CASES
def test_create_pet_success(pet_api):
    """Adding a valid pet (Positive)"""
    response = pet_api.create_pet(1005, "Golden Retriever")
    assert response.status_code in [200]
    assert response.json()["name"] == "Golden Retriever"

def test_create_pet_with_different_category(pet_api):
    """Adding a pet with a different category and tag"""
    response = pet_api.create_pet(1006, "Siamese Cat", category_id=1, category_name="Cat", 
                                  tags=[{"id": 1, "name": "Cute"}])
    assert response.status_code in [200]
    assert response.json()["category"]["name"] == "Cat"

# NEGATIVE TEST CASES 
def test_create_pet_without_name(pet_api):
    """Sending a request without the `name` field"""
    response = pet_api.create_pet(1007, None)
    assert response.status_code == 200 

def test_create_pet_without_photo_urls(pet_api):
    """Sending a request without the `photoUrls` field"""
    response = pet_api.create_pet(1008, "NoPhotoPet", photo_urls=[])
    assert response.status_code == 200

def test_create_pet_with_invalid_status(pet_api):
    """Sending a request with an invalid `status` value"""
    response = pet_api.create_pet(1009, "WeirdPet", status="notavailable")
    assert response.status_code == 200

def test_create_pet_with_empty_body(pet_api):
    """Sending a completely empty JSON request"""
    response = requests.post(pet_api.base_url, json={})
    assert response.status_code == 200

def test_create_pet_with_string_id(pet_api):
    """Sending the `id` field as a string"""
    response = pet_api.create_pet("string_id", "InvalidIDPet")
    assert response.status_code == 500

def test_create_pet_with_get_method(pet_api):
    """Trying to create a pet using the GET method"""
    response = requests.get(pet_api.base_url)
    assert response.status_code == 405
