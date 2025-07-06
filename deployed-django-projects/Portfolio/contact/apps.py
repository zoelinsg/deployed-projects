from django.apps import AppConfig

# 設定 Contact 應用程式的配置
class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'  # 應用程式名稱