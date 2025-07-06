from django.contrib import admin
from .models import ContactMessage

# 註冊 ContactMessage 模型到 Django 管理後台
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')  # 顯示的欄位
    search_fields = ('name', 'email', 'message')  # 可搜尋的欄位