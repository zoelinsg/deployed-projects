from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth.models import User
from .models import ContactMessage
from django.core import mail
from django.core.cache import cache

# 建立測試案例
class ContactMessageTests(TestCase):

    # 設定測試資料
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.contact_message = ContactMessage.objects.create(name='Test User', email='test@example.com', message='Test Message')

    # 測試留言表單視圖
    def test_contact_form_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)  # 檢查是否成功加載頁面