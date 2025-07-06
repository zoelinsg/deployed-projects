import os
from django.db import models
from markdownx.models import MarkdownxField  # 引入 MarkdownxField
from markdownx.utils import markdownify  # 引入 markdownify 用於轉換 Markdown 為 HTML

# 標籤模型
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # 修正拼寫錯誤

    def __str__(self):
        return self.name

# 履歷模型
class Resume(models.Model):
    title = models.CharField(max_length=200, help_text="例如：個人履歷")  # 修正拼寫錯誤
    content = MarkdownxField(help_text="可以用 Markdown 格式撰寫")  # 使用 MarkdownxField

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.content)  # 將內容轉換為 HTML 格式

# 專案模型
class Project(models.Model):
    name = models.CharField(max_length=200)  # 修正拼寫錯誤
    description = MarkdownxField(help_text="可以用 Markdown 格式撰寫")  # 使用 MarkdownxField
    url = models.URLField(blank=True, null=True)  # 沒上線的就不會有網址
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name='projects')  # 使用 ManyToManyField 來引用標籤
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # 新增影片檔案欄位

    def formatted_markdown(self):
        return markdownify(self.description)  # 將描述轉換為 HTML 格式