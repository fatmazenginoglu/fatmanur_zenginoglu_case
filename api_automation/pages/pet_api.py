import requests
from utils.config import BASE_URL

class PetAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/pet"

    def upload_pet_image(self, pet_id, image_path, additional_metadata=""):
        """Bir pet için resim yükler."""
        url = f"{self.base_url}/{pet_id}/uploadImage"
        files = {"file": open(image_path, "rb")}
        data = {"additionalMetadata": additional_metadata}

        response = requests.post(url, files=files, data=data)
        files["file"].close()  # Dosyayı kapatalım, aksi halde sorun çıkarabilir.
        return response

    def create_pet(self, pet_id, name, category_id=0, category_name="default", 
                   photo_urls=None, tags=None, status="available"):
        """Yeni bir pet oluşturur."""

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
        """Var olan bir pet'i günceller."""

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
        """Belirtilen duruma göre pet'leri getirir."""
        params = {"status": status}
        response = requests.get(f"{self.base_url}/findByStatus", params=params)
        return response

    def get_pet_by_id(self, pet_id):
        """Belirtilen pet ID'ye göre pet bilgilerini getirir."""
        response = requests.get(f"{self.base_url}/{pet_id}")
        return response

    def update_pet_by_form(self, pet_id, name=None, status=None):
        """Belirtilen pet ID'yi form verisi ile günceller."""
        url = f"{self.base_url}/{pet_id}"
        data = {}

        if name:
            data["name"] = name
        if status:
            data["status"] = status

        response = requests.post(url, data=data)
        return response

    def delete_pet_by_id(self, pet_id, api_key=""):
        """Belirtilen pet ID'yi siler."""
        url = f"{self.base_url}/{pet_id}"
        headers = {"api_key": api_key} if api_key else {}

        response = requests.delete(url, headers=headers)
        return response
