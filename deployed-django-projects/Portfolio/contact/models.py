from datetime import timedelta
from django.utils import timezone
from django.db import models

# 創建 ContactMessage 模型，用於存儲留言資料
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 檢查是否在 15 分鐘內已經有留言
        last_comment = ContactMessage.objects.filter(email=self.email).order_by('-created_at').first()
        if last_comment and timezone.now() - last_comment.created_at < timedelta(minutes=15):
            raise ValueError("每 15 分鐘只能留言一次")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Message from {self.email}"  # 返回留言者的電子郵件作為表示