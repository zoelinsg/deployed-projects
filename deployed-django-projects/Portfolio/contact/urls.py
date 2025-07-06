from django.urls import path
from django.contrib.auth import views as auth_views  # 確保導入 auth_views
from django.views.generic import TemplateView  # 確保導入 TemplateView
from .views import contact_view, contact_success, contact_limit, ContactMessageCreate

urlpatterns = [
    # API 路由
    path('api/contact/', ContactMessageCreate.as_view(), name='contact-message-create'),  # 留言創建
    
    # 網頁路由
    path('contact/', contact_view, name='contact'),  # 留言頁面
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact-success'),  # 留言成功頁面
    path('contact/limit/', TemplateView.as_view(template_name='contact_limit.html'), name='contact-limit'),  # 留言限制頁面
]