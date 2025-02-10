import pytest
import requests
from pages.pet_api import PetAPI

@pytest.fixture
def pet_api():
    return PetAPI()

# POSITIVE TESTS
def test_update_pet_name_and_status(pet_api):
    """Update both pet name and status using a valid pet ID"""
    response = pet_api.update_pet_by_form(10, name="Golden Updated", status="sold")

    assert response.status_code == 200

def test_update_pet_only_name(pet_api):
    """Update only the pet name"""
    response = pet_api.update_pet_by_form(13, name="Persian Updated")

    assert response.status_code == 200

def test_update_pet_only_status(pet_api):
    """Update only the pet status"""
    response = pet_api.update_pet_by_form(12, status="pending")

    assert response.status_code == 200

# NEGATIVE TESTS
def test_update_non_existent_pet(pet_api):
    """Attempt to update a non-existent pet ID (`petId=999999999999`)"""
    response = pet_api.update_pet_by_form(999999999999, name="GhostPet", status="sold")

    assert response.status_code == 404

def test_update_pet_by_invalid_id(pet_api):
    """Send a request with an invalid ID (`petId="invalid"`)"""
    response = pet_api.update_pet_by_form("invalid", name="InvalidPet", status="sold")

    assert response.status_code == 404

def test_update_pet_without_data(pet_api):
    """Attempt to update a pet without providing any data"""
    pet_api.create_pet(1033, "Beagle", status="available")
    response = pet_api.update_pet_by_form(1033)  

    assert response.status_code == 200
