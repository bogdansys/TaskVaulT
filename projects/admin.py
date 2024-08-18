from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'created_by__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('created_at',)

admin.site.register(Project, ProjectAdmin)