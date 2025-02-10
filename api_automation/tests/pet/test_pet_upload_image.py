import pytest
import os
import requests
from pages.pet_api import PetAPI

# Test files
TEST_IMAGE_PATH = r"C:\Users\Rise Technology\Pictures\Screenshots/Ekran görüntüsü 2025-02-06 154246.png"
UNSUPPORTED_IMAGE_PATH = r"C:\Users\Rise Technology\Documents\Gönderi.xlsx"
EMPTY_IMAGE_PATH = ""
API_URL = "https://petstore.swagger.io/v2/pet/{}/uploadImage"

@pytest.fixture
def pet_api():
    return PetAPI()

# Positive Test Cases
def test_upload_pet_image_success(pet_api):
    """Successfully uploading an image for a pet"""
    with open(TEST_IMAGE_PATH, "rb") as image_file:
        files = {"file": image_file}
        response = requests.post(API_URL.format(1), files=files, headers={"accept": "application/json"})
    
    assert response.status_code == 200
    json_data = response.json()
    assert "code" in json_data
    assert "message" in json_data
    assert "File uploaded to" in json_data["message"]

# Negative Test Cases
def test_upload_pet_image_invalid_pet(pet_api):
    """Attempting to upload an image for a non-existent pet"""
    with open(TEST_IMAGE_PATH, "rb") as image_file:
        files = {"file": image_file}
        response = requests.post(API_URL.format(9999), files=files, headers={"accept": "application/json"})
    
    assert response.status_code in [200]
    assert "message" in response.json()

def test_upload_pet_image_empty_metadata(pet_api):
    """Uploading an image with empty additionalMetadata"""
    with open(TEST_IMAGE_PATH, "rb") as image_file:
        files = {"file": image_file}
        response = requests.post(API_URL.format(1), files=files, headers={"accept": "application/json"})
    
    assert response.status_code == 200
    json_data = response.json()
    assert "code" in json_data
    assert "message" in json_data

def test_upload_pet_excel_file(pet_api):
    """Successfully uploading an Excel file for a pet"""
    with open(UNSUPPORTED_IMAGE_PATH, "rb") as excel_file:
        files = {"file": ("Gönderi.xlsx", excel_file, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        data = {"additionalMetadata": "fatma"}
        response = requests.post(API_URL.format(1), files=files, data=data, headers={"accept": "application/json"})
    
    assert response.status_code == 200
    json_data = response.json()
    assert "code" in json_data
    assert "message" in json_data
    assert "File uploaded to" in json_data["message"]
    assert "additionalMetadata: fatma" in json_data["message"]

def test_upload_pet_image_empty_file(pet_api):
    """Uploading only metadata without an image, expecting 500 Internal Server Error"""
    response = requests.post(
        API_URL.format(1),
        files={},
        data={"additionalMetadata": "fatma"},
        headers={"accept": "application/json", "Content-Type": "multipart/form-data"}
    )
    
    assert response.status_code == 500  # Internal Server Error expected
    assert "Internal Server Error" in response.text
