import sys
sys.path.append("C:/Users/Rise Technology/test_automation/API")
from pages.store_api import StoreAPI

import pytest
import requests
from pages.store_api import StoreAPI

@pytest.fixture
def store_api():
    return StoreAPI()

# ✅ POZİTİF TESTLER
def test_get_inventory_success(store_api):
    """Stok durumu başarılı şekilde getirme (Pozitif)"""
    response = store_api.get_inventory()

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.json())

    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Yanıtın sözlük (dict) formatında olması gerekir
    assert all(isinstance(value, int) for value in response.json().values())  # Tüm değerlerin integer olması gerekir

# ❌ NEGATİF TESTLER
def test_get_inventory_with_invalid_method(store_api):
    """Geçersiz HTTP metodu ile istek gönderme (`POST /store/inventory`) (Negatif)"""
    response = requests.post(f"{store_api.base_url}/inventory")  # GET yerine POST kullanılıyor

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code == 405  # Method Not Allowed
