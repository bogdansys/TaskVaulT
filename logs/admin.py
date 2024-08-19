from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    search_fields = ('user__username', 'action')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)

admin.site.register(Log, LogAdmin)