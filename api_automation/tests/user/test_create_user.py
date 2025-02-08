import pytest
import requests

def test_create_user_success(user_api):
    """✅ Geçerli bir kullanıcı ile kullanıcı oluşturma (Pozitif)"""
    new_user = {
        "id": 101,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "Test@123",
        "phone": "123456789",
        "userStatus": 1
    }
    
    response = user_api.create_user(new_user)

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.json())

    assert response.status_code == 200, "❌ Kullanıcı oluşturulamadı!"
    assert "message" in response.json(), "❌ Yanıt formatı beklenenden farklı!"

@pytest.mark.parametrize("invalid_data, expected_status", [
    ({}, 400),  # Eksik tüm alanlar -> 400 Bad Request bekleniyor
    ({"username": "invaliduser"}, 400),  # Eksik bilgiler -> 400 Bad Request bekleniyor
    ({"id": "wrong_type", "username": "user1"}, 400)  # Yanlış veri tipi -> 400 Bad Request bekleniyor
])
def test_create_user_invalid_data(user_api, invalid_data, expected_status):
    """❌ Eksik veya hatalı veri ile kullanıcı oluşturma (Negatif)"""
    response = user_api.create_user(invalid_data)

    print("\n🔍 Yanıt Kodu:", response.status_code)
    print("📄 Yanıt İçeriği:", response.text)

    if response.status_code == 500:
        # Eğer API 500 döndürüyorsa, içeriğin gerçekten hata içerdiğini kontrol et
        assert "something bad happened" in response.text.lower(), \
            "⚠️ API 500 Internal Server Error döndürdü, ancak hata mesajı beklenenden farklı!"

    elif response.status_code == 200:
        # Eğer API 200 OK döndürüyorsa, hatalı veriyi kabul edip etmediğini incele
        response_json = response.json()
        message_content = str(response_json.get("message", "")).lower()

        assert any(keyword in message_content for keyword in ["invalid", "error", "bad request"]), \
            f"⚠️ API 200 OK döndürdü ancak hata mesajı içermiyor: {response_json}"

        # API yanlışlıkla kullanıcı oluşturduysa bunu da kontrol edelim
        assert response_json.get("code") != 200 or response_json.get("message") not in ["0", "9223372036854762413"], \
            f"⚠️ API yanlışlıkla geçersiz kullanıcıyı oluşturmuş olabilir! Yanıt: {response_json}"

    elif response.status_code == 400:
        # Eğer API 400 döndürüyorsa, hata mesajının uygun formatta olup olmadığını kontrol et
        assert any(keyword in response.text.lower() for keyword in ["error", "invalid", "bad request"]), \
            f"⚠️ API 400 Bad Request döndürdü, ancak hata mesajı beklenen formatta değil: {response.text}"

    else:
        pytest.fail(f"❌ Beklenmeyen bir HTTP yanıt kodu alındı: {response.status_code}")
