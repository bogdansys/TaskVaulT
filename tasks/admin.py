from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'assigned_to', 'project', 'created_at', 'updated_at')
    search_fields = ('title', 'assigned_to__username', 'project__name')
    list_filter = ('status', 'created_at', 'updated_at')
    ordering = ('created_at',)

admin.site.register(Task, TaskAdmin)