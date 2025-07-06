from django.contrib import admin
from .models import Project, Tag, Resume

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url', 'updated_at')
    search_fields = ('name', 'description')
    filter_horizontal = ('tags',)  # 使用 filter_horizontal 來顯示多選框

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)