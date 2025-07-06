from django import forms
from .models import ContactMessage

# 創建 ContactForm 表單類別，用於收集留言資料
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']  # 表單包含的欄位