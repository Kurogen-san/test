from django.contrib import admin
from .models import AdminLog, SystemSettings

@admin.register(AdminLog)
class AdminLogAdmin(admin.ModelAdmin):
    """管理ログ管理"""
    list_display = ('user', 'action', 'ip_address', 'created_at')
    list_filter = ('action', 'created_at', 'user')
    search_fields = ('user__username', 'action', 'details')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    """システム設定管理"""
    list_display = ('key', 'value', 'updated_at')
    search_fields = ('key', 'value')
    readonly_fields = ('updated_at',)
