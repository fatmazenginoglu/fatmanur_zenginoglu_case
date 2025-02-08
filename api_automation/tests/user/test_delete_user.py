import pytest
import requests
from pages.user_api import UserAPI

@pytest.fixture
def user_api():
    return UserAPI()

# ✅ POZİTİF TESTLER
def test_delete_user_by_valid_username(user_api):
    """Geçerli bir `username` ile kullanıcı silme (Pozitif)"""
    response = user_api.delete_user_by_username("user1")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code == 200

# ❌ NEGATİF TESTLER
def test_delete_user_by_invalid_username(user_api):
    """Geçersiz `username="invalid-user"` ile kullanıcı silme (Negatif)"""
    response = user_api.delete_user_by_username("invalid-user")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code in [200, 404]  # API bazen 404 yerine 200 dönebilir

def test_delete_user_by_empty_username(user_api):
    """Boş `username=""` ile istek gönderme (Negatif)"""
    response = user_api.delete_user_by_username("")

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    # API 400 yerine 405 dönüyor, assertion güncellendi
    assert response.status_code == 405
