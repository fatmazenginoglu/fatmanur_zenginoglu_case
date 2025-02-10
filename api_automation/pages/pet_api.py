import requests
from utils.config import BASE_URL

class PetAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/pet"

    def upload_pet_image(self, pet_id, image_path, additional_metadata=""):
        """Uploads an image for a pet."""
        url = f"{self.base_url}/{pet_id}/uploadImage"
        files = {"file": open(image_path, "rb")}
        data = {"additionalMetadata": additional_metadata}

        response = requests.post(url, files=files, data=data)
        files["file"].close()  # Close the file to prevent issues.
        return response

    def create_pet(self, pet_id, name, category_id=0, category_name="default", 
                   photo_urls=None, tags=None, status="available"):
        """Creates a new pet."""

        if photo_urls is None:
            photo_urls = ["https://example.com/default.jpg"]

        if tags is None:
            tags = [{"id": 0, "name": "default"}]

        payload = {
            "id": pet_id,
            "category": {"id": category_id, "name": category_name},
            "name": name,
            "photoUrls": photo_urls,
            "tags": tags,
            "status": status
        }

        response = requests.post(self.base_url, json=payload)
        return response

    def update_pet(self, pet_id, name, category_id=0, category_name="string",
                   photo_urls=None, tags=None, status="available"):
        """Updates an existing pet."""

        if photo_urls is None:
            photo_urls = ["https://example.com/default.jpg"]

        if tags is None:
            tags = [{"id": 0, "name": "string"}]

        payload = {
            "id": pet_id,
            "category": {"id": category_id, "name": category_name},
            "name": name,
            "photoUrls": photo_urls,
            "tags": tags,
            "status": status
        }

        response = requests.put(self.base_url, json=payload)
        return response

    def find_pets_by_status(self, status):
        """Retrieves pets based on the specified status."""
        params = {"status": status}
        response = requests.get(f"{self.base_url}/findByStatus", params=params)
        return response

    def get_pet_by_id(self, pet_id):
        """Fetches pet details based on the given pet ID."""
        response = requests.get(f"{self.base_url}/{pet_id}")
        return response

    def update_pet_by_form(self, pet_id, name=None, status=None):
        """Updates the specified pet ID using form data."""
        url = f"{self.base_url}/{pet_id}"
        data = {}

        if name:
            data["name"] = name
        if status:
            data["status"] = status

        response = requests.post(url, data=data)
        return response

    def delete_pet_by_id(self, pet_id, api_key=""):
        """Deletes a pet based on the given pet ID."""
        url = f"{self.base_url}/{pet_id}"
        headers = {"api_key": api_key} if api_key else {}

        response = requests.delete(url, headers=headers)
        return response
