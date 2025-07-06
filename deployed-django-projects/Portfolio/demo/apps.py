from django.apps import AppConfig

# 設定 Demo 應用程式的配置
class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demo'  # 應用程式名稱