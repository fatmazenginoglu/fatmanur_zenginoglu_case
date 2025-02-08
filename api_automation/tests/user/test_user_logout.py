import pytest
from pages.user_api import UserAPI

@pytest.fixture
def user_api():
    return UserAPI()

def test_logout_user(user_api):
    """✅ Kullanıcı oturumunun başarıyla kapatılması"""
    response = user_api.logout_user()

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    assert response.status_code == 200  # Başarılı işlem
