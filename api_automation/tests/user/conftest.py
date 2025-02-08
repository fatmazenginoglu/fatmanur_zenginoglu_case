import pytest
from pages.user_api import UserAPI

@pytest.fixture
def user_api():
    """UserAPI Fixture - Kullanıcı API bağlantısını sağlar"""
    base_url = "https://petstore.swagger.io/v2"
    return UserAPI(base_url)
