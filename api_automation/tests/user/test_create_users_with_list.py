import pytest
import requests
from pages.user_api import UserAPI

@pytest.fixture
def user_api():
    """UserAPI fixture'ı"""
    return UserAPI()

# ✅ **POZİTİF TESTLER**
def test_create_users_with_valid_list(user_api):
    """✅ Geçerli bir kullanıcı listesi ile kullanıcı oluşturma (Pozitif)"""
    users = [
        {
            "id": 1,
            "username": "johndoe",
            "firstName": "John",
            "lastName": "Doe",
            "email": "johndoe@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        },
        {
            "id": 2,
            "username": "janedoe",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "janedoe@example.com",
            "password": "securepass",
            "phone": "0987654321",
            "userStatus": 1
        }
    ]
    
    response = user_api.create_users_with_list(users)

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.json())

    assert response.status_code == 200, "❌ Kullanıcı listesi oluşturulamadı!"
    assert response.json().get("message") == "ok", "❌ Yanıt beklenen 'ok' mesajını içermiyor!"

# ❌ **NEGATİF TESTLER**  
def test_create_users_with_invalid_data(user_api):
    """❌ Geçersiz `email` ve eksik `id` ile kullanıcı oluşturma"""
    users = [
        {
            "id": 3,
            "username": "baduser",
            "firstName": "Bad",
            "lastName": "User",
            "email": "notanemail",  # Geçersiz email formatı
            "password": "1234",  # Zayıf şifre
            "phone": "abc123",  # Geçersiz telefon formatı
            "userStatus": 1
        }
    ]
    
    response = user_api.create_users_with_list(users)

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code in [400, 200], "⚠️ API beklenen hata kodunu döndürmedi!"
    if response.status_code == 200:
        assert "invalid" in response.text.lower() or "error" in response.text.lower(), \
            "⚠️ API hatalı veriyi kabul etti, ancak hata mesajı içermiyor!"

def test_create_users_with_empty_list(user_api):
    """❌ Boş bir liste ile istek gönderme"""
    users = []
    response = user_api.create_users_with_list(users)

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code in [400, 200], "⚠️ API beklenen hata kodunu döndürmedi!"
    if response.status_code == 200:
        assert "invalid" in response.text.lower() or "error" in response.text.lower(), \
            "⚠️ API boş listeyi kabul etti, ancak hata mesajı içermiyor!"

def test_create_users_with_null(user_api):
    """❌ `null` olarak istek gönderme"""
    response = requests.post(f"{user_api.base_url}/createWithList", json=None)

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code == 415, "⚠️ API `null` isteğine beklenmeyen bir yanıt döndürdü!"
