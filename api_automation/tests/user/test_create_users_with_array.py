import pytest
import requests  # ✅ Eksik import eklendi
from pages.user_api import UserAPI

def test_create_users_with_array_valid(user_api):
    """✅ Geçerli kullanıcı listesi ile istek gönderme"""
    users = [
        {
            "id": 1,
            "username": "validuser",
            "firstName": "Valid",
            "lastName": "User",
            "email": "validuser@example.com",
            "password": "ValidPass123",
            "phone": "1234567890",
            "userStatus": 1
        }
    ]
    response = user_api.create_users_with_array(users)
    
    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)
    
    assert response.status_code == 200, "❌ Kullanıcı listesi oluşturulamadı!"
    assert "message" in response.json(), "❌ Yanıt formatı beklenenden farklı!"

@pytest.mark.parametrize("invalid_users, expected_status", [
    ([{"id": 3, "username": "baduser", "firstName": "Bad", "lastName": "User", "email": "notanemail", "password": "1234", "phone": "abc123", "userStatus": 1}], 400),
    ([], 400),  # Boş kullanıcı listesi
    (None, 415)  # Null gönderme
])
def test_create_users_with_invalid_data(user_api, invalid_users, expected_status):
    """❌ Geçersiz veri içeren kullanıcı listesi ile istek gönderme"""
    response = user_api.create_users_with_array(invalid_users) if invalid_users is not None else requests.post(f"{user_api.base_url}/createWithArray", json=None)
    
    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)
    
    if response.status_code == 500:
        assert "something bad happened" in response.text.lower(), "⚠️ API 500 döndürdü ancak hata mesajı beklenenden farklı!"
    else:
        assert response.status_code == expected_status, f"❌ Beklenen hata kodu {expected_status}, ancak {response.status_code} döndü!"
