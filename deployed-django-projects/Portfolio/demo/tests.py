from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

# 測試受保護的 API
class ProtectedAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = AccessToken.for_user(self.user)

    def test_protected_view(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get('/api/projects/')  # 確保這個 URL 存在於你的路由中
        self.assertEqual(response.status_code, 200)  # 檢查是否成功訪問受保護的 API