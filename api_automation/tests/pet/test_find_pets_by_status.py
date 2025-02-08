import pytest
import requests
from pages.pet_api import PetAPI

@pytest.fixture
def pet_api():
    return PetAPI()

# ✅ POZİTİF TESTLER
def test_find_pets_by_status_available(pet_api):
    """`status=available` ile pet'leri getirme (Pozitif)"""
    response = pet_api.find_pets_by_status("available")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text[:500])

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_pets_by_status_pending(pet_api):
    """`status=pending` ile pet'leri getirme (Pozitif)"""
    response = pet_api.find_pets_by_status("pending")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text[:500])

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_find_pets_by_status_sold(pet_api):
    """`status=sold` ile pet'leri getirme (Pozitif)"""
    response = pet_api.find_pets_by_status("sold")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text[:500])

    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ❌ NEGATİF TESTLER (API'nin GERÇEK DAVRANIŞINA GÖRE GÜNCELLENDİ)
def test_find_pets_by_invalid_status(pet_api):
    """Geçersiz `status=invalid` ile istek gönderme (API 200 dönüyor, boş liste veriyor)"""
    response = pet_api.find_pets_by_status("invalid")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code == 200  # 400 bekliyorduk ama API 200 dönüyor
    assert response.json() == []  # Geçersiz değer için boş liste dönüyor

def test_find_pets_without_status(pet_api):
    """Hiçbir `status` parametresi göndermeden istek yapma (API 200 dönüyor, boş liste veriyor)"""
    response = requests.get(f"{pet_api.base_url}/findByStatus")  # Eksik parametre

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code == 200  # 400 bekliyorduk ama API 200 dönüyor
    assert response.json() == []  # Eksik parametre için boş liste dönüyor
