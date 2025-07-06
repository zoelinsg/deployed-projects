from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, MarkdownPreview, ResumeViewSet, ProjectViewSet, project_detail, resume_detail

# 創建 DefaultRouter 實例
router = DefaultRouter()
router.register(r'resume', ResumeViewSet)  # 註冊 ResumeViewSet 到 router
router.register(r'projects', ProjectViewSet)  # 註冊 ProjectViewSet 到 router

urlpatterns = [
    # 首頁路由
    path('', index, name='index'),  # 首頁

    # API 路由
    path('api/', include(router.urls)),  # 包含 router 生成的所有路由
    path('api/markdown-preview/', MarkdownPreview.as_view(), name='markdown-preview'),  # 新增 Markdown 預覽 API

    # 專案路由
    path('projects/<int:pk>/', project_detail, name='project-detail'),  # 專案詳情

    # 履歷路由
    path('resume/', resume_detail, name='resume-detail'),  # 履歷詳情
]