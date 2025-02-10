import pytest
import requests
from pages.pet_api import PetAPI

@pytest.fixture
def pet_api():
    return PetAPI()

# POSITIVE TESTS
def test_delete_existing_pet(pet_api):
    """Delete a pet using a valid pet ID"""
    pet_api.create_pet(2, "Bulldog")
    response = pet_api.delete_pet_by_id(2)

    assert response.status_code == 200

# NEGATIVE TESTS
def test_delete_pet_by_invalid_id(pet_api):
    """Send a request with an invalid ID (`petId="invalid"`)"""
    response = pet_api.delete_pet_by_id("invalid")

    assert response.status_code == 404

def test_delete_non_existent_pet(pet_api):
    """Send a request to delete a pet that does not exist (`petId=9999999`)"""
    response = pet_api.delete_pet_by_id(9999999)

    assert response.status_code == 404

def test_delete_pet_by_negative_id(pet_api):
    """Send a request to delete a pet using a negative ID (`petId=-1`)"""
    response = pet_api.delete_pet_by_id(-1)

    assert response.status_code == 404
