from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    """チャットメッセージ管理"""
    list_display = ('user_message', 'ai_response', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user_message', 'ai_response')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    # 一覧表示での文字数制限
    def user_message(self, obj):
        return obj.user_message[:50] + '...' if len(obj.user_message) > 50 else obj.user_message
    user_message.short_description = 'ユーザーメッセージ'
    
    def ai_response(self, obj):
        return obj.ai_response[:50] + '...' if len(obj.ai_response) > 50 else obj.ai_response
    ai_response.short_description = 'AI応答'
