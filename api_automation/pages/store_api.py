import requests
from utils.config import BASE_URL

class StoreAPI:
    def __init__(self):
        self.base_url = f"{BASE_URL}/store"

    def get_inventory(self):
        """Mevcut stok durumunu getirir."""
        response = requests.get(f"{self.base_url}/inventory")
        return response

    def create_order(self, pet_id, quantity, ship_date, status="placed", complete=True):
        """Belirtilen pet için sipariş oluşturur."""
        url = f"{self.base_url}/order"
        data = {
            "petId": pet_id,
            "quantity": quantity,
            "shipDate": ship_date,
            "status": status,
            "complete": complete
        }
        response = requests.post(url, json=data)
        return response

    def get_order_by_id(self, order_id):
        """Belirtilen sipariş ID'ye ait sipariş detaylarını getirir."""
        url = f"{self.base_url}/order/{order_id}"
        response = requests.get(url)
        return response

    def delete_order_by_id(self, order_id):
        """Belirtilen sipariş ID'ye ait siparişi siler."""
        url = f"{self.base_url}/order/{order_id}"
        response = requests.delete(url)
        return response
