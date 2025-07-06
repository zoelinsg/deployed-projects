from django.shortcuts import render, get_object_or_404
import markdown
from rest_framework import viewsets, status
from .models import Resume, Project
from .serializers import ResumeSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files import File
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

# 首頁為專案列表視圖
def index(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# 專案詳情視圖
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.description = project.formatted_markdown()  # 將描述轉換為 HTML 格式
    return render(request, 'project_detail.html', {'project': project})

# 履歷 API
class ResumeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

# 專案 API
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# 履歷詳情視圖
def resume_detail(request):
    resume = Resume.objects.first()  # 假設只有一份履歷
    if resume:
        resume.content = resume.formatted_markdown()  # 將內容轉換為 HTML 格式
        return render(request, 'resume_detail.html', {'resume': resume})
    return render(request, 'resume_detail.html', {'resume': None})

# Markdown 預覽
class MarkdownPreview(APIView):
    def post(self, request):
        content = request.data.get('content', '')
        html_content = markdown.markdown(content)
        return Response({'html': html_content}, status=status.HTTP_200_OK)

# 測試受保護的 API
class ProtectedAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_protected_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)